import asyncio
import json
import redis.asyncio as redis
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, BackgroundTasks

app = FastAPI()

# Connect to Redis
redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

active_connections = set()  # Store active WebSocket clients


async def redis_listener():
    """ Continuously listens for new messages on the Redis Pub/Sub channel. """
    pubsub = redis_client.pubsub()
    await pubsub.subscribe("notifications")

    async for message in pubsub.listen():
        if message["type"] == "message":
            notification_data = json.loads(message["data"])
            await broadcast_notification(notification_data)


async def broadcast_notification(notification_data):
    """ Send messages to all active WebSocket clients. """
    for connection in active_connections:
        try:
            await connection.send_json(notification_data)
        except Exception as e:
            print(f"WebSocket error: {e}")
            active_connections.remove(connection)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """ WebSocket endpoint to send real-time notifications. """
    await websocket.accept()
    active_connections.add(websocket)

    try:
        while True:
            await websocket.receive_text()  # Keep connection open
    except WebSocketDisconnect:
        active_connections.remove(websocket)
    except Exception as e:
        print(f"WebSocket error: {e}")
        active_connections.remove(websocket)


@app.post("/send-notification/")
async def send_notification(background_tasks: BackgroundTasks, message: str, channel: str):
    """ Publish messages to Redis. """
    notification_data = {"message": message, "channel": channel}
    
    # Publish the message to Redis
    await redis_client.publish("notifications", json.dumps(notification_data))

    return {"status": "success", "message": "Notification queued"}


# Run the Redis listener in the background
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(redis_listener())
