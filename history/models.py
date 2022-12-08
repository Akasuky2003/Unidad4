from django.db import models
import datetime

class Publicacion(models.Model):
    title= models.CharField(max_length=100)
    description= models.CharField(max_length=250)
    image= models.ImageField(upload_to='blog/images')
    date=models.DateField(datetime.datetime.today)
