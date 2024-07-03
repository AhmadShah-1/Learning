import cv2

img = cv2.imread("assets/logo.jpg", -1)

# Resize
# img = cv2.resize(img, (400, 400))
# Resize half the size of original
img = cv2.resize(img, (0, 0), fx = 0.5, fy = 0.5)

img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
cv2.imwrite('new_image.jpg', img)


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindow()