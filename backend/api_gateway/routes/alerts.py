from fastapi import APIRouter, HTTPException, Depends
from backend.api_gateway.core.security import get_current_user
from backend.api_gateway.utils.http_clients import http_client

router = APIRouter()

@router.get("/alerts")
def get_alerts(user: dict = Depends(get_current_user)):
    return {"alerts": ["High CPU Usage", "Database Connection Failure"]}

@router.post("/alerts")
def create_alert(alert: dict, user: dict = Depends(get_current_user)):
    return {"message": "Alert created", "alert": alert}
