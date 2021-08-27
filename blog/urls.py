from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('<int:blog_post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('edit_blog_post/<int:blog_post_id>/', views.edit_blog_post, name='edit_blog_post'),
    path('delete_blog_post/<int:blog_post_id>/', views.delete_blog_post, name='delete_blog_post'),
]