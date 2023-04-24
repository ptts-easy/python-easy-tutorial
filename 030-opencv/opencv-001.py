import cv2

print("============== OpenCV Environment ===================")

print("-------- Installation of OpenCV --------")

print("pip install opencv-python")

print("-------- Checking OpenCV Version --------")

print(cv2.__version__)

print("============== Introduction to OpenCV ===================")

print("-------- Reading an image --------")

# Reading the image using imread() function
image = cv2.imread('road.jpg')
  
# Extracting the height and width of an image
h, w = image.shape[:2]
# Displaying the height and width
print("Height = {},  Width = {}".format(h, w))

cv2.imshow('image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("-------- Extracting the RGB values of a pixel --------")

# Extracting RGB values. 
# Here we have randomly chosen a pixel
# by passing in 100, 100 for height and width.
(B, G, R) = image[100, 100]
  
# Displaying the pixel values
print("R = {}, G = {}, B = {}".format(R, G, B))
  
# We can also pass the channel to extract 
# the value for a specific channel
B = image[100, 100, 0]
print("B = {}".format(B))

print("-------- Extracting the Region of Interest (ROI) --------")

# We will calculate the region of interest 
# by slicing the pixels of the image
roi = image[100 : 500, 200 : 700]

cv2.imshow('image', roi)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("-------- Resizing the Image --------")

# resize() function takes 2 parameters, 
# the image and the dimensions
resize = cv2.resize(image, (800, 800))

# Calculating the ratio
ratio = 800 / w
  
# Creating a tuple containing width and height
dim = (800, int(h * ratio))
  
# Resizing the image
resize_aspect = cv2.resize(image, dim)

cv2.imshow('image', resize_aspect)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("-------- Rotating the Image --------")

# Calculating the center of the image
center = (w // 2, h // 2)
  
# Generating a rotation matrix
matrix = cv2.getRotationMatrix2D(center, -45, 1.0) 
  
# Performing the affine transformation
rotated = cv2.warpAffine(image, matrix, (w, h))

cv2.imshow('image', rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("-------- Drawing a Rectangle --------")

# We are copying the original image, 
# as it is an in-place operation.
output = image.copy()
  
# Using the rectangle() function to create a rectangle.
rectangle = cv2.rectangle(output, (1500, 900), (600, 400), (255, 0, 0), 2)

cv2.imshow('image', rectangle)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("-------- Displaying text --------")

# Copying the original image
output = image.copy()
  
# Adding the text using putText() function
text = cv2.putText(output, 'OpenCV Demo', (500, 550), cv2.FONT_HERSHEY_SIMPLEX, 4, (255, 0, 0), 2)

cv2.imshow('image', text)
cv2.waitKey(0)
cv2.destroyAllWindows()