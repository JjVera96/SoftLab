from django import forms
from .models import User, Egresado, Admin, Noticia, Categoria, Mensaje

class User_Form(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username", "email", "first_name", "second_name", "last_name", "second_last_name", "gender"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		base, exten = email.split("@")
		if not "utp.edu.co" == exten:
			raise forms.ValidationError("Ingrese por favor el correo institucional")
		return email

class Egre_Form(forms.ModelForm):
	class Meta:
		model = Egresado
		fields = ["country", "career", "graduation", "birthdate"]

class Admin_Form(forms.ModelForm):
	class Meta:
		model = Admin
		fields= ["address", "city"]

class Login_Form(forms.Form):
	id_user = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)

	def clean_id_user(self):
		id_user = self.cleaned_data.get("id_user")
		if id_user.isdigit() or id_user=="admin":
			return id_user
		raise forms.ValidationError("Los codigos son solamente numeros")
		
class Forget_Form(forms.Form):
	email = forms.EmailField(max_length=50)

class New_Password_Form(forms.Form):
	password = forms.CharField(max_length=50)
	again = forms.CharField(max_length=50)

class Change_Form(forms.Form):
	old = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50)
	again = forms.CharField(max_length=50)

class Notice_Form(forms.ModelForm):
	class Meta:
		model = Noticia
		fields = ["title", "body", "media", "category"]

class Category_Form(forms.ModelForm):
	class Meta:
		model = Categoria
		fields = ["name"]

class Mensaje_Form(forms.ModelForm):
	class Meta:
		model = Mensaje
		fields = ["title", "body"]