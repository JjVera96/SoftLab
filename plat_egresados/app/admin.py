# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Egresado, Admin, Categoria, User, Noticia, Mensaje

class Admin_Admin(admin.ModelAdmin):
	list_display = ["usuario", "nombre" , "domicilio", "estado"]

	class Meta:
		model = Admin

	def estado(self, obj):
		return obj.user.is_active

	def nombre(self, obj):
		return obj.user.get_full_name()

	def domicilio(self, obj):
		return obj.address

	def usuario(self, obj):
		return obj.user

admin.site.register(Egresado)
admin.site.register(Admin, Admin_Admin)
admin.site.register(Categoria)
admin.site.register(User)
admin.site.register(Noticia)
admin.site.register(Mensaje)
