from django.urls import path
from . import views
from user.views import follow_tweet_view

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/create/', views.create_tweet, name='create_tweet'),
    path('tweet/', views.show_tweet, name='show_tweet'),
    path('tweet/detail/<int:detail_id>', views.detail_tweet, name='detail'),

    # 댓글 모델이 이 아래에 url 작성
    path('tweet/comment/<int:detail_id>',
         views.write_comment, name='write-comment'),
    path('tweet/comment/delete/<int:comment_id>',
         views.delete_comment, name='delete-comment'),
    path('tweet/comment/update/<int:comment_id>',
         views.update_comment, name='update-comment'),
    # 댓글모델

    path('tweet/update/<int:update_id>', views.update_tweet, name='update'),
    path('tweet/delete/<int:delete_id>', views.delete_tweet, name='delete'),
    path('tweet/mypage/<int:user_id>', views.my_page, name='my_page'),
    path('tweet/likes/<int:tweet_id>', views.like_create, name='like_create'),
    path('tweet/followers', follow_tweet_view, name='followers'),
]
