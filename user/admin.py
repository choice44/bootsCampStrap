from django.contrib import admin
from .models import UserModel


# admin페이지에서
# User테이블 필드값 보여주기
# Object (1)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'bio')


admin.site.register(UserModel, UserModelAdmin)
