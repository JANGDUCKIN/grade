from django.contrib.auth.models import User
# from .models import UploadFile
from django import forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)


	class Meta:
		model = User
		fields = ['username', 'email', 'password']

class LoginForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username', 'password']		


# class UploadFileForm(forms.ModelForm):
# 	class Meta:
# 		model = UploadFile
# 		fields = ['file', 'score', 'result']
