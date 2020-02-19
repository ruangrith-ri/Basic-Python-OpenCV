# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\export5-1.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
width, height = img.shape[0:2]

edgeImg = cv2.Canny(img,100,200)
cv2.imshow('edge Image',edgeImg)
edgeImg = cv2.Canny(img,200,200)
cv2.imshow('edge Image2',edgeImg)

# Displaying the image
cv2.imshow('Original Image',img)
cv2.waitKey()