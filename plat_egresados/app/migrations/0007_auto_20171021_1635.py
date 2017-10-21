# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-21 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20171021_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='is_admin'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_graduated',
            field=models.BooleanField(default=False, verbose_name='is_graduated'),
        ),
    ]
