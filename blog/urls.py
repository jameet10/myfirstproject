from django.urls import path
from .views import blog_index,get_posts,create_post
urlpatterns = [
    path('',blog_index),   
    path('posts/',get_posts),  
    path('posts/new',create_post) 
]