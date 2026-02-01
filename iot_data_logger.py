import csv
import random
from datetime import datetime

with open("sensor_data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "Temperature", "Humidity"])
    for _ in range(10):
        writer.writerow([datetime.now(), random.randint(20,30), random.randint(40,60)])

print("Sensor data logged to sensor_data.csv")
