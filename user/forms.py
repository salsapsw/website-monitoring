from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)
    

# class PasswordChangeCustomForm(PasswordChangeForm):
#     class Meta:
#         model = User