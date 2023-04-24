import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
import shutil

"""
print("============== Getting Started ===================")

print("-------- Reading an image in OpenCV using Python --------")

print("---- Example #1 (Using OpenCV) : ----")

# To read image from disk, we use
# cv2.imread function, in below method,
img = cv2.imread("geeks.png", cv2.IMREAD_COLOR)

# Creating GUI window to display an image on screen
# first Parameter is windows title (should be in string format)
# Second Parameter is image array
cv2.imshow("image", img)

# To hold the window on screen, we use cv2.waitKey method
# Once it detected the close input, it will release the control
# To the next line
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
cv2.waitKey(0)

# It is for removing/deleting created GUI window from screen
# and memory
cv2.destroyAllWindows()

print("---- Example#2 : ----")

img=cv2.imread("geeks.png")
#Displaying image using plt.imshow() method
plt.imshow(img)

#hold the window
plt.waitforbuttonpress()
plt.close('all')

print("---- Example#3 : ----")

img=cv2.imread("geeks.png")

# Converting BGR color to RGB color format
RGB_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#Displaying image using plt.imshow() method
plt.imshow(RGB_img)

# hold the window
plt.waitforbuttonpress()
plt.close('all')

print("---- Example #4: Opening in grayscale mode ----")

# path
path = r'geeks.png'

# Using cv2.imread() method
# Using 0 to read image in grayscale mode
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

# Displaying the image
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("-------- Display an image in OpenCV using Python --------")

print("---- Example #1 : ----")

# path
path = r'geeksforgeeks.png'

# Reading an image in default mode
image = cv2.imread(path)

# Window name in which image is displayed
window_name = 'image'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()

print("---- Example #2 : ----")

# path
path = r'geeksforgeeks.png'

# Reading an image in grayscale mode
image = cv2.imread(path, 0)

# Window name in which image is displayed
window_name = 'image'

# Using cv2.imshow() method
# Displaying the image
cv2.imshow(window_name, image)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
"""
"""
from google.colab.patches import cv2_imshow

window_name = "Image"

cv2_imshow(img) # Pay special attention to "_" (underscore)
"""

print("-------- Writing an image in OpenCV using Python --------")

print("---- Example #1 : ----")

# Image path
image_path = r'geeks.png'

# Image directory
directory = r'./GeeksforGeeks'

# Using cv2.imread() method
# to read the image
img = cv2.imread(image_path)

shutil.rmtree(directory)

os.mkdir(directory)

# Change the current directory
# to specified directory
os.chdir(directory)

# List files and directories
print("Before saving image:")

print(os.listdir("./"))

# Filename
filename = 'savedImage.jpg'

# Using cv2.imwrite() method
# Saving the image
cv2.imwrite(filename, img)

# List files and directories
print("After saving image:")
print(os.listdir("./"))

print('Successfully saved')

print("-------- OpenCV | Saving an Image --------")

print("---- Example #1 : ----")