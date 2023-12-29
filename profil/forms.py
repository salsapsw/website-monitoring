from django import forms
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

class UserEditForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number']

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['profile_picture']

class PasswordChangeCustomForm(PasswordChangeForm):
    class Meta:
        model = User

