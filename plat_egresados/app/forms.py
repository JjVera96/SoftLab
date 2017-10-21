from django import forms
from .models import User, Egresado

class User_Form(forms.ModelForm):
	class Meta:
		model = User
		fields = ["identification", "email", "first_name", "second_name", "last_name", "second_last_name", "gender"]

class Egre_Form(forms.ModelForm):
	class Meta:
		model = Egresado
		fields = ["country", "career", "graduation"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		base, exten = email.split("@")
		if not "utp.edu.co" == exten:
			raise forms.ValidationError("Ingrese por favor el correo institucional")
		return email

class Login_Form(forms.Form):
	id_user = forms.CharField(max_length= 30)
	password = forms.CharField(max_length= 30)