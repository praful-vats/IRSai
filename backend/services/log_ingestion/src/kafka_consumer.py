from kafka import KafkaConsumer
from backend.common.logging_config import get_logger

logger = get_logger("KafkaConsumer")

consumer = KafkaConsumer(
    'incident_logs',
    bootstrap_servers=[KAFKA_BROKER],
    auto_offset_reset='earliest',
    enable_auto_commit=True
)

def consume_logs():
    for message in consumer:
        logger.info(f"Received log: {message.value}")