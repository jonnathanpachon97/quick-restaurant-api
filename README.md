# API Restaurant

## Descripción
Esta API permite la gestión de restaurantes, menús, pedidos, y la generación de reportes de ventas.

## Funcionalidades Principales
- **Gestión de Restaurantes**: Crear, editar, listar y eliminar restaurantes.
- **Gestión de Pedidos**: Crear y gestionar pedidos de clientes.
- **Generación de Reportes de Ventas**: Genera reportes de ventas en formato CSV utilizando Celery para procesar los reportes de manera asíncrona.
- **Autenticación**: Autenticación basada en JWT para asegurar las operaciones.
  
## Tecnologías Utilizadas
- **Python 3.x**: Lenguaje de programación.
- **Django 4.x**: Framework web para la creación de la API.
- **Django REST Framework**: Para la creación de la API RESTful.
- **Celery**: Para tareas asíncronas como la generación de reportes.
- **Redis**: Usado como broker para Celery.
- **PostgreSQL**: Base de datos relacional para almacenamiento de datos.
- **JWT Authentication**: Para la autenticación de los usuarios.

## Requisitos
- Python 3.x
- Django 4.x
- Django REST Framework
- Celery
- Redis
- PostgreSQL
- JWT Authentication

## Instalación
1. Clonar el repositorio:
   ```bash
    git clone https://github.com/jonnathanpachon97/quick-restaurant-api.git
    cd nombre-repositorio

2. Crear y activar un entorno virtual:
    ```bash
    python -m venv env
    source env/Scripts/activate

3. Instalar los requisitos del archivo requirements.txt:
   ```bash
    pip install -r requirements.txt

4. Crear una base de datos en PostgreSQL:

- Accede a la consola de PostgreSQL.

- Crea una nueva base de datos con el siguiente comando:
    ```bash
    CREATE DATABASE nombre_de_tu_base_de_datos;
    
- Crea un nuevo usuario para acceder a la base de datos con privilegios. Reemplaza usuario y contraseña con los valores que desees:
    ```bash
    CREATE USER usuario WITH PASSWORD 'contraseña';

5. Configurar Django para usar PostgreSQL
    En tu proyecto Django, abre el archivo settings.py y configura la base de datos con los valores que acabas de crear.

Aquí hay un ejemplo de cómo se configuraría la base de datos en settings.py:
    ```bash
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre_de_tu_base_de_datos',
        'USER': 'usuario',
        'PASSWORD': 'contraseña',
        'HOST': 'localhost',  # o la IP de tu servidor PostgreSQL si es remoto
        'PORT': '5432',  # Puerto por defecto de PostgreSQL
    }
}

6. Realizar migraciones de la base de datos:
    ```bash
    python manage.py migrate

7. Cargar datos de prueba:

- Acceder a Django Shell:
Para comenzar, ejecuta el siguiente comando en tu terminal:
    ```bash
    python manage.py shell

- Crear los datos de prueba: (ver archivo datosprueba.txt)
    
- Salir del Django shell
    ```bash
    exit()

8. Iniciar el servidor:
    ```bash
    python manage.py runserver

9. Iniciar Redis:Asegúrate de tener Redis corriendo en tu máquina para que Celery funcione correctamente. Puedes iniciar Redis con el siguiente comando:
    ```bash
    redis-server

10. Iniciar Celery: En una terminal diferente, corre el worker de Celery:
    ```bash
    celery -A restaurant_api worker --loglevel=info

## Endpoints

- **Token Autenticación**

POST http://127.0.0.1:8000/api/token/

{
  "username": "jonnathan",
  "password": "apiquick"
}

POST http://127.0.0.1:8000/api/token/refresh/

{
    "refresh": "Generado en el endpoint token"
}

NOTA: recuerda que para ejecutar todos los endpoints requiere el token de authenticacion.

- **Restaurants**

POST http://127.0.0.1:8000/api/restaurants/
GET http://127.0.0.1:8000/api/restaurants/
GET http://127.0.0.1:8000/api/restaurants/{ID}/
PUT http://127.0.0.1:8000/api/restaurants/{ID}/
DELETE http://127.0.0.1:8000/api/restaurants/{ID}/
FILTERS http://127.0.0.1:8000/api/restaurants/?ordering=rating

- **Menu-items**

POST http://127.0.0.1:8000/api/menu-items/
GET http://127.0.0.1:8000/api/menu-items/
GET http://127.0.0.1:8000/api/menu-items/{ID}/
PUT http://127.0.0.1:8000/api/menu-items/{ID}/
DELETE http://127.0.0.1:8000/api/menu-items/{ID}/
FILTERS http://127.0.0.1:8000/api/menu-items/?category=Main Course

- **Orders**

POST http://127.0.0.1:8000/api/orders/
GET http://127.0.0.1:8000/api/orders/
GET http://127.0.0.1:8000/api/orders/{ID}/
PUT http://127.0.0.1:8000/api/orders/{ID}/
DELETE http://127.0.0.1:8000/api/orders/{ID}/
FILTERS http://127.0.0.1:8000/api/orders/?created_at=2024-12-14 13:23:26.996199-05

- **Users**

POST http://127.0.0.1:8000/api/users/
GET http://127.0.0.1:8000/api/users/
GET http://127.0.0.1:8000/api/users/{ID}/
PUT http://127.0.0.1:8000/api/users/{ID}/
DELETE http://127.0.0.1:8000/api/users/{ID}/
FILTERS http://127.0.0.1:8000/api/users/?first_name=Jonnathan

- **Reports**
POST http://localhost:8000/api/reports/generate-report/
GET http://localhost:8000/api/reports/download-report/
POST http://localhost:8000/api/users/bulk-upload/


## Swagger
La API está documentada automáticamente con Swagger. Puedes acceder a la documentación interactiva de la API a través de la siguiente URL:
    ```bash
    http://127.0.0.1:8000/swagger/

