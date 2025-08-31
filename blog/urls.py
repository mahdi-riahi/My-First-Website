from django.urls import path
from . import views

urlpatterns= [
    path('',views.welcome_blog,name='home'),
    path('first/',views.first_article,name='first article'),
]