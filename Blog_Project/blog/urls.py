from django.urls import path
from .views import homepage, details

app_name = 'blog'
urlpatterns = [
    path('', homepage, name='homepage'),
    path('blogs/', details, name='details')
]