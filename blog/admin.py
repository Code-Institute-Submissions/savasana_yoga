from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_on')

    list_filter = ("status",)

    search_fields = ['title', 'content']

    ordering = ('-created_on',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)