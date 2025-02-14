from sqlalchemy import Column, Integer, String, DateTime, func
from backend.services.database_service.database import Base

class Incident(Base):
    __tablename__ = "incidents"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=func.now())
