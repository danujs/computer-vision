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

"""In addition, shape gives the dimensions of the image array. 
To find out the height and width, use shape[]"""
print ('Height of Image:', int(input.shape[0]),'pixels')
print ('Width of Image:', int(input.shape[1]), 'pixels')

#We can save the image file we edit and rename it
cv2.imwrite('output.jpg', input)
cv2.imwrite('output.png', input)
