from django import forms
from .models import UserModel


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel

    field = fields = ['username', 'password', 'bio',]
