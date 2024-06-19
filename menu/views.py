from django.shortcuts import render
from rest_framework import viewsets
from .models import MenusItem
from .serializers import MenuItemSerializer
from drf_spectacular.utils import extend_schema

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

class MenusItemViewSet(viewsets.ReadOnlyModelViewSet):
    """ 
    A simple ViewSet for viewing the menu items.
    """
    queryset = MenusItem.objects.all()
    serializer_class = MenuItemSerializer

