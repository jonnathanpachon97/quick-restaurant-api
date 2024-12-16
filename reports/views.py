# reports/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .tasks import generate_sales_report  # La tarea de Celery que generará el reporte
from rest_framework import status

class GenerateSalesReportView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, restaurant_id, month):
        # Llamamos a la tarea de Celery
        generate_sales_report.delay(restaurant_id, month)
        return Response({'message': 'Reporte generado. Estará disponible pronto.'}, status=status.HTTP_202_ACCEPTED)
