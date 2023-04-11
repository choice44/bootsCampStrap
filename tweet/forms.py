from django import forms
from .models import TweetModel


# form - 기본 Tweet폼
class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        fields = ['user', 'image', 'content', 'update_at', 'created_at']
