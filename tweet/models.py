from django.db import models
from user.models import UserModel
# Create your models here.


class TweetModel(models.Model):

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    image = models.URLField('url', unique=True, blank=True)  # 사진이 없어도 트윗 추가 가능
    content = models.TextField(verbose_name="내용", null=False)
    # ordering(피드정렬)='-created_at'
    update_at = models.DateTimeField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    class Meta:     # 데이터 베이스에 정보를 넣어주는 역할
        db_table = "tweet"  # 테이블 이름

    def __str__(self):
        return str(self.id)
