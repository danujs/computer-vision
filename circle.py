# circle
# cv2.circle(image, center, radius, color, fill)

# Draw a diagonal blue line of thickness of 5 pixels

image = np.zeros((512, 512, 3), np.uint8)

cv2.circle(image, (350, 350), 100, (15, 75, 50), -1)
cv2.imshhow("Circle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()
