import os
from kafka import KafkaConsumer
from backend.common.logging_config import get_logger

logger = get_logger("KafkaConsumer")

# Fetch Kafka broker from environment variables
KAFKA_BROKER = os.getenv("KAFKA_BROKER", "kafka:9092")

# Create Kafka consumer
consumer = KafkaConsumer(
    'incident_logs',
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

def consume_logs():
    logger.info("Starting Kafka log consumer...")
    for message in consumer:
        logger.info(f"Received log: {message.value}")

if __name__ == "__main__":
    consume_logs()
