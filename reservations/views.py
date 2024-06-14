from django.shortcuts import render
from rest_framework import viewsets
from .models import Reservation
from .serializer import ReservationsSerializer


def reservations(request):
    reservations_list = Reservation.objects.all() 
    context = {
        'reservations_list' : reservations_list
    }
    return render(
        request,
        'pages/reservations.html',
        context
    )

class ReservationsViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationsSerializer