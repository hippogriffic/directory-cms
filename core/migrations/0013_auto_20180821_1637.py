# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-08-21 16:26
from __future__ import unicode_literals

from django.db import migrations

from core.models import BasePage


def populate_historic_slug_service_name(apps, schema_editor):
    for sub_class in BasePage.__subclasses__():
        try:
            historic_model = apps.get_model(
                sub_class._meta.app_label, sub_class._meta.object_name
            )
        except LookupError:
            pass
        else:
            for page in historic_model.objects.all():
                page.historicslug_set.update(
                    service_name=page.service_name
                )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20180821_1634'),
        ('invest', '0008_auto_20180817_1630'),
        ('find_a_supplier', '0063_auto_20180821_0810'),
        ('export_readiness', '0012_auto_20180821_0810'),
    ]

    operations = [
        migrations.RunPython(
           populate_historic_slug_service_name,
           reverse_code=migrations.RunPython.noop
        )
    ]

