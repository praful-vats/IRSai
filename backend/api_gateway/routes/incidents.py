from fastapi import APIRouter


router = APIRouter()

@router.get("/incidents")
def get_incidents():
    return {"incidents": ["Server Down", "High Latency"]}

@router.post("/incidents")
def create_incident(incident: dict):
    return {"message": "Incident reported", "incident": incident}