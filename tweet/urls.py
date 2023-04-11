from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create_tweet, name='create_tweet'),
    path('tweet/', views.show_tweet, name='show_tweet'),
    path('detail/<int:detail_id>', views.detail_tweet, name='detail'),
    path('update/<int:update_id>', views.update_tweet, name='update'),
    path('delete/<int:delete_id>', views.delete_tweet, name='delete'),
    path('mypage/<int:user_id>', views.my_page, name='my_page'),
]
