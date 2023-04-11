from django.contrib import admin
from .models import UserModel


class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'bio')


admin.site.register(UserModel, UserModelAdmin)
