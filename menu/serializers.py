from rest_framework import serializers
from .models import MenusItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenusItem
        #Felder angeben, die in der API auftauchen 
        fields = [
            'id',
            'name',
            'description',
            'price',            
        ]
