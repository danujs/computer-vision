# Let's add text withh cv2.putText

# cv2.putText(image, 'Text to Display', bottom left starting point, Font, Font Size, BGR Color, Thickness)

image = np.zeros((512, 512, 3), np.uint8)

cv2.putText(image, 'Hello World!', (75, 290), cv2.FONT_HERSHEY_COMPLEX, 2, (245, 161, 66), 3)
cv2.imshow("Hello World", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
