# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-02 15:34
from __future__ import unicode_literals

import core.api_fields
import core.fields
import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0025_auto_20180920_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highpotentialopportunitydetailpage',
            name='competitive_advantages_title',
            field=models.CharField(max_length=300, verbose_name='Body text'),
        ),
        migrations.AlterField(
            model_name='highpotentialopportunitydetailpage',
            name='contact_proposition',
            field=core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks], verbose_name='Body text'),
        ),
    ]
