from django.db import models
from django.contrib.auth.models import AbstractUser, User


class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user"

    bio = models.TextField("자기소개", blank=True)

    def __str__(self):
        return self.username


# class UserModel(AbstractUser):
#     class Meta:
#         db_table = "user"

#     bio = models.TextField(max_length=500, default='')
