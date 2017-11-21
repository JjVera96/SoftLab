# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from random import choice
from .forms import User_Form, Egre_Form, Admin_Form, Login_Form, Forget_Form, New_Password_Form
from .forms import Notice_Form, Category_Form
from .models import User, Egresado, Admin, Noticia, Categoria
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
		form_data = eg_form.cleaned_data
		country = form_data.get("country") 
		career = form_data.get("career")
		graduation = form_data.get("graduation")
		birthdate = form_data.get("birthdate")
		user = User.objects.create(username=username, password=password, email=email, first_name=first_name, second_name=second_name, last_name=last_name, second_last_name=second_last_name, gender=gender, is_graduated=True)
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
		form_data = ad_form.cleaned_data
		address = form_data.get("address") 
		city= form_data.get("city")
		user = User.objects.create(username=username, password=password, email=email, first_name=first_name, second_name=second_name, last_name=last_name, second_last_name=second_last_name, gender=gender, is_admin=True)
		admin = Admin.objects.create(user=user, address=address, city=city)
		context = {
			"InfoCorreo" : "Te enviaremos un correo a {} con tu contraseña de ingreso cuando seas activado".format(email),
			"InfoGracias" : "Gracias {} {}, UTP Egresados ☺".format(first_name, last_name),
		}

	return render(request, "register_admin.html", context)

def index(request):
	if request.user.is_anonymous():
		return render(request, "base.html")
	else:
		return render(request, "index.html")

def profile_graduated(request):
	eg = Egresado.objects.get(user=request.user.username)
	context = {
		'eg':eg,
	}
	return render(request, "profile_graduated.html", context)

def profile_admin(request):
	return render(request, "profile_admin.html", {})

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

def list_graduated(request):
	users = User.objects.all().filter(is_active=True, is_graduated=True)
	mode = True
	if not len(users):
		msg = "No hay Egresados para listar"
		mode = False
	else:
		msg = ""
	context = {
		"type": "Egresados",
		"msg": msg,
		"users" : users,
		"mode" : mode,
	}
	return render(request, "list_users.html", context)

def list_admin(request):
	users = User.objects.all().filter(is_admin=True)
	mode = True
	if not len(users):
		msg = "No hay Administradores para listar"
		mode = False
	else:
		msg = ""
	context = {
		"type": "Administradores",
		"msg": msg,
		"users" : users,
		"mode" : mode,
	}
	return render(request, "list_users.html", context)

def create_notice(request):
	notice_form = Notice_Form(request.POST or None, request.FILES or None)
	categories = Categoria.objects.all()
	context = {
		"notice_form" : notice_form,
		"categories" : categories,
	}

	if notice_form.is_valid():
		form_data = notice_form.cleaned_data
		title = form_data.get("title")
		body = form_data.get("body")
		media = form_data.get("media")
		category = form_data.get("category")
		notice = Noticia.objects.create(title=title, body=body, media=media, category=category)
	return render(request, "notice.html", context)

def create_category(request):
	category_form = Category_Form(request.POST or None)
	categories = Categoria.objects.all()
	context = {
		"category_form" : category_form,
		"categories" : categories,
	}

	if category_form.is_valid():
		form_data = category_form.cleaned_data
		name = form_data.get("name")
		category = Categoria.objects.create(name=name)
	return render(request, "category.html", context)

def desactivate_user(request, id_user):
	if not request.user.is_anonymous:
		if request.user.is_admin or request.user.is_staff:
			user = User.objects.get(username=id_user)
			user.is_active = False
			user.save()
			if request.user.is_admin:
				return HttpResponseRedirect('/list_graduated')
			elif request.user.is_staff:
				return HttpResponseRedirect('/list_admin')
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def delete_category(request, category):
	if not request.user.is_anonymous or not request.user.is_staff:
		categoria = Categoria.objects.get(id=category)
		categoria.delete()
		return HttpResponseRedirect('/create_category')
	else:
		return HttpResponseRedirect('/')

def edit_graduated(request, id_user):
	if not request.user.is_anonymous:
		if request.user.username == id_user or request.user.is_admin:
			user = User.objects.get(username=id_user)
			eg = Egresado.objects.get(user=id_user)
			user_form = User_Form(request.POST or None, instance=user)
			eg_form = Egre_Form(request.POST or None, instance=eg)
			if user_form.is_valid() and ad_form.is_valid():
				form_data = user_form.cleaned_data
				user.username = form_data.get("username")
				user.email = form_data.get("email")
				user.first_name = form_data.get("first_name")
				user.second_name = form_data.get("second_name")
				user.last_name = form_data.get("last_name")
				user.second_last_name = form_data.get("second_last_name")
				user.gender = form_data.get("gender")
				form_data = eg_form.cleaned_data
				eg.country = form_data.get("country")
				eg.career = form_data.get("career")
				eg.graduation = form_data.get("graduation")
				eg.birthdate = form_data.get("birthdate")
				user.save()
				eg.save()
			else:
				user = User.objects.get(username=id_user)
				eg = Egresado.objects.get(user=id_user)
			context = {
				"user_form": user_form,
				"eg_form": eg_form,
				"username": user.username,
				"email": user.email,
				"first_name": user.first_name,
				"second_name": user.second_name,
				"last_name": user.last_name,
				"second_last_name": user.second_last_name,
				"gender": user.gender,
				"country": eg.country,
				"career": eg.career,
				"graduation": eg.graduation,
				"birthdate": eg.birthdate,
			}
			print eg.graduation
			print eg.birthdate
			return render(request, "update_graduated.html", context)
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')

def edit_admin(request, id_user):
	if not request.user.is_anonymous:
		if request.user.username == id_user or request.user.is_staff:
			user = User.objects.get(username=id_user)
			ad = Admin.objects.get(user=id_user)
			user_form = User_Form(request.POST or None, instance=user)
			ad_form = Admin_Form(request.POST or None, instance=ad)
			if user_form.is_valid() and ad_form.is_valid():
				form_data = user_form.cleaned_data
				user.username = form_data.get("username")
				user.email = form_data.get("email")
				user.first_name = form_data.get("first_name")
				user.second_name = form_data.get("second_name")
				user.last_name = form_data.get("last_name")
				user.second_last_name = form_data.get("second_last_name")
				user.gender = form_data.get("gender")
				form_data = ad_form.cleaned_data
				ad.address = form_data.get("address") 
				ad.city= form_data.get("city")
				user.save()
				ad.save()
			else:
				user = User.objects.get(username=id_user)
				ad = Admin.objects.get(user=id_user)
			context = {
				"user_form": user_form,
				"ad_form": ad_form,
				"username": user.username,
				"email": user.email,
				"first_name": user.first_name,
				"second_name": user.second_name,
				"last_name": user.last_name,
				"second_last_name": user.second_last_name,
				"gender": user.gender,
				"address": ad.address,
				"city": ad.city,
			}
			return render(request, "update_admin.html", context)
		else:
			return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')


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
