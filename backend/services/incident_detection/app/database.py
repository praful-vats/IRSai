from pymongo import MongoClient
from app.config import MONGO_URI, MONGO_DB

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]
incidents_collection = db["incidents"]
