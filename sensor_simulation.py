import csv
import random
from datetime import datetime

filename = "sensor_data.csv"

with open(filename, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "temperature", "humidity", "motion"])

    for i in range(100):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        temperature = round(random.uniform(22, 35), 2)
        humidity = round(random.uniform(40, 70), 2)
        motion = random.choice([0, 1])

        writer.writerow([timestamp, temperature, humidity, motion])

print("Sensor data generated successfully.")
