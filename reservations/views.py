from django.shortcuts import render
from django.views.generic import TemplateView

class ReservationsPageView(TemplateView):
    template_name = 'pages/reservations.html'