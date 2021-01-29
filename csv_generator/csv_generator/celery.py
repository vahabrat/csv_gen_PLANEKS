from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
#from .settings import BROKER_URL

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'csv_generator.settings')

#app = Celery('csv_generator', broker='redis://redis:6379/0')
app = Celery('csv_generator')
# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')
# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

#@app.task(bind=True)
#def debug_task(self):
#    print(f'Request: {self.request!r}')