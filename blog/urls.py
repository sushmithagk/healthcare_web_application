from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('create/', views.create_post, name='blog_create'),
    path('my-posts/', views.my_posts, name='blog_my_posts'),
    path('category/<slug:slug>/', views.category_posts, name='blog_category'),
    path('post/<int:pk>/', views.post_detail, name='blog_detail'),
]
