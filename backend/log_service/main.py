from fastapi import FastAPI
from routes import logs
from core.database import init_db
from core.kafka_client import kafka_producer

app = FastAPI(title="IRSai Log Ingestion Service", version="1.0.0")

# Initialize database connection
init_db()

# Include Routes
app.include_router(logs.router, prefix="/logs", tags=["Logs"])

@app.get("/health")
async def health_check():
    """Health check for Kubernetes & monitoring."""
    return {"status": "healthy"}

@app.on_event("shutdown")
async def shutdown():
    """Gracefully shutdown Kafka producer."""
    kafka_producer.close()
