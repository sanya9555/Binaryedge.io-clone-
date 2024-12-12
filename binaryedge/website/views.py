from django import http
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.contrib import auth

def index(request):
    return render(request,"websites/index.html")

def data(request):
    return render(request,"websites/data.html")

def about(request):
    return render(request,"websites/about.html")

def pricing(request):
    return render(request,"websites/pricing.html")

def contact(request):
    return render(request,"websites/contact.html")

def blog(request):
    return render(request,"websites/blog.html")

