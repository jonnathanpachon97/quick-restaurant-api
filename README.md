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

- Crear los datos de prueba:
Crear los restaurantes
    ```bash
    from restaurants.models import Restaurant

# Crear algunos restaurantes de prueba
restaurant1 = Restaurant.objects.create(
    name="Restaurant A",
    address="Address A, City",
    rating=4.5,
    status="Active",
    category="Italian",
    latitude=40.712776,
    longitude=-74.005974,
    activate=True
)

restaurant2 = Restaurant.objects.create(
    name="Restaurant B",
    address="Address B, City",
    rating=4.0,
    status="Active",
    category="Mexican",
    latitude=34.052235,
    longitude=-118.243683,
    activate=True
)

restaurant3 = Restaurant.objects.create(
    name="Restaurant C",
    address="Address C, City",
    rating=3.8,
    status="Inactive",
    category="Chinese",
    latitude=41.878113,
    longitude=-87.629799,
    activate=False
)

restaurant4 = Restaurant.objects.create(
    name="Restaurant D",
    address="Address D, City",
    rating=4.2,
    status="Active",
    category="Indian",
    latitude=51.507351,
    longitude=-0.127758,
    activate=True
)

restaurant5 = Restaurant.objects.create(
    name="Restaurant E",
    address="Address E, City",
    rating=3.9,
    status="Active",
    category="American",
    latitude=48.856613,
    longitude=2.352222,
    activate=True
)

Crear los usuarios
    ```bash
    from users.models import User

# Crear 10 usuarios de prueba
users = []
for i in range(1, 11):
    user = User.objects.create(
        first_name=f'FirstName{i}',
        last_name=f'LastName{i}',
        email=f'user{i}@example.com',
        phone=f'123-456-789{i}',
        default_address=f'Address {i}, City',
        restaurant=restaurant1 if i % 2 == 0 else restaurant2,  # Alternamos entre dos restaurantes
        typology='dealer' if i % 2 == 0 else 'customer',  # Alternamos entre "dealer" y "customer"
        active=True
    )
    users.append(user)

# Verificar que los usuarios se crearon correctamente
for user in users:
    print(user.first_name, user.email)

Crear los menu-items
    ```bash
    from menu.models import MenuItem

# Crear algunos elementos de menú de prueba
item1 = MenuItem.objects.create(name="Pizza", price=12.99)
item2 = MenuItem.objects.create(name="Tacos", price=8.99)
item3 = MenuItem.objects.create(name="Burger", price=10.99)
item4 = MenuItem.objects.create(name="Sushi", price=15.99)
item5 = MenuItem.objects.create(name="Pasta", price=11.99)

Crear las ordenes
    ```bash
    from orders.models import Order
    from datetime import datetime, timedelta

# Crear algunas órdenes de prueba
orders = []
for i, user in enumerate(users[:5]):  # Solo tomamos los primeros 5 usuarios para crear órdenes
    order = Order.objects.create(
        customer=user,
        restaurant=restaurant1 if i % 2 == 0 else restaurant2,  # Alternamos entre dos restaurantes
        total_amount=35.00,
        delivery_address=f"Delivery Address {i+1}, City",
        special_instructions="No onions" if i % 2 == 0 else "Extra spicy",
        status="Pending",
        estimated_delivery_time=datetime.now() + timedelta(hours=1)
    )
    order.items.set([item1, item2])  # Asignamos los elementos del menú (Pizza y Tacos)
    orders.append(order)

# Verificar que las órdenes se crearon correctamente
for order in orders:
    print(order.id, order.customer.first_name, order.restaurant.name)   

- Salir del Django shell:
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


## Swagger
La API está documentada automáticamente con Swagger. Puedes acceder a la documentación interactiva de la API a través de la siguiente URL:
        ```bash
    [redis-server](http://127.0.0.1:8000/swagger/)

