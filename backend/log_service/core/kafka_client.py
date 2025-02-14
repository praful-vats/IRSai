from kafka import KafkaProducer
import json
from core.config import config

kafka_producer = KafkaProducer(
    bootstrap_servers=config.KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

def send_log_to_kafka(log):
    """Send log data to Kafka for AI processing."""
    kafka_producer.send(config.LOG_TOPIC, log)
