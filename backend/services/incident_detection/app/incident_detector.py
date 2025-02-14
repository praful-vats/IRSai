import json
import redis
from app.database import incidents_collection
from app.config import REDIS_HOST, REDIS_PORT, REDIS_CHANNEL

redis_client = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)

def detect_incident(log_data):
    """
    AI/ML-based anomaly detection.
    For now, simple keyword-based detection.
    """
    alert_keywords = ["error", "failure", "critical", "exception"]
    if any(word in log_data["message"].lower() for word in alert_keywords):
        incident = {
            "log": log_data,
            "severity": "high",
            "status": "new"
        }
        incidents_collection.insert_one(incident)
        print(f"[Incident Detected] {incident}")

        # Publish alert to Redis (for notification_alerting)
        redis_client.publish(REDIS_CHANNEL, json.dumps(incident))
