# celery_add.py

from celery_config import app

@app.task
def add(a, b):
    return a + b

def func(x, y):
    add.delay(x, y)    