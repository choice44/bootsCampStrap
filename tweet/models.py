from django.db import models
from user.models import UserModel


# Create your models here.
class TweetModel(models.Model):

    user = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name="이름", related_name='tweet')
    image = models.ImageField(
        verbose_name='이미지', upload_to="photo/%Y/%m/%d")  # 파일 찾기 기능을 고려 시간대별 저장
    content = models.TextField("내용")
    update_at = models.DateTimeField(auto_now=True)
    # ordering(피드정렬)='-created_at'
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.ManyToManyField(UserModel, related_name='likeit', blank=True)

    @property   # 메소드의 return 값을 필드로 정의
    def short_content(self):
        return self.content[:15]    # title 대신 short_content로 간단하게 admin에서 보여주기

    def __str__(self):
        return self.short_content


# 댓글 모델
class CommentModel(models.Model):
    class Meta:
        db_table = "comment"
    tweet = models.ForeignKey(
        TweetModel, on_delete=models.CASCADE, verbose_name="트윗", related_name='tweet+')
    author = models.ForeignKey(
        UserModel, on_delete=models.CASCADE, verbose_name="댓글작성자")
    comment = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
