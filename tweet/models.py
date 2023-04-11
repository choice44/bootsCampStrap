from django.db import models
from user.models import UserModel
# Create your models here.


class TweetModel(models.Model):

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name="이름")
    image = models.URLField('이미지', unique=True, blank=True,
                            null=True)  # 사진이 없어도 트윗 추가 가능
    content = models.TextField("내용")
    update_at = models.DateTimeField("수정날짜", auto_now=True)
    # ordering(피드정렬)='-created_at'
    created_at = models.DateTimeField("생성날짜", auto_now_add=True)

    class Meta:     # 데이터 베이스에 정보를 넣어주는 역할
        db_table = "tweet"  # 테이블 이름

    @property   # 메소드의 return 값을 필드로 정의
    def short_content(self):
        return self.content[:15]    # title 대신 short_content로 간단하게 admin에서 보여주기

    def __str__(self):
        return self.short_content
