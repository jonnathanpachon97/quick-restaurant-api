# reports/urls.py
from django.urls import path
from .generate_report import GenerateSalesReportView  # Importar desde generate-report.py
from .download_report import DownloadSalesReportView  # Importar desde download-report.py

urlpatterns = [
    # Ruta para generar el reporte
    path('generate-report/', GenerateSalesReportView.as_view(), name='generate_report'),
    
    # Ruta para descargar el reporte
    path('download-report/', DownloadSalesReportView.as_view(), name='download_report'),
]