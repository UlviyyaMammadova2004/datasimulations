import paho.mqtt.client as mqtt
import time
import random
import json
import ssl
import os

# AWS IoT endpoint and topic
broker = "a2ktg7pl1fzpok-ats.iot.eu-north-1.amazonaws.com"
port = 8883
topic = "myiot/device1/data"

# Corrected Certificate file paths
cert_path = "certs/device1.cert.pem"           # FIXED HERE
key_path = "certs/private.pem.key"
ca_path = "certs/AmazonRootCA1.pem"

# Debug: Check if paths exist
print("CERT path exists:", os.path.exists(cert_path))
print("KEY path exists:", os.path.exists(key_path))
print("CA path exists:", os.path.exists(ca_path))

# Create MQTT client
client = mqtt.Client()

# Enable TLS/SSL with TLSv1.2 explicitly
client.tls_set(
    ca_certs=ca_path,
    certfile=cert_path,
    keyfile=key_path,
    tls_version=ssl.PROTOCOL_TLSv1_2
)

# Connect to AWS IoT
client.connect(broker, port, keepalive=60)

# Loop to publish temperature data
while True:
    temperature = round(random.uniform(20, 30), 2)
    data = {
        "device_id": "device1",
        "timestamp": time.time(),
        "temperature": temperature
    }
    client.publish(topic, json.dumps(data))
    print(f"Sent to AWS IoT: {data}")
    time.sleep(2)
