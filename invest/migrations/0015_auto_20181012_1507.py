# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-12 15:07
from __future__ import unicode_literals

import core.fields
import core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invest', '0014_auto_20180904_1113_squashed_0026_auto_20181002_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='highpotentialopportunitydetailpage',
            name='other_opportunities_title',
            field=models.CharField(max_length=300, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='setupguidepage',
            name='subsection_content_one',
            field=core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='setupguidepage',
            name='subsection_content_two',
            field=core.fields.MarkdownField(validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='setupguidepage',
            name='subsection_title_one',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='setupguidepage',
            name='subsection_title_two',
            field=models.CharField(max_length=255),
        ),
    ]
