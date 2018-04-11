from wagtail.api import APIField

from core.serializers import APIQuerysetSerializer
from find_a_supplier import serializers


class APIIndustriesListField(APIField):
    def __init__(self, name, queryset):
        # see explanation of the `fields_config` syntax here:
        # https://github.com/wagtail/wagtail/blob/
        # db6d36845f3f2c5d7009a22421c2efab9968aa24/wagtail/api/v2/utils.py#L68
        fields_config = [
            ('meta', False, None),
            ('hero_image', False, None),
            ('hero_text', False, None),
            ('breadcrumbs_label', None, None)
        ]
        serializer = APIQuerysetSerializer(
            name,
            fields_config=fields_config,
            queryset=queryset,
        )
        super().__init__(name=name, serializer=serializer)


class APIArticleSummariesField(APIField):
    def __init__(self, name):
        serializer = serializers.APIArticleSummariesSerializer(name)
        super().__init__(name=name, serializer=serializer)
