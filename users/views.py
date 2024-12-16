# users/views.py
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework as django_filters

class UserFilter(django_filters.FilterSet):
    created_at_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    updated_at_after = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='gte')
    updated_at_before = django_filters.DateTimeFilter(field_name='updated_at', lookup_expr='lte')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone', 'typology', 'active', 'restaurant', 'created_at', 'updated_at']

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = UserFilter
    search_fields = ['first_name', 'last_name', 'email', 'phone', 'typology', 'restaurant__name', 'created_at', 'updated_at']
    ordering_fields = ['first_name', 'last_name', 'email', 'phone', 'typology', 'active', 'created_at', 'updated_at']
    ordering = ['first_name']
