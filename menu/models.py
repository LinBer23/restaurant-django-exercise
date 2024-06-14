from django.db import models



# Create your models here.

class Category(models.Model):
  title = models.CharField(max_length=100)


class MenusItem(models.Model):
    name =  models.CharField(max_length=50)
    description = models.TextField(max_length= 200)
    price = models.FloatField(null = True)
    
    category = models.ForeignKey(
       Category,
       null= True,
       on_delete= models.SET_NULL,
    #   related_name = 'items'
    )
    def __str__(self):
      return self.name

