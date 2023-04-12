from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserModel


class UserForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'bio']
