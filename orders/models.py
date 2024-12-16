# orders/models.py
from django.db import models
from users.models import User
from restaurants.models import Restaurant
from menu.models import MenuItem  # Importación directa de MenuItem

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_address = models.TextField()
    special_instructions = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20)
    estimated_delivery_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # Relación muchos a muchos con MenuItem
    items = models.ManyToManyField(MenuItem)  # Esto elimina la necesidad del método get_menu_item
    
    def __str__(self):
        return f"Order {self.id} - {self.customer.first_name}"