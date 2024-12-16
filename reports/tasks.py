# reports/tasks.py
from celery import shared_task
import csv
from io import StringIO
from orders.models import Order  # Cambié la importación para que apunte al lugar correcto
from django.core.files.base import ContentFile
from django.conf import settings
import os

@shared_task
def generate_sales_report(restaurant_id, month):
    # Filtrar pedidos según restaurante y mes
    orders = Order.objects.filter(restaurant_id=restaurant_id, created_at__month=month)
    
    # Calcular total de ventas
    total_sales = sum(order.total_amount for order in orders)
    
    # Crear CSV
    output = StringIO()
    writer = csv.writer(output, delimiter=';')
    writer.writerow(['id', 'name', 'total_sales', 'total_amount'])
    
    for order in orders:
        writer.writerow([order.id, order.restaurant.name, order.total_amount, total_sales])
    
    output.seek(0)
    
    # Guardar el archivo CSV temporalmente
    report_file = ContentFile(output.getvalue())
    file_path = os.path.join(settings.MEDIA_ROOT, f'report_{restaurant_id}_{month}.csv')
    with open(file_path, 'wb') as f:
        f.write(report_file.read())

    return file_path