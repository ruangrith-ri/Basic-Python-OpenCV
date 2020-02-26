# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\Week2 - BasicCapture\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
width, height = img.shape[0:2]

#Create Kernel
kerrnel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])

kernel_3x3 = np.ones((3,3),np.float32)/9.0
kernel_5x5 = np.ones((5,5),np.float32)/25.0
kernel_7x7 = np.ones((7,7),np.float32)/49.0

output = cv2.filter2D(img,-1,kerrnel_identity)
cv2.imshow('Identity filter',output)
output = cv2.filter2D(img,-1,kernel_3x3)
cv2.imshow('3x3 filter',output)
output = cv2.filter2D(img,-1,kernel_5x5)
cv2.imshow('5x5 filter',output)
output = cv2.filter2D(img,-1,kernel_7x7)
cv2.imshow('7x7 filter',output)

# Displaying the image
cv2.waitKey()