# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-12 07:58
from __future__ import unicode_literals

from django.db import migrations



def populate_slug(apps, schema_migrations):
    ExportReadinessApp = apps.get_model(
        'export_readiness', 'ExportReadinessApp'
    )
    FindASupplierApp = apps.get_model('find_a_supplier', 'FindASupplierApp')
    InvestApp = apps.get_model('invest', 'InvestApp')

    ExportReadinessApp.objects.all().update(slug='export-readiness-app')
    FindASupplierApp.objects.all().update(slug='find-a-supplier-app')
    InvestApp.objects.all().update(slug='invest-app')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0022_auto_20180906_1344'),
        ('export_readiness', '0019_auto_20180905_1350'),
        ('find_a_supplier', '0066_auto_20180830_0632'),
        ('invest', '0014_auto_20180904_1113'),
    ]

    operations = [
       migrations.RunPython(
           populate_slug,
           reverse_code=migrations.RunPython.noop,
           elidable=True
        )
    ]
