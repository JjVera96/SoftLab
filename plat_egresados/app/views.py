# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from random import choice
from .forms import User_Form, Egre_Form, Admin_Form, Login_Form, Forget_Form, New_Password_Form
from .models import User, Egresado, Admin
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group
from .models import User

valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Create your views here.
def view_login(request):
	if request.user.is_anonymous():
		login_form = Login_Form(request.POST or None)
		msg = ""
		if login_form.is_valid():
			form_data = login_form.cleaned_data
			id_user = form_data.get("id_user")
			password = form_data.get("password")
			try:
				user = User.objects.get(username=id_user)
			except User.DoesNotExist:
				user = None
			if user is not None:
				if user.is_active == True:
					acceso = authenticate(username=id_user, password=password)
					if acceso is not None:
						user = User.objects.get(username=id_user)
						if user.last_login == None:
							return HttpResponseRedirect("/first_entrance/"+id_user)
						else:
							login(request, acceso)
							return HttpResponseRedirect("/")
					else:
						msg = "Contraseña Incorrecta"
				else:
					msg = "No estas activo"
			else:
				return HttpResponseRedirect("/no_registred")
		context = {
			"login_form" : login_form,
			"msg" : msg
		}
		return render(request, "login.html", context)
	else:
		return HttpResponseRedirect("/")


def first_entrance(request, id_user):
	try:
		user = User.objects.get(username=id_user)
	except User.DoesNotExist:
		user = None
	if user == None or user.is_active == False:
		return HttpResponseRedirect("/") 
	password_form = New_Password_Form(request.POST or None)
	context = {
		"password_form" : password_form,
		"msg" : ""
	}
	if password_form.is_valid():
		form_data = password_form.cleaned_data
		password = form_data.get("password")
		again = form_data.get("again")
		if password == again:
			user.password = make_password(password, salt=None, hasher='default')
			user.save()
			acceso = authenticate(username=id_user, password=again)
			login(request, acceso)
			return HttpResponseRedirect("/")
		else:
			msg = "Las contraseñas no coinciden"
			context = {
				"password_form" : password_form,
				"msg" : msg,
			}
	return render(request, "first_entrance.html", context)

def view_logout(request):
	logout(request)
	return render(request, "logout.html", {})

def forget_account(request):
	forget_form = Forget_Form(request.POST or None)
	context = {
		"msg" : "",
		"forget_form" : forget_form
	}

	if forget_form.is_valid():
		password = ""
		form_data = forget_form.cleaned_data
		email = form_data.get("email")
		try:
			user = User.objects.get(email=email)
		except User.DoesNotExist:
			user = None
		if user is not None:
			if user.is_active == True:
				send_password(1, user)
				msg = "Te hemos enviado un correo con tu nueva contraseña de ingreso. Revisa tu bandeja de entrada"
			else:
				msg = "Aun no has sido activado. Espera a que activemos tu cuenta. Paciencia por favor"
		else:
			msg = "No hay usuario con este email. Por favor registrate"
		context = {
			"msg" : msg
		}
			
	return render(request, "forget_account.html", context)

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
	print "Hola"
	if eg_form.is_valid() and user_form.is_valid():	
		form_data = user_form.cleaned_data
		username = form_data.get("username")
		email = form_data.get("email")
		first_name = form_data.get("first_name")
		second_name = form_data.get("second_name")
		last_name = form_data.get("last_name")
		second_last_name = form_data.get("second_last_name")
		gender = form_data.get("gender")
		password = ""
		user = User.objects.create(username=username, password=password, email=email, first_name=first_name, second_name=second_name, last_name=last_name, second_last_name=second_last_name, gender=gender, is_graduated=True)
		form_data = eg_form.cleaned_data
		country = form_data.get("country") 
		career = form_data.get("career")
		graduation = form_data.get("graduation")
		birthdate = form_data.get("birthdate")
		egresado = Egresado.objects.create(user=user, country=country, career=career, graduation=graduation, birthdate=birthdate)
		#grupo_egresado = Group.objects.get(name='Egresados')
		#user.groups.add(grupo_egresado)

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
		form_data = user_form.cleaned_data
		username = form_data.get("username")
		email = form_data.get("email")
		first_name = form_data.get("first_name")
		second_name = form_data.get("second_name")
		last_name = form_data.get("last_name")
		second_last_name = form_data.get("second_last_name")
		gender = form_data.get("gender")
		password = ""
		user = User.objects.create(username=username, password=password, email=email, first_name=first_name, second_name=second_name, last_name=last_name, second_last_name=second_last_name, gender=gender, is_admin=True)
		form_data = ad_form.cleaned_data
		address = form_data.get("address") 
		city= form_data.get("city")
		admin = Admin.objects.create(user=user, address=address, city=city)
		#grupo_administradores = Group.objects.get(name='Administradores')
		#user.groups.add(grupo_administradores)

		context = {
			"InfoCorreo" : "Te enviaremos un correo a {} con tu contraseña de ingreso cuando seas activado".format(email),
			"InfoGracias" : "Gracias {} {}, UTP Egresados ☺".format(first_name, last_name),
		}

	return render(request, "register_admin.html", context)

def index(request):
	if request.user.is_anonymous():
		return render(request, "base.html")
	elif request.user.is_graduated:
		return HttpResponseRedirect('/profile_graduated')
	elif request.user.is_admin:
		return HttpResponseRedirect('/profile_admin')
	else:
		return HttpResponseRedirect('/profile_root')

def index_graduated(request):
	return render(request, "index_graduated.html", {})

def index_admin(request):
	return render(request, "index_admin.html", {})

def index_root(request):
	return render(request, "index_root.html", {})

def active_graduated(request):
	users = User.objects.all().filter(is_active=False, is_graduated=True)
	mode = True
	if not len(users):
		msg = "No hay Egresados para activar"
		mode = False
	else:
		msg = ""
	context = {
		"type": "Egresados",
		"msg": msg,
		"users" : users,
		"mode" : mode,
	}
	return render(request, "activate_users.html", context)

def active_admin(request):
	users = User.objects.all().filter(is_active=False, is_admin=True)
	print len(users)
	mode = True
	if not len(users):
		msg = "No hay Administradores para activar"
		mode = False
	else:
		msg = ""
	context = {
		"type": "Administradores",
		"msg": msg,
		"users" : users,
		"mode" : mode,
	}
	return render(request, "activate_users.html", context)

def activate_user(request, id_user):
	if not request.user.is_anonymous:
		if request.user.is_admin or request.user.is_staff:
			user = User.objects.get(username=id_user)
			user.is_active = True
			user.save()
			send_password(0, user)
			if request.user.is_admin:
				return HttpResponseRedirect('/activate_graduated')
			elif request.user.is_staff:
				return HttpResponseRedirect('/activate_admin')
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


def delete_user(request, id_user):
	if request.user.is_admin or request.user.is_staff:
		user = User.objects.get(username=id_user)
		user.delete()
		if request.user.is_admin:
			return HttpResponseRedirect('/activate_graduated')
		elif request.user.is_staff:
			return HttpResponseRedirect('/activate_admin')

###############################################################################
#Functions
def send_password(mode, user):
	password = ""
	password = password.join([choice(valores) for i in range(8)])
	if mode == 0:
		title = 'Registro Plataforma Egresados UTP'
		body = "Genial! Registro Completado\nBienvenido {} {}\nTu contraseña de ingreso es {}".format(user.first_name, user.last_name, password)
	else:
		title = "Recuperacion Contraseña Plataforma Egresados UTP"
		body = "Hola {} {}\nTu nueva contraseña de ingreso es {}".format(user.first_name, user.last_name, password)
	password = make_password(password, salt=None, hasher='default')
	user.password = password
	user.save()
	send_mail(
		title,
		body,
	 	settings.EMAIL_HOST_USER,
		[user.email],
		fail_silently=False,
	)
