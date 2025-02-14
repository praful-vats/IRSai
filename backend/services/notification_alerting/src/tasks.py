from celery_app import celery_app
from src.slack_alert import send_slack_alert
from src.email_alert import send_email_alert

@celery_app.task(name="src.tasks.send_notification_task")
def send_notification_task(notification_data):
    message = notification_data["message"]
    channel = notification_data["channel"]
    recipient = notification_data["recipient"]

    if channel == "slack":
        return send_slack_alert(message, recipient)
    elif channel == "email":
        return send_email_alert(message, recipient)
    else:
        return {"status": "error", "message": "Invalid notification channel"}
