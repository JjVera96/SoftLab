# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from .managers import UserManager

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):
	identification = models.CharField(_('identification'), primary_key=True, max_length=30, unique=True)
	email = models.EmailField(_('email address'))
	first_name = models.CharField(_('first name'), max_length=30, blank=True)
	second_name = models.CharField(_('second name'), max_length=30, blank=True)
	last_name = models.CharField(_('first last name'), max_length=30, blank=True)
	second_last_name = models.CharField(_('second last name'), max_length=30, blank=True)
	gender = models.CharField(_('gender'), max_length=30, blank=True)
	date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
	is_staff = models.BooleanField(_('is_staff'), default=False)	
	is_active = models.BooleanField(_('is_active'), default=False)
	
	objects = UserManager()

	USERNAME_FIELD = 'identification'
	REQUIRED_FIELDS = []

	class Meta:
		verbose_name = _('user')
		verbose_name_plural = _('users')

	def get_full_name(self):
		full_name = '%s %s' % (self.first_name, self.last_name)
		return full_name.strip()

	def get_short_name(self):
		return self.first_name


class Egresado(models.Model):
	class Meta:
		verbose_name = _('Egresado')
		verbose_name_plural = _('Egresados')
	
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	country = models.CharField(_('country'), max_length=30, blank=True)	
	career = models.CharField(_('career'), max_length=30, blank=True)
	graduation = models.DateTimeField(_('graduation year'))

	def __unicode__(self):
		return unicode(self.user)

class Admin(models.Model):
	class Meta:
		verbose_name = _('Administrador')
		verbose_name_plural = _('Administradores')

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	def __unicode__(self):
		return unicode(self.user)