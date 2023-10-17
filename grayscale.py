#=================== Step 1 =======================
# Let's convert our color image to grayscale
import cv2

# Load our input image
image = cv2.imread('onepiecelake.jpeg')
cv2.imshow('original', image)
cv2.waitKey()

# We use cvtColor, to convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.imshow('Grayscale', gray_image)
cv2.waitKey()
cv2.destroyAllWindows()

#====================== Step 2 ===================
# Another faster method to make a grayscale image
import cv2

# load our input image
img = cv2.imread('onepiecelake.jpeg', 0)
cv2.imshow('original', img)
cv2.waitKey()
cv2.destroyAllWindows()

#======================= Step 3 =================
# Let's look at the individual color levels for the first pixel(0,0)
# Find out BGR Values for the first 0, 0 pixel
import cv2
import numpy as np
image = cv2.imread('onepiecelake.jpeg')
B, G, R = image[20, 70]
print (B, G, R)
print (image.shape)

#Let's see what happens when we convert it to grayscale
#it changes to 2 dimensional array, with one value: while previously was 3D)
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print (gray_img.shape)
print (gray_img[10, 50])

