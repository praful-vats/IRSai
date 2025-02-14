from fastapi import FastAPI
from app.database import incidents_collection

app = FastAPI()

@app.get("/incidents")
def get_incidents():
    """Fetch all detected incidents."""
    incidents = list(incidents_collection.find({}, {"_id": 0}))
    return {"incidents": incidents}
