# reports/views.py
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from reports.tasks import generate_sales_report

class GenerateSalesReportView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, *args, **kwargs):
        # Obtener parámetros
        restaurant_id = request.data.get('restaurant_id')
        month = request.data.get('month')

        if not restaurant_id or not month:
            return JsonResponse({"error": "restaurant_id and month are required"}, status=400)

        # Iniciar tarea Celery
        result = generate_sales_report.delay(restaurant_id, month)
        
        return JsonResponse({"message": "Reporte en proceso", "task_id": result.id})
