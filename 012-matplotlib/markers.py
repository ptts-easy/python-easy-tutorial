import matplotlib.pyplot as plt
import numpy as np

print("============== Matplotlib Markers ===================")

print("-------- Markers --------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

plt.plot(ypoints, marker = '*')
plt.show()

print("-------- Marker Reference --------")

#y3points = []

#for x in range(30):
#  y3points.append(np.array([x, x, x]))

#y3points = [None] * 30

#for x in range(len(y3points)):
#  y3points[x] = np.array([x, x, x])

y3points = [np.array([i, i, i]) for i in range(30)]

plt.plot(y3points[1], marker = 'o')

plt.plot(y3points[2], marker = '*')

plt.plot(y3points[3], marker = '.')

plt.plot(y3points[4], marker = ',')

plt.plot(y3points[5], marker = 'x')

plt.plot(y3points[6], marker = 'X')

plt.plot(y3points[7], marker = '+')

plt.plot(y3points[8], marker = 'P')

plt.plot(y3points[9], marker = 's')

plt.plot(y3points[10], marker = 'D')

plt.plot(y3points[11], marker = 'd')

plt.plot(y3points[12], marker = 'p')

plt.plot(y3points[13], marker = 'H')

plt.plot(y3points[14], marker = 'h')

plt.plot(y3points[15], marker = 'v')

plt.plot(y3points[16], marker = '<')

plt.plot(y3points[17], marker = '>')

plt.plot(y3points[18], marker = '1')

plt.plot(y3points[19], marker = '2')

plt.plot(y3points[20], marker = '3')

plt.plot(y3points[21], marker = '4')

plt.plot(y3points[22], marker = '|')

plt.plot(y3points[23], marker = '_')

plt.show()

print("-------- Format Strings fmt --------")

print("marker|line|color")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

print("-------- Line Reference --------")

plt.plot(y3points[1], 'o-r')

plt.plot(y3points[2], 'o:r')

plt.plot(y3points[3], 'o--r')

plt.plot(y3points[4], 'o-.r')

plt.show()

print("-------- Color Reference --------")

plt.plot(y3points[1], 'o:r')

plt.plot(y3points[2], 'o:b')

plt.plot(y3points[3], 'o:b')

plt.plot(y3points[4], 'o:c')

plt.plot(y3points[5], 'o:m')

plt.plot(y3points[6], 'o:y')

plt.plot(y3points[7], 'o:k')

plt.plot(y3points[8], 'o:w')

plt.show()

print("-------- Marker Size --------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

print("-------- Marker Color --------")

plt.plot(y3points[1], marker = 'o', ms = 20)

plt.plot(y3points[2], marker = 'o', ms = 20, mec = 'r')

plt.plot(y3points[3], marker = 'o', ms = 20, mfc = 'r')

plt.plot(y3points[4], marker = 'o', ms = 20, mec = 'r', mfc = 'r')

plt.plot(y3points[5], marker = 'o', ms = 20, mec = '#4CAF50', mfc = '#4CAF50')

plt.plot(y3points[6], marker = 'o', ms = 20, mec = 'hotpink', mfc = 'hotpink')

plt.show()
