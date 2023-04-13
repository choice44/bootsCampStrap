from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel


class UserForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'bio']


class EditProfileForm(UserChangeForm):
    class Meta:
        model = UserModel
        fields = ('bio',)

        
class FileForm(forms.ModelForm):
    
    class Meta:
        model = UserModel
        fields = ['imgfile']
