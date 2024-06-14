from django.shortcuts import render
from rest_framework import viewsets
from .models import MenusItem
from .serializers import MenuItemSerializer

def menu(request):
    menu_list = MenusItem.objects.all()
    context = { 
        'menu_list': menu_list 
    }
    return render( request,
                   'pages/menu.html',
                   context )

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenusItem.objects.all()
    serializer_class = MenuItemSerializer

