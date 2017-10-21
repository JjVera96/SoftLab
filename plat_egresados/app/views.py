# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from random import choice
from .forms import User_Form, Egre_Form, Login_Form
from .models import User, Egresado
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
	login_form = Login_Form(request.POST or None)
	context = {
		"login_form" : login_form
	}

	if login_form.is_valid():
		form_data = login_form.cleaned_data
		id_user = form_data.get("id_user")
		password = form_data.get("password")
		print id_user, password
		acceso = authenticate(username=id_user, password=password)
		print acceso
		if acceso is not None:
			login(request, acceso)
			return HttpResponseRedirect("/registrarAdmon")
		else:
			return HttpResponseRedirect("/registrarEgresado")

	return render(request, "index.html", context)

def register(request):
	context = {}
	return render(request, "registrar.html", context)

def register_eg(request):
	user_form = User_Form(request.POST or None)
	eg_form = Egre_Form(request.POST or None)
	context = {
		"user_form" : user_form,
		"eg_form" : eg_form,
	}

	if eg_form.is_valid() and user_form.is_valid():
		valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"
		passw = ""
		form_data = user_form.cleaned_data
		identification = form_data.get("identification")
		email = form_data.get("email")
		first_name = form_data.get("first_name")
		second_name = form_data.get("second_name")
		last_name = form_data.get("last_name")
		second_last_name = form_data.get("second_last_name")
		gender = form_data.get("gender")
		passw = passw.join([choice(valores) for i in range(8)])
		password = make_password(passw, salt=None, hasher='default')
		user = User.objects.create(identification=identification, password=password, email=email, first_name=first_name, second_name=second_name, last_name=last_name, second_last_name=second_last_name, gender=gender)
		form_data = eg_form.cleaned_data
		country = form_data.get("country") 
		career = form_data.get("career")
		graduation = form_data.get("graduation")
		egresado = Egresado.objects.create(user=user, country=country, career=career, graduation=graduation)
		print "User"
		print identification, password, email, first_name, second_name, last_name, second_last_name, gender
		print "Egresado"
		print user, country, career, graduation

		send_mail(
			'Registro Plataforma Egresados UTP',
	   		"Genial! Registro Completado\nBienvenido {} {}\nTu contraseña de ingreso es {}".format(first_name, last_name, passw),
	 		settings.EMAIL_HOST_USER,
    		[email],
    		fail_silently=False,
		)

		context = {
			"InfoCorreo" : "Te enviaremos un correo a {} con tu contraseña de ingreso cuando seas activado".format(email),
			"InfoGracias" : "Gracias {} {}, UTP Egresados ☺".format(first_name, last_name),
		}

	return render(request, "regEgresado.html", context)

def register_admin(request):
	context = {}
	return render(request, "regAdmin.html", context)
