from django import forms
from .models import TweetModel, CommentModel


# form - 기본 Tweet폼
class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        fields = ['image', 'content']
        # user는 빠져도 되는데 저장할 땐 값이 있어야 한다.


# 댓글 폼
class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ['comment']
