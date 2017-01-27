# celery_config.py

from celery import Celery

app = Celery('celery_config',
             broker='redis://10.20.20.13:6379/0',
             include=['pack.celery_fetch', 'pack.celery_add'])