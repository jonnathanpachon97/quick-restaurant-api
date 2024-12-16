"""
URL configuration for restaurant_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from restaurants.views import RestaurantViewSet
from users.views import UserViewSet
from menu.views import MenuItemViewSet
from orders.views import OrderViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_simplejwt.authentication import JWTAuthentication
from reports.views import GenerateSalesReportView

# Crear el esquema de autenticación JWT para Swagger
swagger_jwt_security = openapi.Parameter(
    'Authorization',
    in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING,
    description="Bearer <JWT token>"
)

# Crear la vista del esquema de Swagger sin usar SecurityRequirement
schema_view = get_schema_view(
    openapi.Info(
        title="API Restaurant",
        default_version='v1',
        description="Documentación de la API REST",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="restaurantapi@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    authentication_classes=[JWTAuthentication],  # Usar JWT para la autenticación
)


router = DefaultRouter()
router.register(r'restaurants', RestaurantViewSet)
router.register(r'users', UserViewSet)
router.register(r'menu-items', MenuItemViewSet)
router.register(r'orders', OrderViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Rutas para obtener y refrescar el token
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Ruta para la documentación de Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger-docs'),
    # Ruta para la documentación de ReDoc (si deseas usarla en lugar de Swagger)
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-docs'),

    # Incluir las URLs de reportes
    path('api/reports/', include('reports.urls')),  # Incluimos las rutas de reportes
    path('api/reports/generate_sales_report/<int:restaurant_id>/<int:month>/', GenerateSalesReportView.as_view(), name='generate_sales_report'),  
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)