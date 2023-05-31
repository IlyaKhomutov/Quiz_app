from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'is_staff', 'password1', 'password2']
