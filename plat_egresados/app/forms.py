from django import forms
from .models import User, Egresado, Admin

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

class Notice_Form(forms.Form):
	title = forms.CharField(max_length=50)
	body = forms.CharField(max_length=50)
	media = forms.ImageField()
	category = forms.CharField(max_length=50)

class Category_Form(forms.Form):
	name = forms.CharField(max_length=50)
