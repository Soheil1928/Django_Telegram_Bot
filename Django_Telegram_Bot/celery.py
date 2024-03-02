import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Telegram_Bot.settings')
celery_app = Celery('Django_Telegram_Bot')
celery_app.config_from_object('django.conf:settings', namespace='CELERY')
celery_app.conf.timezone = 'Asia/Tehran'

celery_app.autodiscover_tasks()
