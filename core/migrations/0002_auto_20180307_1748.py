# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-03-07 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_create'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagehash',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
    ]
