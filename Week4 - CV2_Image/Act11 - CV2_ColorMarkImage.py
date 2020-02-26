# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\Week2 - BasicCapture\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
width, height = img.shape[0:2]

hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

lower = np.array([0,200,0])
upper = np.array([255,255,255])

marking = cv2.inRange(hsvImg,lower,upper)

# Displaying the image
cv2.imshow('Image',img)
cv2.imshow('HSV Image',hsvImg)
cv2.imshow('Mark Image',marking)
cv2.waitKey()