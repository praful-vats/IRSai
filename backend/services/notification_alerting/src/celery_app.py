from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")

celery_app = Celery(
    "notification_alerting",
    broker=redis_url,
    backend=redis_url
)

celery_app.conf.update(
    task_routes={
        "src.tasks.send_notification_task": {"queue": "notifications"},
    }
)
