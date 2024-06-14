from django.db import models


# Create your models here.

class Reservation(models.Model):
    name = models.CharField(max_length = 100)

    timestamp = models.DateTimeField(null = True)    
    guests_quantity = models.IntegerField(null = True)

