import numpy as np
import cv2

# path
path = r'C:\Users\admin\Desktop\MDT425\Week2 - BasicCapture\geeksforgeeks.png'
path1 = r'C:\Users\admin\Desktop\MDT425\Week2 - BasicCapture\export4-1.png'

# Using cv2.imread() method
img = cv2.imread(path, 0)
cv2.imshow('image', img)
k = cv2.waitKey()

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite(path1, img)
    cv2.destroyAllWindows()
