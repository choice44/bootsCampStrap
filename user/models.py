from django.db import models


class UserModel(models.Model):
    class Meta:
        db_table = "user"

    username = models.CharField(max_length=50, verbose_name="이름")
    password = models.CharField(max_length=500, verbose_name="비밀번호")
    bio = models.TextField(verbose_name="자기소개")
