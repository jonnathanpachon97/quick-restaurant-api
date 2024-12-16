# orders/views.py
from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.pagination import PageNumberPagination


# Filtro personalizado para Order
class OrderFilter(django_filters.FilterSet):
    # Filtro para rango de fechas de creación
    created_at_after = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='gte')
    created_at_before = django_filters.DateTimeFilter(field_name='created_at', lookup_expr='lte')
    
    # Filtro para el total_amount
    total_amount_min = django_filters.NumberFilter(field_name='total_amount', lookup_expr='gte')
    total_amount_max = django_filters.NumberFilter(field_name='total_amount', lookup_expr='lte')

    class Meta:
        model = Order
        fields = ['customer', 'restaurant', 'status', 'total_amount', 'estimated_delivery_time', 'created_at', 'updated_at']


# Paginación personalizada para Order
class OrderPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'  # Permitir ajustar el tamaño de página a través de la URL
    max_page_size = 100  # Tamaño máximo de la página que puede ser solicitado


# ViewSet para el modelo Order
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    # Filtros
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = OrderFilter  # Aplicar el filtro personalizado
    search_fields = ['delivery_address', 'special_instructions']  # Campos de búsqueda
    ordering_fields = ['total_amount', 'created_at', 'status', 'estimated_delivery_time']  # Campos por los que ordenar
    ordering = ['created_at']  # Orden por defecto (por fecha de creación)
    
    # Paginación
    pagination_class = OrderPagination  # Usamos la paginación personalizada