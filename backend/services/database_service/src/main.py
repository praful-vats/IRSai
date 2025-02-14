from fastapi import FastAPI, Depends
from backend.services.database_service.src.db import SessionLocal
from backend.services.database_service.src.models import Incident

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/incidents/")
def read_incidents(db=Depends(get_db)):
    return db.query(Incident).all()
