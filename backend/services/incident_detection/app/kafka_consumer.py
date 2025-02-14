from kafka import KafkaConsumer
import json
from app.config import KAFKA_BROKER, KAFKA_TOPIC
from app.incident_detector import detect_incident

consumer = KafkaConsumer(
    KAFKA_TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

def consume_logs():
    """ Continuously consume logs and analyze them """
    print("[Kafka Consumer] Listening for logs...")
    for message in consumer:
        log_data = message.value
        detect_incident(log_data)
