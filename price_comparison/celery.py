from __future__ import absolute_import
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'price_comparison.settings')

app = Celery('price_comparison')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

# Celery Beat schedule (every 10 seconds)
app.conf.beat_schedule = {
    'check-price-drops-every-hour': {
        'task': 'priceapp.tasks.check_price_drops',
        'schedule': crontab(minute=0),  # Run every hour at minute 0
    },
}

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')