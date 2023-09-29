#Let's now explore looking at individual channels in an RGB image
#> OpenCV's split function splits the image into each color index

import cv2
import numpy as np

image = cv2.imread('onepeacelake.jpeg')

B, G, R = cv2.split(image)

print (B.shape)

cv2.imshow("Red", R)
cv2.imshow("Green", G)
cv2.imshow("Blue", B)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Let's remake the original image,
merged= cv2.merge([B, G, R])
cv2.imshow("Merged", merged)

# Let's amplify the blue color
merged = cv2.merge([B+100, G, R])
cv2.imshow("Merged with Blue Amplified", merged)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Let's create a matrix of Zeros
# with dimensions of the image h x w


zeros = np.zeros(image.shape[:2], dtype= "uint8")

cv2.imshow("Red", cv2.merge([zeros, zeros, R])
cv2.imshow("Green", cv2.merge([zeros, G, zeros]))
cv2.imshow("Blue", cv2.merge([B, zeros, zeros]))

cv2.waitKey(0)
cv2.destroyAllWindows()
           
