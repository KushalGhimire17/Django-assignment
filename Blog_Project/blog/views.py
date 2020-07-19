from django.shortcuts import render
from .models import Blog

def homepage(request):
    return render(request, 'blog/home.html')

def details(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/detail.html', {'blogs': blogs})

def blog_details(request, id):
    blogs = Blog.objects.all().get(pk=id)
    return render(request, 'blog/blog_detail.html', {'blogs': blogs})
