from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'user'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('follow/<int:user_id>', views.follow_function, name='following'),
    path('edit/<int:pk>/', views.edit_profile_view, name='edit'),
    path('user_image_upload/<int:user_id>', views.user_image_upload, name='user_image_upload'),
]
