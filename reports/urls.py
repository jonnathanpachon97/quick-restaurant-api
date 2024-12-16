# reports/urls.py
from django.urls import path
from .views import GenerateSalesReportView, DownloadSalesReportView

urlpatterns = [
    # Ruta para generar el reporte
    path('generate-report/', GenerateSalesReportView.as_view(), name='generate_report'),
    
    # Ruta para descargar el reporte
    path('download-report/', DownloadSalesReportView.as_view(), name='download_report'),
]
