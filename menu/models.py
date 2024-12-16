# menu/models.py
from django.db import models
from restaurants.models import Restaurant

class MenuItem(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.CharField(max_length=100)
    image_url = models.CharField(max_length=255, null=True, blank=True)