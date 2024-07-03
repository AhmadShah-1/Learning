import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # ret lets you know if its being copied correctly
    ret, frame = cap.read()

    # Get width and Height (there are 17 different things)
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Top Left of screen is 0,0
    # Increasing x makes it go right, and increasing y makes it go down
    img = cv2.line(frame, (0,0), (width, height), (255, 0, 0), 10)
    img = cv2.line(img, (0,height), (width, 0), (0, 255, 0), 10)

    # Center position, radius, color, line thickness (-1 is fill line)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)

    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)

    font = cv2.FONT_HERSHEY_SIMPLEX
    img = cv2.putText(img, 'The great chariot!', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    cv2.imshow('frame', img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()