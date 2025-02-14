from fastapi import APIRouter, HTTPException, Depends
from core.database import log_collection
from core.kafka_client import send_log_to_kafka
from models.log_model import LogSchema

router = APIRouter()

@router.post("/")
async def ingest_log(log: LogSchema):
    """Ingest logs into MongoDB and Kafka."""
    log_dict = log.dict()
    
    # Store log in MongoDB
    log_collection.insert_one(log_dict)

    # Stream log to Kafka
    send_log_to_kafka(log_dict)

    return {"message": "Log stored successfully"}

@router.get("/")
async def get_logs(limit: int = 10):
    """Retrieve logs from MongoDB."""
    logs = list(log_collection.find().sort("timestamp", -1).limit(limit))
    if not logs:
        raise HTTPException(status_code=404, detail="No logs found")
    return logs
