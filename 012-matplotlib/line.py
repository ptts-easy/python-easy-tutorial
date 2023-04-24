import matplotlib.pyplot as plt
import numpy as np

print("============== Matplotlib Line ===================")

print("-------- Linestyle --------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linestyle = 'dotted')
plt.show()

plt.plot(ypoints, linestyle = 'dashed')
plt.show()

print("-------- Shorter Syntax --------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, ls = ':')
plt.show()

print("-------- Line Styles --------")

ypoints_1 = np.array([1, 1, 1])
ypoints_2 = np.array([2, 2, 2])
ypoints_3 = np.array([3, 3, 3])
ypoints_4 = np.array([4, 4, 4])
ypoints_5 = np.array([5, 5, 5])

plt.plot(ypoints_1, ls = '-') #'solid'
plt.show()

plt.plot(ypoints_2, ls = ':') #'dotted'
plt.show()

plt.plot(ypoints_3, ls = '--') #'dashed'
plt.show()

plt.plot(ypoints_4, ls = '-.') #'dashdot'
plt.show()

plt.plot(ypoints_5, ls = '') #'None'
plt.show()

print("-------- Line Color --------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

plt.plot(ypoints, c = '#4CAF50')
plt.show()

plt.plot(ypoints, c = 'hotpink')
plt.show()

print("-------- Line Width --------")

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

print("-------- Multiple Lines --------")

y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)

plt.show()

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
