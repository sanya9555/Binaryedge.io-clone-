from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
    path('app', views.index, name="home"),
    path('data', views.data, name="data"),
    path('pricing', views.pricing, name="pricing"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),
    path('blog', views.blog, name="blog"),
    
    
]