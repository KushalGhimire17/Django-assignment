from django.shortcuts import render
from django.http import HttpResponse

def homepage(request):
    return render(request, 'blog/home.html')

def details(request):
    return HttpResponse("Details here")