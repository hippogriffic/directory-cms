from modeltranslation.translator import TranslationOptions
from modeltranslation.decorators import register

from django.conf import settings

from find_a_supplier import models


@register(models.IndustryPage)
class IndustryPageTranslationOptions(TranslationOptions):
    fields = (
        'hero_text',
        'lede',
        'lede_column_one',
        'lede_column_two',
        'lede_column_three',
        'sector_label',
        'seo_description',
        'lede_column_one_icon',
        'lede_column_two_icon',
        'lede_column_three_icon',
    )
    required_languages = (settings.LANGUAGE_CODE,)


@register(models.IndustryArticlePage)
class IndustryArticlePageTranslationOptions(TranslationOptions):
    fields = (
        'author_name',
        'job_title',
        'date',
        'body',
    )
    required_languages = (settings.LANGUAGE_CODE,)


@register(models.IndustryLandingPage)
class IndustryLandingPageTranslationOptions(TranslationOptions):
    fields = (
        'proposition_text',
        'call_to_action_text',
        'breadcrumbs_label',
        'seo_description',
    )
    required_languages = (settings.LANGUAGE_CODE,)


@register(models.LandingPage)
class LandingPageTranslationOptions(TranslationOptions):
    fields = (
        'hero_text',
        'search_field_placeholder',
        'search_button_text',
        'proposition_text',
        'call_to_action_text',
        'industries_list_text',
        'industries_list_call_to_action_text',
        'services_list_text',
        'services_column_one',
        'services_column_two',
        'services_column_three',
        'services_column_four',
        'services_column_one_icon',
        'services_column_two_icon',
        'services_column_three_icon',
        'services_column_four_icon',
        'seo_description',
    )
    required_languages = (settings.LANGUAGE_CODE,)