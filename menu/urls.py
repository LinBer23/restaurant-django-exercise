from . import views
from django.urls import path
from menu import views

urlpatterns = [   
  path('', views.menu, name ='menu'),
#  path('', views.menu, name ='menu'),    
]
