# users/models.py
from django.db import models
from restaurants.models import Restaurant

class User(models.Model):
    DEALER = 'dealer'
    CUSTOMER = 'customer'
    TYPOS = [(DEALER, 'Dealer'), (CUSTOMER, 'Customer')]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    default_address = models.TextField()
    restaurant = models.ForeignKey(Restaurant, null=True, on_delete=models.SET_NULL)
    typology = models.CharField(max_length=10, choices=TYPOS)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)