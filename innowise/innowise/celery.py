from celery import Celery
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'innowise.settings')

app = Celery('innowise')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
