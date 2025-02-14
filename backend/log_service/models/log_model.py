from pydantic import BaseModel
from datetime import datetime

class LogSchema(BaseModel):
    service: str
    level: str  # INFO, WARN, ERROR
    message: str
    timestamp: datetime = datetime.utcnow()
