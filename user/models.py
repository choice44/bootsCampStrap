from django.db import models


class UserModel(models.Model):
    class Meta:
        db_table = "user"

    username = models.CharField("이름", max_length=50)
    password = models.CharField("비밀번호", max_length=500)
    bio = models.TextField("자기소개")

    def __str__(self):
        return self.username
