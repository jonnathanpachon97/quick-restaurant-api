# menu/views.py
from rest_framework import viewsets
from .models import MenuItem
from .serializers import MenuItemSerializer
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django_filters import rest_framework as django_filters
from rest_framework.pagination import PageNumberPagination


# Filtro personalizado para MenuItem
class MenuItemFilter(django_filters.FilterSet):
    # Filtros para el precio del menú
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    
    # Filtros para la disponibilidad
    available = django_filters.BooleanFilter(field_name='available')

    class Meta:
        model = MenuItem
        fields = ['restaurant', 'name', 'available', 'category', 'price', 'image_url']


# Paginación personalizada para MenuItem
class MenuItemPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'  # Permitir ajustar el tamaño de página a través de la URL
    max_page_size = 100  # Tamaño máximo de la página que puede ser solicitado


# ViewSet para el modelo MenuItem
class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [IsAuthenticated]
    
    # Filtros
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = MenuItemFilter  # Aplicar el filtro personalizado
    search_fields = ['name', 'description', 'category']  # Campos de búsqueda
    ordering_fields = ['name', 'price', 'category', 'available', 'restaurant']  # Campos por los que ordenar
    ordering = ['name']  # Orden por defecto (por nombre)
    
    # Paginación
    pagination_class = MenuItemPagination  # Usamos la paginación personalizada

