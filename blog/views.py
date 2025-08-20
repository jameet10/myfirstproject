from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Posts
# Create your views here.

def blog_index(request):
    return render(request=request, template_name='blog_index.html')

def get_posts(request):
    all_posts= Posts.objects.all()
    return render(request,'blog/posts.html',context={"all_posts":all_posts})    