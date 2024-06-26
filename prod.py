from kafka import KafkaProducer
import json
import time

def create_large_message(num_keys):
    """Create a large message with the specified number of keys."""
    message = {f"key_{i}": f"value_{i}" for i in range(num_keys)}
    message["epoch_time"] = round(time.time() * 1000)
    return json.dumps(message).encode('utf-8')

def produce_large_message(broker, topic, id):
    """Produce a large message with many keys to a Kafka topic."""
    producer = KafkaProducer(bootstrap_servers=broker)

    try:
        message = json.dumps({"ID": str(id)}).encode('utf-8')
        future = producer.send(topic, message)
        result = future.get(timeout=60)  # Wait up to 60 seconds for the message to be sent
        print(f"Message sent to topic {topic}: {result}")
    except Exception as e:
        print(f"Failed to send message: {e}")
    finally:
        producer.close()

if __name__ == "__main__":
    # Configuration
    kafka_broker = 'localhost:9092'  # Update with your Kafka broker address
    kafka_topic = 'topic1'       # Update with your Kafka topic name
    num_keys = 10                 # Number of keys in the message

    for i in range(10000):
        produce_large_message(kafka_broker, kafka_topic, i)

