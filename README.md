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
