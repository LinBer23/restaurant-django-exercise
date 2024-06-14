from django.urls import path
#from .views import ReservationsPageView

from reservations import views

urlpatterns =[
    path('', views.reservations, name= 'reservations')
]