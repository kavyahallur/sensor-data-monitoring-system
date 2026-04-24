import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("sensor_data.csv")

plt.figure(figsize=(10, 5))
plt.plot(data["temperature"], label="Temperature")
plt.plot(data["humidity"], label="Humidity")
plt.title("Sensor Data Monitoring")
plt.xlabel("Sample Number")
plt.ylabel("Sensor Values")
plt.legend()
plt.grid(True)
plt.show()

print("Motion Detection Summary:")
print(data["motion"].value_counts())
