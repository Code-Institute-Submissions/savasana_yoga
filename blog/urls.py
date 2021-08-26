from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('add_blog_post/', views.add_blog_post, name='add_blog_post'),
    path('<slug:slug>/', views.blog_post_detail, name='blog_post_detail'),
    
]