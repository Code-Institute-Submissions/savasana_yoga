from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('<int:blog_post_id>/',
         views.blog_post_detail,
         name='blog_post_detail'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('edit_blog_post/<int:blog_post_id>/',
         views.edit_blog_post, name='edit_blog_post'),
    path('delete_blog_post/<int:blog_post_id>/',
         views.delete_blog_post, name='delete_blog_post'),
    path('add_comment/<int:blog_post_id>/',
         views.add_blog_post_comment, name='add_blog_post_comment'),
    path('comment_approve/<int:comment_id>/',
         views.comment_approve, name='comment_approve'),
    path('comment_remove/<int:comment_id>',
         views.comment_remove, name='comment_remove'),
    path('edit_comment/<int:comment_id>',
         views.edit_comment, name='edit_comment'),
]
