# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
width, height = img.shape[0:2]

# Displaying the image
cv2.imshow('Original Image',img)
cv2.imshow('Crpped Image',croppedImage)
cv2.waitKey()