# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
	username = models.CharField(_('username'), primary_key=True, max_length=50, unique=True)
	email = models.EmailField(_('email address'), unique=True)
	first_name = models.CharField(_('Primer Nombre'), max_length=50)
	second_name = models.CharField(_('Segundo Nombre'), max_length=50, blank=True)
	last_name = models.CharField(_('Primer Apellido'), max_length=50)
	second_last_name = models.CharField(_('Segundo Apellido'), max_length=50)
	gender = models.CharField(_('Genero'), max_length=50)
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	is_staff = models.BooleanField(_('is_staff'), default=False)	
	is_active = models.BooleanField(_('is_active'), default=False)
	is_graduated = models.BooleanField(_('is_graduated'), default=False)
	is_admin = models.BooleanField(_('is_admin'), default=False)
	
	objects = UserManager()

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ["email"]

	class Meta:
		verbose_name = _('Usuario')
		verbose_name_plural = _('Usuarios')

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name


class Egresado(models.Model):
	class Meta:
		verbose_name = _('Egresado')
		verbose_name_plural = _('Egresados')
	
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	country = models.CharField(_('Pais'), max_length=50)	
	career = models.CharField(_('Carrera'), max_length=50)
	graduation = models.DateField(_('Año de Graduación'))
	birthdate = models.DateField(_('Fecha de Cumpleaños'))
	friends = models.ManyToManyField("Egresado")
	interests = models.ManyToManyField("Categoria")
	message = models.ManyToManyField("Mensaje")

	def __unicode__(self):
		return unicode(self.user)

class Admin(models.Model):
	class Meta:
		verbose_name = _('Administrador')
		verbose_name_plural = _('Administradores')

	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	address = models.CharField(_('Dirección'), max_length=50)
	city = models.CharField(_('Ciudad'), max_length=50)

	def __unicode__(self):
		return unicode(self.user)

class Categoria(models.Model):
	class Meta:
		verbose_name = _('Categoria')
		verbose_name_plural = _('Categorias')

	name = models.CharField(_('name'), max_length=50, unique=True)

	def __unicode__(self):
		return unicode(self.name)

class Noticia(models.Model):
	class Meta:
		verbose_name = _('Noticia')
		verbose_name_plural = _('Noticias')

	title = models.CharField(_('Titulo'), max_length=50)
	body = models.CharField(_('Cuerpo'), max_length=2000)
	media = models.ImageField(_('Imagen'), upload_to='images/')
	category = models.CharField(_('Categoria'), max_length=50)

class Mensaje(models.Model):
	class Meta:
		verbose_name = _('Mensaje')
		verbose_name_plural = _('Mensajes')

	receiver = models.CharField(_('Para'), max_length=50)
	title = models.CharField(_('Titulo'), max_length=50)
	body = models.CharField(_('Cuerpo'), max_length=500)
	date = models.DateField(_('Fecha de Envio'), auto_now_add=True)