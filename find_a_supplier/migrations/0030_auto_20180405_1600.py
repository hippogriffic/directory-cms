# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-05 16:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('find_a_supplier', '0029_auto_20180404_1420'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndustryContactPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('breadcrumb_label', models.CharField(max_length=500)),
                ('breadcrumb_label_en_gb', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_de', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_ja', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_ru', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_zh_hans', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_fr', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_es', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_pt', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_pt_br', models.CharField(max_length=500, null=True)),
                ('breadcrumb_label_ar', models.CharField(max_length=500, null=True)),
                ('introduction_text', wagtail.wagtailcore.fields.RichTextField()),
                ('introduction_text_en_gb', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_de', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_ja', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_ru', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_zh_hans', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_fr', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_es', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_pt', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_pt_br', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('introduction_text_ar', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('submit_button_text', models.CharField(max_length=100)),
                ('submit_button_text_en_gb', models.CharField(max_length=100, null=True)),
                ('submit_button_text_de', models.CharField(max_length=100, null=True)),
                ('submit_button_text_ja', models.CharField(max_length=100, null=True)),
                ('submit_button_text_ru', models.CharField(max_length=100, null=True)),
                ('submit_button_text_zh_hans', models.CharField(max_length=100, null=True)),
                ('submit_button_text_fr', models.CharField(max_length=100, null=True)),
                ('submit_button_text_es', models.CharField(max_length=100, null=True)),
                ('submit_button_text_pt', models.CharField(max_length=100, null=True)),
                ('submit_button_text_pt_br', models.CharField(max_length=100, null=True)),
                ('submit_button_text_ar', models.CharField(max_length=100, null=True)),
                ('success_message_text', wagtail.wagtailcore.fields.RichTextField()),
                ('success_message_text_en_gb', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_de', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_ja', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_ru', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_zh_hans', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_fr', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_es', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_pt', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_pt_br', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_message_text_ar', wagtail.wagtailcore.fields.RichTextField(null=True)),
                ('success_back_link_text', models.CharField(max_length=100)),
                ('success_back_link_text_en_gb', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_de', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_ja', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_ru', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_zh_hans', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_fr', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_es', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_pt', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_pt_br', models.CharField(max_length=100, null=True)),
                ('success_back_link_text_ar', models.CharField(max_length=100, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_ar',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_de',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_en_gb',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_es',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_fr',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_ja',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_pt',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_pt_br',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_ru',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_breadcrumb_label_zh_hans',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_ar',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_de',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_es',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_fr',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_ja',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_pt',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_pt_br',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_ru',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_button_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_ar',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_de',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_es',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_fr',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_ja',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_pt',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_pt_br',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_ru',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_introduction_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_ar',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_de',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_es',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_fr',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_ja',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_pt',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_pt_br',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_ru',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_back_link_text_zh_hans',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_ar',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_de',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_en_gb',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_es',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_fr',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_ja',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_pt',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_pt_br',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_ru',
        ),
        migrations.RemoveField(
            model_name='industrypage',
            name='contact_success_message_text_zh_hans',
        ),
    ]
