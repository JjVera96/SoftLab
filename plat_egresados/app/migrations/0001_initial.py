# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 22:07
from __future__ import unicode_literals

import app.managers
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False, unique=True, verbose_name='username')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=50, verbose_name='Primer Nombre')),
                ('second_name', models.CharField(blank=True, max_length=50, verbose_name='Segundo Nombre')),
                ('last_name', models.CharField(max_length=50, verbose_name='Primer Apellido')),
                ('second_last_name', models.CharField(max_length=50, verbose_name='Segundo Apellido')),
                ('gender', models.CharField(max_length=50, verbose_name='Genero')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False, verbose_name='is_staff')),
                ('is_active', models.BooleanField(default=False, verbose_name='is_active')),
                ('is_graduated', models.BooleanField(default=False, verbose_name='is_graduated')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is_admin')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', app.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receiver', models.CharField(max_length=50, verbose_name='Para')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('body', models.CharField(max_length=500, verbose_name='Cuerpo')),
                ('date', models.DateField(blank=True, verbose_name='Fecha de Envio')),
            ],
            options={
                'verbose_name': 'Mensaje',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Titulo')),
                ('body', models.CharField(max_length=2000, verbose_name='Cuerpo')),
                ('media', models.ImageField(upload_to='images/', verbose_name='Imagen')),
                ('category', models.CharField(max_length=50, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Noticia',
                'verbose_name_plural': 'Noticias',
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('address', models.CharField(max_length=50, verbose_name='Direcci\xf3n')),
                ('city', models.CharField(max_length=50, verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Administrador',
                'verbose_name_plural': 'Administradores',
            },
        ),
        migrations.CreateModel(
            name='Egresado',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('country', models.CharField(max_length=50, verbose_name='Pais')),
                ('career', models.CharField(max_length=50, verbose_name='Carrera')),
                ('graduation', models.DateField(verbose_name='A\xf1o de Graduaci\xf3n')),
                ('birthdate', models.DateField(verbose_name='Fecha de Cumplea\xf1os')),
                ('friends', models.ManyToManyField(to='app.Egresado')),
                ('interests', models.ManyToManyField(to='app.Categoria')),
                ('message', models.ManyToManyField(to='app.Mensaje')),
            ],
            options={
                'verbose_name': 'Egresado',
                'verbose_name_plural': 'Egresados',
            },
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
