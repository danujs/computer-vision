import cv2
import matplotlib.pyplot as plt

#Open the image
img = cv2.imread('onepiecelake.jpeg')
#Apply Canny

edges = cv2.Canny(img, 100,200, 3, L2gradient=True)
plt.figure()
plt.title('One Piece')
plt.imsave('onepiecelake.jpeg', edges, cmap='gray', format='jpeg')
plt.imshow(edges, cmap='gray')
plt.show()

# you can see the origin picture 'onepiecelake.jpeg'
# and the result 'figure 1'