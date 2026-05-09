import numpy as np
import matplotlib.pyplot as plt

# Generate 1000 random temperatures between 20 and 40 degrees
temps = np.random.normal(30, 5, 1000)

plt.hist(temps, bins=20, color='skyblue', edgecolor='black')
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.show()