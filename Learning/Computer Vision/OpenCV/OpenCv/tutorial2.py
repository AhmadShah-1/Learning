import cv2
import random


# The image is stored as a numpy array
img = cv2.imread('assets/logo.jpg', -1)

# Height, Width, Channels (color)
print(img.shape)

# First row
print(img[0])

# Looking at pixels 45 to 400 at row 257
print(img[257][45:400])


# for the first 100 rows, for the width of the image j
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]



# Copy part of an image and paste it somewhere else on the original image
# from rows 500 to 700 and columns 600 to 900
tag = img[500:700, 600:900]
img[100:300, 650:950] = tag


cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindow()