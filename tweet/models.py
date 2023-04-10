from django.db import models
from user.models import UserModel
# Create your models here.


class TweetModel(models.Model):
    class Meta:     # 데이터 베이스에 정보를 넣어주는 역할
        db_table = "tweet"  # 테이블 이름

    user = models.ForeignKey(Usermodel, on_delete=models.CASCADE)
    image = models.URLField(max_length=200)
    content = models.TextField(verbose_name="내용", null=False)
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
