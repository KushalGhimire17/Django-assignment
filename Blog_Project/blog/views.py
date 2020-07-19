from django.shortcuts import render
from .models import Blog

def homepage(request):
    return render(request, 'blog/home.html')

def details(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/detail.html', {'blogs': blogs})