import os
import json
import time
from confluent_kafka import Producer

# Sample JSON data
sample_json = {
    "event_id": "c4c8d4rt-a4b0-7de9-br68-5e3ec7xs92y6",
    "event_timestamp": "2025-01-20T16:18:08.868123",
    "event_type": "UserTestEvent",
    "transaction": {
        "first_payment": "200",
        "total_transaction_amount": 1000,
        "transaction_refunds": ["100", "200"],
    },
    "user": {
        "phone_number": "123456789",
        "user_id": "abcd",
        "address": {
            "city": "Delhi",
            "country": "India",
            "country_code": "IN",
            "metadata": {
                "address_tag": "Near my village",
                "email": "abc@mail.com"
            }
        }
    },
    "cartDetails": [
        {
            "item": "Phone charger",
            "value": 25,
            "quantity": 2,
            "metadata": {
                "tax_applicable": true
            }
        },
        {
            "item": "TShirt",
            "value": 50,
            "quantity": 10,
            "metadata": {
                "tax_applicable": false
            }
        }
    ],
    "api_errors": ["No errors", "200 status code"],
    "session": {
        "pages_viewed": [
            "homepage",
            "offers"
        ],
        "session_length_in_seconds": 50.5,
        "total_pages_viewed": 6
    },
    "event_version": "1.0.2"
}

# Delivery report function
def delivery_report(err, msg):
    if err is not None:
        print(f"Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

# Function to produce events to Kafka
def produce_event_kafka():
    producer = Producer({'bootstrap.servers': 'kafka:9092'})  # Docker service name
    kafka_data = json.dumps(sample_json)  # Serialize to JSON string
    print('Serialized data to json')
    try:
        producer.produce('topic_events_data', key=None, value=kafka_data, callback=delivery_report)
        producer.flush()
        print('Data published to Kafka')
    except Exception as e:
        print(e)

if __name__ == "__main__":
    while True:
        produce_event_kafka()
        time.sleep(10)  # Wait for 5 seconds before sending the next message
