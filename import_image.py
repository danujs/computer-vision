#Welcome to the basics of Computer Vision
#import the library
import cv2
import numpy as np

#the easiest thing to display image
input = cv2.imread('onepiecelake.jpg')
cv2.imshow('Hello World', input)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Let's take a closer look at how images are stored
print(input.shape)
