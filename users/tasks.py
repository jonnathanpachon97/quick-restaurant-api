# users/tasks.py
from celery import shared_task
import pandas as pd
from .models import User
from django.core.exceptions import ValidationError

@shared_task
def bulk_create_users(file_path):
    # Cargar el archivo usando pandas
    try:
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith('.xlsx'):
            df = pd.read_excel(file_path)
        else:
            raise ValidationError("Unsupported file format")
    except Exception as e:
        raise ValidationError(f"Error processing the file: {str(e)}")

    # Validar si el archivo contiene más de 20 usuarios
    if len(df) > 20:
        raise ValidationError("Cannot upload more than 20 users")

    # Procesar cada fila del archivo y crear usuarios
    for _, row in df.iterrows():
        user = User(
            first_name=row['first_name'],
            last_name=row['last_name'],
            email=row['email'],
            phone=row['phone'],
            default_address=row['default_address'],
            restaurant_id=row.get('restaurant_id', None),  # Opcional si existe en el archivo
            typology=row['typology'],
        )
        user.save()

    return f"Successfully created {len(df)} users"
