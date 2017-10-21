# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import Egresado, Admin

class Admin_Admin(admin.ModelAdmin):
	list_display = ["user", "address", "get_active"]

	class Meta:
		model = Admin

	def get_active(self, obj):
		return obj.user.is_active

admin.site.register(Egresado)
admin.site.register(Admin, Admin_Admin)