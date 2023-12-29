from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from django import forms

class CreateUsersForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    phone_number = forms.CharField(max_length=15, required=False)
    profile_picture = forms.FileField(required=False)
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'phone_number', 'profile_picture', 'groups')

class AddGroupForm(forms.Form):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
