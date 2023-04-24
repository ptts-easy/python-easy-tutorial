import matplotlib
import matplotlib.pyplot as plt
import numpy as np

print("============== Matplotlib Getting Started ===================")

print("-------- Installation of Matplotlib --------")

print("pip install matplotlib")

print("-------- Checking Matplotlib Version --------")

print(matplotlib.__version__)

print("============== Matplotlib Pyplot ===================")

print("-------- Pyplot --------")

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()

print("============== Matplotlib Plotting ===================")

print("-------- Plotting x and y points --------")

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()

print("-------- Plotting Without Line --------")

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints, 'o')
plt.show()

print("-------- Multiple Points --------")

xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

plt.plot(xpoints, ypoints)
plt.show()

print("-------- Default X-Points --------")

ypoints = np.array([3, 8, 1, 10, 5, 7])

plt.plot(ypoints)
plt.show()
