from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/create/', views.create_tweet, name='create_tweet'),
    path('tweet/', views.show_tweet, name='show_tweet'),
    path('tweet/detail/<int:detail_id>', views.detail_tweet, name='detail'),
    path('tweet/update/<int:update_id>', views.update_tweet, name='update'),
    path('tweet/delete/<int:delete_id>', views.delete_tweet, name='delete'),
    path('tweet/mypage/<int:user_id>', views.my_page, name='my_page'),
]
