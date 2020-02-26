import numpy as np
import cv2 as cv

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print()
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print()
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.imshow('frame', gray)

    k = cv.waitKey(1)

    if k == ord('q'):
        break
    elif k == ord('s'):
        path1 = r'C:\Users\admin\Desktop\MDT425\week2\export5-1.png'
        cv.imwrite(path1, frame)

cap.release()
cv.destroyAllWindows()
