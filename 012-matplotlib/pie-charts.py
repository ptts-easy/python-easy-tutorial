import matplotlib.pyplot as plt
import numpy as np

print("============== Matplotlib Pie Charts ===================")

print("-------- Creating Pie Charts --------")

fig = plt.figure("Creating Pie Charts")

y = np.array([35, 25, 25, 15])

plt.pie(y)
plt.show()

print("-------- Labels --------")

fig = plt.figure("Labels")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.show()

print("-------- Start Angle --------")

fig = plt.figure("Start Angle")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels, startangle = 90)
plt.show()

print("-------- Explode --------")

fig = plt.figure("Explode")

import matplotlib.pyplot as plt
import numpy as np

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show()

print("-------- Shadow --------")

fig = plt.figure("Shadow")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode, shadow = True)
plt.show()

print("-------- Colors --------")

fig = plt.figure("Colors")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]
mycolors = ["black", "hotpink", "b", "#4CAF50"]

plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()

#'r' - Red
#'g' - Green
#'b' - Blue
#'c' - Cyan
#'m' - Magenta
#'y' - Yellow
#'k' - Black
#'w' - White

print("-------- Legend --------")

fig = plt.figure("Legend")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend()
plt.show() 

print("-------- Legend With Header --------")

fig = plt.figure("Legend With Header")

y = np.array([35, 25, 25, 15])
mylabels = ["Apples", "Bananas", "Cherries", "Dates"]

plt.pie(y, labels = mylabels)
plt.legend(title = "Four Fruits:")
plt.show() 