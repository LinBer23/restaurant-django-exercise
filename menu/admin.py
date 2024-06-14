from django.contrib import admin
from .models import Category, MenusItem
# Register your models here.

admin.site.register(MenusItem)
admin.site.register(Category)