import httpx
from fastapi import APIRouter, HTTPException
from typing import List

router = APIRouter()

LOG_SERVICE_URL = "http://log-service:8002"  # Update as per `docker-compose.yml`

@router.post("/logs")
async def forward_create_log(log: dict):
    """Forward log ingestion to log_service."""
    async with httpx.AsyncClient() as client:
        response = await client.post(f"{LOG_SERVICE_URL}/", json=log)  # Log ingestion endpoint
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to store log")
    return response.json()

@router.get("/logs", response_model=List[dict])
async def forward_get_logs():
    """Forward log retrieval request to log_service."""
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{LOG_SERVICE_URL}/")  # Log retrieval endpoint
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Failed to fetch logs")
    return response.json()
