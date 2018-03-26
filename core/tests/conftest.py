from itertools import product
import pytest

from modeltranslation.utils import build_localized_fieldname
from wagtail.wagtailcore.models import Page

from find_a_supplier.tests.factories import IndustryPageFactory


@pytest.fixture
def page():
    return IndustryPageFactory(
        parent=Page.objects.get(pk=1),
    )


@pytest.fixture
def untranslated_page():
    return IndustryPageFactory(
        parent=Page.objects.get(pk=1),
        title_en_gb='ENGLISH',
        sector_label_en_gb='label',
        lede_en_gb='lede',
        seo_description_en_gb='description',
        hero_text_en_gb='hero text',
        lede_column_one_en_gb='lede column one',
        lede_column_two_en_gb='lede column two',
        lede_column_three_en_gb='lede column three',
    )


@pytest.fixture
def translated_page(settings):
    page = IndustryPageFactory(
        parent=Page.objects.get(pk=1),
        title_en_gb='ENGLISH',
        title_de='GERMAN',
        title_ja='JAPANESE',
        title_zh_hans='SIMPLIFIED CHINESE',
        title_fr='FRENCH',
        title_es='SPANISH',
        title_pt='PORTUGUESE',
        title_pt_br='BRAZILIAN',
        title_ar='ARABIC',
        sector_label_en_gb='label',
        lede_en_gb='lede',
        seo_description_en_gb='description',
        hero_text_en_gb='hero text',
        lede_column_one_en_gb='lede column one',
        lede_column_two_en_gb='lede column two',
        lede_column_three_en_gb='lede column three',
    )
    field_names = page.get_required_translatable_fields()
    language_codes = settings.LANGUAGES
    for field_name, (language_code, _) in product(field_names, language_codes):
        localized_name = build_localized_fieldname(field_name, language_code)
        if not getattr(page, localized_name):
            setattr(page, localized_name, localized_name + '-value')
    page.save()
    return page


@pytest.fixture
def page_with_reversion(admin_user, translated_page):
    translated_page.title = 'published-title',
    translated_page.title_en_gb = 'published-title'
    translated_page.save()

    translated_page.title_en_gb = 'draft-title'
    translated_page.save_revision(
        user=admin_user,
        submitted_for_moderation=False,
    )
    return translated_page