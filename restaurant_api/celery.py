# restaurant_api/celery.py
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Asignar el nombre de la aplicación de Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_api.settings')

# Inicializar Celery con Redis como broker
app = Celery('restaurant_api', broker='redis://localhost:6379/0')

# Usar la configuración predeterminada de Celery para los resultados
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodiscovery de tareas en todas las apps registradas en INSTALLED_APPS
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))