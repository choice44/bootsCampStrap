from django.db import models
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):

    class Meta:
        db_table = "my_user"

    follow = models.ManyToManyField(
        'self', blank=True, symmetrical=False, related_name='follower')
    bio = models.TextField("자기소개", blank=True)
    # blank를 지정하지 않으면, 이미지 값을 넣어달라고 요청함
    # null 이미지를 넣지 않아도 오류가 안남
    imgfile = models.ImageField(upload_to="user_images", blank=True, default="static/image/defaultprofileimage.jpeg")

    def __str__(self):
        return self.username
