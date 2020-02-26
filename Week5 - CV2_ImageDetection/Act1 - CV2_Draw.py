from matplotlib import pyplot as plt
import numpy as np 
import cv2

height = 320
width = 640 

canvas = np.zeros((height,width,3),np.uint8)

cv2.circle(canvas,(100,100),20,(0,100,255),5)

CV_FILLED = -1

cv2.circle(canvas,(200,150),20,(0,255,0),CV_FILLED)
cv2.circle(canvas,(300,200),20,(255,0,0),CV_FILLED)

cv2.line(canvas,(400,50),(500,100),(255,100,0),5)

cv2.rectangle(canvas,(400,200),(500,250),(255,255,0),5)

plt.imshow(canvas)
plt.show()