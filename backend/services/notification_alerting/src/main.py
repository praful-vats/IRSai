from fastapi import FastAPI, Depends
from src.notifier import NotificationService
from src.schemas import NotificationRequest

app = FastAPI()

notification_service = NotificationService()

@app.post("/send-notification/")
async def send_notification(notification: NotificationRequest):
    return notification_service.send_alert(notification)
