from rest_framework import serializers
from .models import Reservation

class ReservationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            'id',
            'name',
            'timestamp',
            'guests_quantity'
        ]