# users/views.py
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .tasks import bulk_create_users

class BulkUserUploadView(APIView):
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    parser_classes = (MultiPartParser, FormParser)  # Para aceptar archivos CSV o XLSX

    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')  # Obtener el archivo del request

        if not file:
            return Response({"error": "No file provided"}, status=400)

        file_extension = file.name.split('.')[-1].lower()

        # Validar que el archivo sea CSV o XLSX
        if file_extension not in ['csv', 'xlsx']:
            return Response({"error": "File must be a CSV or XLSX file"}, status=400)

        # Cargar el archivo con pandas
        try:
            if file_extension == 'csv':
                df = pd.read_csv(file)
            elif file_extension == 'xlsx':
                df = pd.read_excel(file)
        except Exception as e:
            return Response({"error": f"Error processing the file: {str(e)}"}, status=400)

        # Validar que no haya más de 20 usuarios
        if len(df) > 20:
            return Response({"error": "Cannot upload more than 20 users"}, status=400)

        # Guardar el archivo temporalmente (esto lo hacemos para la tarea de Celery)
        file_path = f'/tmp/{file.name}'
        with open(file_path, 'wb') as temp_file:
            for chunk in file.chunks():
                temp_file.write(chunk)

        # Llamar a la tarea de Celery para procesar el archivo
        bulk_create_users.delay(file_path)

        return Response({"message": "File is being processed."})