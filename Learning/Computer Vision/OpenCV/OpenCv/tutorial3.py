import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # ret lets you know if its being copied correctly
    ret, frame = cap.read()

    # Get width and Height (there are 17 different things)
    width = int(cap.get(3))
    height = int(cap.get(4))


    # Extract parts of the frame as seperate images
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)

    # Top Left
    image[:height//2, :width//2] = smaller_frame
    # Bottom Left
    image[height//2:, :width//2] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # Top Right
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.ROTATE_180)
    # Bottom Right
    image[height//2:, width//2:] = smaller_frame




    cv2.imshow('frame', image)




    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()