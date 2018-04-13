from wagtail.api.v2.endpoints import filter_page_type, page_models_from_string
from wagtail.api.v2.utils import BadRequestError
from wagtail.wagtailadmin.api.endpoints import PagesAdminAPIEndpoint
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.models import Image
from wagtail.wagtailcore.models import Orderable

from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.forms.models import model_to_dict, ModelChoiceField
from django.shortcuts import get_object_or_404, Http404
from django.template.response import TemplateResponse
from django.utils import translation
from django.views.generic.edit import FormView

from config.signature import SignatureCheckPermission
from core import forms, helpers, permissions


class APIEndpointBase(PagesAdminAPIEndpoint):
    queryset = Page.objects.all()
    meta_fields = []
    known_query_parameters = (
        PagesAdminAPIEndpoint.known_query_parameters.union(
            ['lang', 'draft_token']
        )
    )

    @classmethod
    def get_nested_default_fields(cls, model):
        return [field.name for field in model.api_fields]

    @property
    def permission_classes(self):
        permission_classes = [SignatureCheckPermission]
        if helpers.is_draft_requested(self.request):
            permission_classes.append(permissions.DraftTokenPermisison)
        return permission_classes

    def handle_serve_draft_object(self, instance):
        if helpers.is_draft_requested(self.request):
            instance = instance.get_latest_nested_revision_as_page()
        return instance

    def handle_activate_language(self, instance):
        if translation.get_language() not in instance.translated_languages:
            translation.activate(settings.LANGUAGE_CODE)

    def get_object(self):
        instance = super().get_object()
        instance = self.handle_serve_draft_object(instance)
        self.handle_activate_language(instance)
        return instance


class PagesOptionalDraftAPIEndpoint(APIEndpointBase):
    pass


class PageLookupByTypeAPIEndpoint(APIEndpointBase):
    lookup_url_kwarg = 'page_type'
    detail_only_fields = ['id']

    def get_queryset(self):
        try:
            models = page_models_from_string(self.kwargs['page_type'])
        except (LookupError, ValueError):
            raise BadRequestError("type doesn't exist")
        return filter_page_type(models[0].objects.all(), models)

    def get_object(self):
        queryset = self.get_queryset()
        if not queryset.exists():
            raise Http404()
        instance = queryset.first()
        instance = self.handle_serve_draft_object(instance)
        self.handle_activate_language(instance)
        return instance

    def detail_view(self, *args, **kwargs):
        return super().detail_view(self.request, pk=None)


class CopyPageView(FormView):
    environment_form_class = forms.CopyToEnvironmentForm
    template_name = 'core/copy_to_environment.html'

    def get_form_class(self):
        page = self.get_object()
        return page.get_edit_handler().get_form_class(page.__class__)

    def get_form_kwargs(self):
        instance = self.get_object()
        initial = model_to_dict(instance)
        for f in instance._meta.concrete_fields:
            field = getattr(instance, f.name)
            if isinstance(field, Image) and field.file.name:
                initial[f.name] = field.file.name

        return {
            **super().get_form_kwargs(),
            'initial': initial,
        }

    def get_object(self):
        if not hasattr(self, 'object'):
            self.object = Page.objects.get(id=self.kwargs['pk']).specific
        return self.object

    def get_cluster_form_data(self):
        instance = self.get_object()
        cluster_data = {}
        for field in instance._meta.related_objects:
            if issubclass(field.related_model, Orderable):
                data = helpers.nested_form_data({
                    field.name: helpers.inline_formset([])
                })
                cluster_data.update(data)
        return cluster_data.items()

    def get_context_data(self, **kwargs):
        page = self.get_object()
        return super().get_context_data(
            environment_form=self.environment_form_class(),
            page=page,
            app_label=page._meta.app_label,
            model_name=page._meta.model_name,
            cluster_data=self.get_cluster_form_data(),
            **kwargs
        )


class PeloadPageView(FormView):
    template_name = 'wagtailadmin/pages/create.html'

    def get_form_class(self):
        content_type = self.get_content_type()
        page_class = content_type.model_class()
        return page_class.get_edit_handler().get_form_class(page_class)

    def get_content_type(self):
        try:
            return ContentType.objects.get_by_natural_key(
                self.kwargs['app_name'],
                self.kwargs['model_name'],
            )
        except ContentType.DoesNotExist:
            raise Http404()

    def get_parent(self):
        return get_object_or_404(Page, id=self.kwargs['parent_pk']).specific

    def get_context_data(self, form):
        content_type = self.get_content_type()
        page_class = content_type.model_class()
        page = page_class(owner=self.request.user)
        parent_page = self.get_parent()
        edit_handler_class = page_class.get_edit_handler()
        form_class = edit_handler_class.get_form_class(page_class)
        form = form_class(
            initial=form.cleaned_data,
            instance=page,
            parent_page=parent_page
        )
        return {
            'content_type': content_type,
            'page_class': page_class,
            'parent_page': parent_page,
            'edit_handler': edit_handler_class(instance=page, form=form),
            'preview_modes': page.preview_modes,
            'form': form,
            'has_unsaved_changes': True,
            **super().get_context_data(form=form),
        }

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['data'] = kwargs['data'].dict()
        form = self.get_form_class()()
        for name, field in form.fields.items():
            if isinstance(field, ModelChoiceField) and name in kwargs['data']:
                value = kwargs['data'][name]
                if value not in ['', 'None', None]:
                    image = helpers.get_or_create_image(value)
                    kwargs['data'][name] = image.pk

        return kwargs

    def form_valid(self, form):
        return TemplateResponse(
            self.request,
            self.template_name,
            self.get_context_data(form=form),
        )
