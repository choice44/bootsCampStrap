from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserModel


# 회원가입용 폼
class UserForm(UserCreationForm):

    class Meta:
        model = UserModel
        fields = ['username', 'password1', 'password2', 'bio']


# 회원정보 수정을 위한 UserChangeForm 상속
class EditProfileForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ['bio']


# 사진 업로드 페이지용 폼
class FileForm(forms.ModelForm):

    class Meta:
        model = UserModel
        fields = ['imgfile']
