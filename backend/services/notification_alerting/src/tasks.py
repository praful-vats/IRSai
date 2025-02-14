from celery_app import celery_app
import redis
import json

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

@celery_app.task(name="src.tasks.send_notification_task")
def send_notification_task(notification_data):
    """ Process notification and publish to Redis """
    message = notification_data["message"]
    channel = notification_data["channel"]

    redis_client.publish("notifications", json.dumps({"message": message, "channel": channel}))
    
    return {"status": "success", "message": "Notification sent via Redis"}
