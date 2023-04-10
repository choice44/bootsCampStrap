from django.db import models


class UserModel(models.Model):
    class Meta:
        db_table = "user"

    username = models.CharField(max_length=32, verbose_name="이름", null=False)
    password = models.CharField(max_length=32, verbose_name="이름", null=False)
    bio = models.TextField(verbose_name="이름", null=False)
