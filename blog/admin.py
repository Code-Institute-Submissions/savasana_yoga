from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_on')

    search_fields = ['title', 'content']

    ordering = ('-created_on',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body', 'post', 'created_on', 'approved_comment')
    list_filter = ('approved_comment', 'created_on')
    search_fields = ('author', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved_comment=True)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
