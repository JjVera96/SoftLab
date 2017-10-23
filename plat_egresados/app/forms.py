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
		fields = ["country", "career", "graduation"]

class Admin_Form(forms.ModelForm):
	class Meta:
		model = Admin
		fields= ["address"]

class Login_Form(forms.Form):
	id_user = forms.CharField(max_length= 50)
	password = forms.CharField(max_length= 50)

class Forget_Form(forms.Form):
	email = forms.EmailField(max_length=50)