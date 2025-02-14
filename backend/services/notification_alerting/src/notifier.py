from src.tasks import send_notification_task
from src.schemas import NotificationRequest

class NotificationService:
    def send_alert(self, notification: NotificationRequest):
        task = send_notification_task.apply_async(args=[notification.dict()])
        return {"task_id": task.id, "status": "queued"}
