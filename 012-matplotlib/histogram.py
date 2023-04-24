import matplotlib.pyplot as plt
import numpy as np

print("============== Matplotlib Histograms ===================")

print("-------- Create Histogram --------")

fig = plt.figure("Create Histogram")

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()