import redis
import os

redis_client = redis.Redis(host=os.getenv("REDIS_HOST", "localhost"), port=6379, db=0)

def set_cache(key: str, value: str, expire: int = 3600):
    redis_client.setex(key, expire, value)

def get_cache(key: str):
    return redis_client.get(key)