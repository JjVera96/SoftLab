# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171021_1635'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='identification',
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=None, max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='username'),
            preserve_default=False,
        ),
    ]
