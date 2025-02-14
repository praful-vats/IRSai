import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/logs_db")
    KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")
    LOG_TOPIC = os.getenv("LOG_TOPIC", "log_topic")

config = Config()
