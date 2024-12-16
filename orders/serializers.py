# orders/serializers.py
from rest_framework import serializers
from .models import Order
from menu.models import MenuItem

class OrderSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(queryset=MenuItem.objects.all(), many=True)  # Usamos PrimaryKeyRelatedField para la relación ManyToMany

    class Meta:
        model = Order
        fields = '__all__'


