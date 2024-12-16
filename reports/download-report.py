# reports/views.py
from django.http import JsonResponse, FileResponse
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
import os

class DownloadSalesReportView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        task_id = request.query_params.get('task_id')
        
        # Validación de task_id
        if not task_id:
            return JsonResponse({"error": "task_id is required"}, status=400)

        # Definir la ruta del archivo
        file_path = os.path.join(settings.MEDIA_ROOT, 'reports', f'sales_report_{task_id}.csv')
        
        # Verificar si el archivo existe
        if os.path.exists(file_path):
            try:
                # Abrir el archivo de manera segura con `with` para evitar fugas de recursos
                with open(file_path, 'rb') as file:
                    response = FileResponse(file)
                    response['Content-Type'] = 'text/csv'
                    response['Content-Disposition'] = f'attachment; filename="sales_report_{task_id}.csv"'

                    # Eliminar el archivo después de que se haya servido
                    os.remove(file_path)
                    return response

            except Exception as e:
                return JsonResponse({"error": f"Error al abrir el archivo: {str(e)}"}, status=500)

        return JsonResponse({"error": "Reporte no encontrado o en proceso"}, status=404)
