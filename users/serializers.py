# users/serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, value):
        # Obtiene el usuario que estamos actualizando (en caso de ser un PUT)
        user = self.instance

        # Si el correo ha cambiado, verificamos si ya existe
        if value != user.email and User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo electrónico ya está en uso.")
        
        return value