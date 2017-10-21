# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-20 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_admin_egresado'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='admin',
            options={'verbose_name': 'Administrador', 'verbose_name_plural': 'Administradores'},
        ),
        migrations.AlterModelOptions(
            name='egresado',
            options={'verbose_name': 'Egresado', 'verbose_name_plural': 'Egresados'},
        ),
        migrations.RemoveField(
            model_name='user',
            name='id',
        ),
        migrations.AddField(
            model_name='egresado',
            name='country',
            field=models.CharField(blank=True, max_length=30, verbose_name='country'),
        ),
        migrations.AlterField(
            model_name='user',
            name='identification',
            field=models.CharField(max_length=30, primary_key=True, serialize=False, unique=True, verbose_name='identification'),
        ),
    ]
