import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    AUTH_SECRET = os.getenv("AUTH_SECRET", "supersecret")
    LOG_SERVICE_URL = os.getenv("LOG_SERVICE_URL", "http://log-service:8001")
    INCIDENT_SERVICE_URL = os.getenv("INCIDENT_SERVICE_URL", "http://incident-service:8002")
    ALERT_SERVICE_URL = os.getenv("ALERT_SERVICE_URL", "http://alert-service:8003")

config = Config()
