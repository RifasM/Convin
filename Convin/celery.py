import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Convin.settings')

app = Celery('Convin',
             backend='rpc://',
             broker='pyamqp://', )

app.config_from_object('django.conf:settings', namespace='CELERY', )

app.conf.update(result_expires=3600,
                enable_utc=True,
                timezone='Asia/Kolkata', )

app.conf.beat_schedule = {
    "every day at 5 PM": {
        "task": "Send_Emails_Everyday",
        "schedule": crontab(hour=17,
                            minute=0,
                            )
    },
    "every Week on Monday": {
        "task": "Send_Emails_Every_Week",
        'schedule': crontab(minute=0,
                            hour=0,
                            day_of_week="monday")
    },
    "every first day of Month": {
        "task": "Send_Emails_Every_Month",
        'schedule': crontab(minute=0,
                            hour=0,
                            day_of_month=1)
    }
}

app.autodiscover_tasks()
