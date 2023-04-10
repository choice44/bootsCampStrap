from django import forms
from .models import Tweet


# form - 기본 Tweet폼
class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['user', 'image', 'content', 'update_at', 'created_at']
