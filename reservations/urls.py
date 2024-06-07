from django.urls import path
from .views import ReservationsPageView

urlpatterns =[
    path('', ReservationsPageView.as_view(), name= 'reservations')
]