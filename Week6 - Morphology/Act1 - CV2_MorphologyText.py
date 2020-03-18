import numpy as np 
import cv2

#PART IMAGE
path1 = r'C:\Users\Jeeno\source\repos\python-CV-basic\Week6 - Morphology\img\input.PNG'

#
img = cv2.imread(path1,0)
kernel = np.ones((5,5),np.uint8)


img_erosion = cv2.erode(img,kernel,iterations=1)
img_dilation = cv2.dilate(img,kernel,iterations=1)

cv2.imshow('input',img)
cv2.imshow('erosion',img_erosion)
cv2.imshow('dilation',img_dilation)

cv2.waitKey()