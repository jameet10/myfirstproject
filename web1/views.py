from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return HttpResponse("Hello")


def home(request):
    return render (request=request,template_name='index.html')
        
