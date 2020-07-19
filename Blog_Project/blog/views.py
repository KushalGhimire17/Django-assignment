from django.shortcuts import render
from .models import Blog

def homepage(request):
    return render(request, 'blog/home.html')

# list of blogs
def details(request):
    blogs = Blog.objects.all()
    return render(request, 'blog/detail.html', {'blogs': blogs})

# details of individual blog
def blog_details(request, id):
    blog = Blog.objects.get(pk=id)
    return render(request, 'blog/blog_detail.html', {'blog': blog})
