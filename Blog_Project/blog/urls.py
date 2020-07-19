from django.urls import path
from .views import homepage, details, blog_details

app_name = 'blog'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('blogs/', details, name='details'),
    path('blogs/<str:id>', blog_details, name='blog_details')
]