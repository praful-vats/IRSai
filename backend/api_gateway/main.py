from fastapi import FastAPI
from core.middleware import setup_middleware
from routes import logs, incidents, alerts, auth

app = FastAPI(title="IRSai API Gateway", version="1.0.0")

# Setup Middleware (Logging, Rate Limiting, Circuit Breaker)
setup_middleware(app)

# Include Routes
app.include_router(auth.router, prefix="/auth", tags=["Auth"])
app.include_router(logs.router, prefix="/logs", tags=["Logs"])
app.include_router(incidents.router, prefix="/incidents", tags=["Incidents"])
app.include_router(alerts.router, prefix="/alerts", tags=["Alerts"])

@app.get("/health")
async def health_check():
    """Health check for Kubernetes & monitoring."""
    return {"status": "healthy"}
