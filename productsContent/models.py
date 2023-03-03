from django.db import models
from django.contrib.auth.models import User
import os


class Brand(models.Model):

    name = models.CharField(max_length = 15)

    def __str__(self):
        return f'{self.name}'
    

class Shoe_size(models.Model):

    name = models.CharField(max_length=10)
    f40 = models.IntegerField()
    f40d5 = models.IntegerField()
    f41 = models.IntegerField()
    f41d5 = models.IntegerField()
    f42 = models.IntegerField()
    f42d5 = models.IntegerField()
    f43 = models.IntegerField()
    f44 = models.IntegerField()
    f44d5 = models.IntegerField()
    f45 = models.IntegerField()

    def __str__(self):
        return f'{self.name}'
    
    
class Image(models.Model):
        
    name = models.CharField(max_length=10)
    img1 = models.ImageField(upload_to='image/%Y')
    img2 = models.ImageField(upload_to='image/%Y')
    img3 = models.ImageField(upload_to='image/%Y')

    def __str__(self):
        return f'{self.name}'
    
    
class Products(models.Model):

    brand = models.ForeignKey(Brand, related_name='items', on_delete=models.CASCADE)
    model_name = models.CharField(max_length=20)
    price =  models.DecimalField(max_digits = 6, decimal_places = 2)
    size = models.ForeignKey(Shoe_size, on_delete=models.CASCADE)
    images = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.brand} {self.model_name}'
    


