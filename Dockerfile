# Usa la imagen oficial de Python como base
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . .

# Instala las dependencias necesarias (las que están en requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto (solo necesario si tu app tiene servidor web, no es obligatorio para Celery)
EXPOSE 8000

# Define el comando para iniciar el worker de Celery
CMD ["celery", "-A", "app", "worker", "--loglevel=info"]