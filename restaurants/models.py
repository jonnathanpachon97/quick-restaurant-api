# restaurants/models.py
from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20)
    category = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=21, decimal_places=11)
    longitude = models.DecimalField(max_digits=21, decimal_places=11)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activate = models.BooleanField(default=True)