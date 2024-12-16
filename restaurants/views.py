# restaurants/views.py
from django_filters.rest_framework import FilterSet, CharFilter, BooleanFilter, DateFromToRangeFilter  # Importar filtros de django-filter
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from .models import Restaurant
from .serializers import RestaurantSerializer

# Clase de Filtro Personalizado para el modelo Restaurant
class RestaurantFilter(FilterSet):  # Usamos FilterSet de django_filters
    name = CharFilter(lookup_expr='icontains')  # Filtro por nombre (case insensitive)
    category = CharFilter(lookup_expr='icontains')  # Filtro por categoría (case insensitive)
    status = CharFilter(lookup_expr='icontains')  # Filtro por estado
    activate = BooleanFilter()  # Filtro por activo/inactivo
    created_at = DateFromToRangeFilter()  # Rango de fechas para created_at
    updated_at = DateFromToRangeFilter()  # Rango de fechas para updated_at

    class Meta:
        model = Restaurant
        fields = ['name', 'category', 'status', 'activate', 'created_at', 'updated_at']

# Clase de Paginación para los resultados
class RestaurantPagination(PageNumberPagination):
    page_size = 10  # Número de elementos por página
    page_size_query_param = 'page_size'  # Puedes pasar el tamaño de página con el parámetro de la query
    max_page_size = 100  # Tamaño máximo de página

# ViewSet para el modelo Restaurant
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo los usuarios autenticados puedan acceder
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter)
    filterset_class = RestaurantFilter  # Asignamos los filtros personalizados
    pagination_class = RestaurantPagination  # Asignamos la paginación personalizada
    search_fields = ['name', 'address', 'category']  # Campos a los que se les puede hacer búsqueda
    ordering_fields = ['rating', 'name', 'category']  # Campos por los que se puede ordenar
    ordering = ['name']  # Orden por defecto