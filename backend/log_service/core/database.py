from pymongo import MongoClient
from core.config import config

client = MongoClient(config.MONGO_URI)
db = client.logs_db
log_collection = db.logs

def init_db():
    """Ensures indexes are set on startup."""
    log_collection.create_index("timestamp")
