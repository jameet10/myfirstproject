from django.urls import path
from .views import blog_index,get_posts
urlpatterns = [
    path('',blog_index),   
    path('posts/',get_posts),   
]