import time
import redis
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from core.config import config
from fastapi.responses import JSONResponse

redis_client = redis.Redis.from_url(config.REDIS_URL)

class RateLimiterMiddleware(BaseHTTPMiddleware):
    """Middleware for API rate limiting using Redis."""
    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        key = f"ratelimit:{client_ip}"
        count = redis_client.get(key)

        if count and int(count) > 50:
            return JSONResponse(status_code=429, content={"message": "Rate limit exceeded"})
        
        redis_client.incr(key)
        redis_client.expire(key, 60)
        
        return await call_next(request)

def setup_middleware(app):
    app.add_middleware(RateLimiterMiddleware)
