from datetime import date
from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Posts, Users

# Create your views here.

def blog_index(request):
    return render(request=request, template_name='blog_index.html')
def get_posts(request):
    return render(request=request, template_name='blog_index.html')
def get_posts(request):
    all_posts = Posts.objects.all()
    return render(request,'blog/posts.html',context={"all_posts": all_posts})

def create_post(request):
    print("test",dir(request))
    if request.method =='POST':
        title =request.POST('title_form')
        content =request.POST('content_form')
        try:
            #post1=Posts()
            #post1.title=title
            #post1.content=content
            #post1.pub_date=date.today().strftime("%Y-%m-%d")
            #post1.modified_date=date.today().strftime("%Y-%m-%d")
            #post1.user=Users.objects.get(id=1).idpost1.save()

            post2 = Posts(title=title,
                        content=content,
                        pub_date = date.today().strftime("%Y-%m-%d"),
                        modified_date = date.today().strftime("%Y-%m-%d"),
                        user = Users.objects.get(id=1))
            post2.save()
            return HttpResponse("Post added successfuly")
        except Exception as e:
            print(f"Error: {e}")
            return HttpResponse("something went wrong!!!")
    return render(request,'blog/posts/new_post.html')