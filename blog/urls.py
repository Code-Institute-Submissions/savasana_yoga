from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_blog, name='view_blog'),
    path('<blog_id>/', views.blog_post_detail, name='blog_post_detail'),
]
