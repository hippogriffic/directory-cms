# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-04-04 14:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('find_a_supplier', '0028_auto_20180404_1345'),
    ]

    operations = [
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_ar',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_de',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_en_gb',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_es',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_fr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_ja',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_pt',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_pt_br',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_ru',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='industrypage',
            name='contact_success_back_link_text_zh_hans',
            field=models.CharField(max_length=100, null=True),
        ),
    ]