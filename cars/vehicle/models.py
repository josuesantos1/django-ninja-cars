from django.db import models

class Vehicle(models.Model):
    title = models.CharField('Name',
                             max_length=150)
    brand = models.CharField('Brand',
                             max_length=50)
    model = models.CharField('Model',
                             max_length=50)
    photo = models.CharField('Photo',
                             max_length=1024)
    description = models.CharField('Description',
                             max_length=526)
    price = models.IntegerField('Price')

