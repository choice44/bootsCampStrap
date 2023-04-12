from django.contrib import admin
from .models import TweetModel, CommentModel


class TweetModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image',
                    'short_content', 'update_at', 'created_at']
    list_display_links = ['id', 'user']
    list_filter = ('user', 'update_at', 'created_at',)


# class CommentModelAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'image',
#                     'short_content', 'update_at', 'created_at']
#     list_display_links = ['id', 'user']
#     list_filter = ('user', 'update_at', 'created_at',)


admin.site.register(TweetModel, TweetModelAdmin)
# admin.site.register(CommentModel, CommentModelAdmin)
