from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome_blog(request):
    return HttpResponse('<h1 style="background-color:blue; color; white;">Hello\nWellcome to my blog</h1><p>This is our first page made with simple html,css</p><br><a href="first">First article</a>')

def first_article(request):
    context={'currentdatetime':datetime.now().strftime("%Y-%m-%d  %H:%M:%S")}
    return render(request,'blog/index.html',context)