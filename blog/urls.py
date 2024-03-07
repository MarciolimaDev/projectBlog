from django.urls import path
from . import views



appName = 'blog'

urlpatterns = [
    path('', views.home, name='home'),
]
