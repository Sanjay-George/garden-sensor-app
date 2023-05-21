import time
import json
import random

from kafka import KafkaProducer

def random_temp_cels():
    return round(random.uniform(-10, 50), 1)

def random_humidity():
    return round(random.uniform(0, 100), 1)

def random_wind():
    return round(random.uniform(0, 10), 1)

def random_soil():
    return round(random.uniform(0, 100), 1)

def random_location():
    return random.choice(["fulda", "kassel", "frankfurt", "münchen"])

def get_json_data():
    data = {}

    data["temperature"] = random_temp_cels()
    data["humidity"] = random_humidity()
    data["wind"] = random_wind()
    data["soil"] = random_soil()
    data["location"] = random_location()

    return json.dumps(data) 

def main():
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    for _ in range(500000):
    # for _ in range(500):
        json_data = get_json_data()
        producer.send('garden_sensor_data', bytes(f'{json_data}','UTF-8'))
        print(f"Sensor data is sent: {json_data}")
        time.sleep(0.001 / 3)


if __name__ == "__main__":
    main()