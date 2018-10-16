# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-25 11:46
from __future__ import unicode_literals

import core.api_fields
import core.fields
import core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0021_image_file_hash'),
        ('export_readiness', '0019_auto_20180905_1350'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleListingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('landing_page_title', models.CharField(max_length=255)),
                ('hero_teaser', models.CharField(blank=True, max_length=255, null=True)),
                ('list_teaser', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ArticlePage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('article_title', models.CharField(max_length=255)),
                ('article_teaser', models.CharField(max_length=255)),
                ('article_body_text', core.api_fields.MarkdownField(validators=[core.validators.slug_hyperlinks])),
                ('related_article_one_url', models.CharField(help_text='Paste the article path here (eg /foo/bar/)', max_length=255)),
                ('related_article_one_title', models.CharField(help_text='Paste the title of the article here', max_length=255)),
                ('related_article_one_teaser', models.CharField(help_text='Paste the article description here (max 255 characters)', max_length=255)),
                ('related_article_two_url', models.CharField(help_text='Paste the article path here (eg /foo/bar/)', max_length=255)),
                ('related_article_two_title', models.CharField(help_text='Paste the title of the article here', max_length=255)),
                ('related_article_two_teaser', models.CharField(help_text='Paste the article description here (max 255 characters)', max_length=255)),
                ('related_article_three_url', models.CharField(help_text='Paste the article path here (eg /foo/bar/)', max_length=255)),
                ('related_article_three_title', models.CharField(help_text='Paste the title of the article here', max_length=255)),
                ('related_article_three_teaser', models.CharField(help_text='Paste the article description here (max 255 characters)', max_length=255)),
                ('article_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='TopicLandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('service_name', models.CharField(choices=[('FIND_A_SUPPLIER', 'Find a Supplier'), ('EXPORT_READINESS', 'Export Readiness'), ('INVEST', 'Invest')], db_index=True, max_length=100, null=True)),
                ('landing_page_title', models.CharField(max_length=255)),
                ('hero_teaser', models.CharField(blank=True, max_length=255, null=True)),
                ('hero_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
