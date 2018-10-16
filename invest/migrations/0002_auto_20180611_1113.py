# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 11:13
from __future__ import unicode_literals

import core.api_fields
import core.fields
import core.models
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailcore', '0040_page_draft_title'),
        ('invest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegionLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('heading', models.CharField(max_length=255)),
                ('heading_en_gb', models.CharField(max_length=255, null=True)),
                ('heading_de', models.CharField(max_length=255, null=True)),
                ('heading_ja', models.CharField(max_length=255, null=True)),
                ('heading_ru', models.CharField(max_length=255, null=True)),
                ('heading_zh_hans', models.CharField(max_length=255, null=True)),
                ('heading_fr', models.CharField(max_length=255, null=True)),
                ('heading_es', models.CharField(max_length=255, null=True)),
                ('heading_pt', models.CharField(max_length=255, null=True)),
                ('heading_pt_br', models.CharField(max_length=255, null=True)),
                ('heading_ar', models.CharField(max_length=255, null=True)),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=(core.models.ExclusivePageMixin, 'wagtailcore.page'),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content',
            field=core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_ar',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_de',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_en_gb',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_es',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_fr',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_ja',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_pt',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_pt_br',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_ru',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
        migrations.AlterField(
            model_name='infopage',
            name='content_zh_hans',
            field=core.api_fields.MarkdownField(null=True, validators=[core.validators.slug_hyperlinks]),
        ),
    ]
