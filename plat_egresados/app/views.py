# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from random import choice
from .forms import User_Form, Egre_Form, Admin_Form, Login_Form
from .models import User, Egresado, Admin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group
from .models import User

valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Create your views here.
def view_login(request):
	login_form = Login_Form(request.POST or None)
	context = {
		"login_form" : login_form
	}

	if login_form.is_valid():
		form_data = login_form.cleaned_data
		id_user = form_data.get("id_user")
		password = form_data.get("password")
		acceso = authenticate(username=id_user, password=password)
		print acceso
		if acceso is not None:
			login(request, acceso)
			return HttpResponseRedirect("/")
		else:
			return HttpResponseRedirect("/no_registred")

	return render(request, "login.html", context)

def view_logout(request):
	logout(request)
	return render(request, "logout.html", {})

def no_registred(request):
	context = {}
	return render(request, "no_registred.html", context)

def register(request):
	context = {}
	return render(request, "register.html", context)

def register_graduated(request):
	user_form = User_Form(request.POST or None)
	eg_form = Egre_Form(request.POST or None)
	context = {
		"user_form" : user_form,
		"eg_form" : eg_form,
	}

	if eg_form.is_valid() and user_form.is_valid():
		password = ""
		form_data = user_form.cleaned_data
		username = form_data.get("username")
		email = form_data.get("email")
		first_name = form_data.get("first_name")
		second_name = form_data.get("second_name")
		last_name = form_data.get("last_name")
		second_last_name = form_data.get("second_last_name")
		gender = form_data.get("gender")
		password = password.join([choice(valores) for i in range(8)])
		print password
		password = make_password(password, salt=None, hasher='default')
		user = User.objects.create(username=username, password=password, email=email, first_name=first_name, second_name=second_name, last_name=last_name, second_last_name=second_last_name, gender=gender, is_graduated=True)
		form_data = eg_form.cleaned_data
		country = form_data.get("country") 
		career = form_data.get("career")
		graduation = form_data.get("graduation")
		egresado = Egresado.objects.create(user=user, country=country, career=career, graduation=graduation)
		grupo_egresado = Group.objects.get(name='Egresados')
		user.groups.add(grupo_egresado)

		context = {
			"InfoCorreo" : "Te enviaremos un correo a {} con tu contraseña de ingreso cuando seas activado".format(email),
			"InfoGracias" : "Gracias {} {}, UTP Egresados ☺".format(first_name, last_name),
		}

	return render(request, "register_graduated.html", context)

def register_admin(request):
	user_form = User_Form(request.POST or None)
	ad_form = Admin_Form(request.POST or None)
	context = {
		"user_form" : user_form,
		"ad_form" : ad_form,
	}

	if ad_form.is_valid() and user_form.is_valid():	
		password = ""
		form_data = user_form.cleaned_data
		username = form_data.get("username")
		email = form_data.get("email")
		first_name = form_data.get("first_name")
		second_name = form_data.get("second_name")
		last_name = form_data.get("last_name")
		second_last_name = form_data.get("second_last_name")
		gender = form_data.get("gender")
		password = password.join([choice(valores) for i in range(8)])
		password = make_password(password, salt=None, hasher='default')
		user = User.objects.create(username=username, password=password, email=email, first_name=first_name, second_name=second_name, last_name=last_name, second_last_name=second_last_name, gender=gender, is_admin=True)
		form_data = ad_form.cleaned_data
		address = form_data.get("address") 
		admin = Admin.objects.create(user=user, address=address)
		grupo_administradores = Group.objects.get(name='Administradores')
		user.groups.add(grupo_administradores)

		context = {
			"InfoCorreo" : "Te enviaremos un correo a {} con tu contraseña de ingreso cuando seas activado".format(email),
			"InfoGracias" : "Gracias {} {}, UTP Egresados ☺".format(first_name, last_name),
		}

	return render(request, "register_admin.html", context)

def index(request):
	if request.user.is_anonymous():
		return HttpResponseRedirect('/login')
	elif request.user.groups.filter(name='Egresados').exists():
		print "aqui"
		return HttpResponseRedirect('/profile_graduated')
	elif request.user.groups.filter(name='Administradores').exists():
		print "por aqui"
		return HttpResponseRedirect('/profile_admin')
	else:
		return HttpResponseRedirect('/admin')

def index_graduated(request):
	return render(request, "index_graduated.html", {})

def index_admin(request):
	return render(request, "index_admin.html", {})

def active_graduated(request):
	users = User.objects.all().filter(is_active=False, is_graduated=True)
	for user in users:
		print user
	context = {
		"users" : users
	}
	return render(request, "activate_graduated.html", context)


def send_email(email, first_name, last_name, password):
	send_mail(
			'Registro Plataforma Egresados UTP',
	   		"Genial! Registro Completado\nBienvenido {} {}\nTu contraseña de ingreso es {}".format(first_name, last_name, password),
	 		settings.EMAIL_HOST_USER,
			[email],
			fail_silently=False,
		)