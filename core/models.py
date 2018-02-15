import functools
from urllib.parse import urljoin

from modeltranslation.translator import translator
from modeltranslation.utils import build_localized_fieldname
from rest_framework.fields import CharField
from wagtail.wagtailcore.models import Page

from django.core import signing
from django.shortcuts import redirect
from django.utils import translation

from core import constants, helpers


class BasePage(Page):

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        self.signer = signing.Signer()
        super().__init__(*args, **kwargs)

    def get_draft_token(self):
        return self.signer.sign(self.pk)

    def is_draft_token_valid(self, draft_token):
        try:
            value = self.signer.unsign(draft_token)
        except signing.BadSignature:
            return False
        else:
            return str(self.pk) == str(value)

    @property
    def published_url(self):
        app_url = dict(constants.APP_URLS)[self.view_app]
        url_parts = [
            app_url, self.view_path, str(self.pk) + '/', self.slug + '/'
        ]
        return functools.reduce(urljoin, url_parts)

    @property
    def draft_url(self):
        return self.published_url + '?draft_token=' + self.get_draft_token()

    def serve(self, request, *args, **kwargs):
        return redirect(self.published_url)


class TranslationsBrokenField:
    def __init__(self, field_name):
        self.field_name = field_name

    def __get__(self, instance, owner):
        language_code = translation.get_language()
        field_name = build_localized_fieldname(self.field_name, language_code)
        if instance:
            return getattr(instance, field_name)


class AddTranslationsBrokenFieldsMixin:
    """
    For each field specified as "translatable" via modeltranslation's
    translation.py, add a field to the model called `translated_<FIELD>`,
    which will return different content depending on the value returned by
    Django's `translation.get_language()`.

    e.g., `translated_title` will return `title_de` if the current language is
    German.

    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_translations_broker_fields()
        self.add_translations_broker_api_fields()

    @classmethod
    def get_translatable_fields(cls):
        return translator.get_options_for_model(cls).fields

    @classmethod
    def add_translations_broker_fields(cls):
        for field_name in cls.get_translatable_fields():
            setattr(
                cls,
                helpers.build_translated_fieldname(field_name),
                TranslationsBrokenField(field_name)
            )

    @classmethod
    def add_translations_broker_api_fields(cls):
        translated_fields = cls.get_translatable_fields()
        for api_field in cls.api_fields:
            if api_field.name in translated_fields:
                api_field.serializer = CharField(
                    source=helpers.build_translated_fieldname(api_field.name)
                )
