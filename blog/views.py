from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def welcome_blog(request):
    return HttpResponse('<h1 style="background-color:blue; color; white;">Hello\nWellcome to my blog</h1><p>This is our first page</p>')
