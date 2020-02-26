# importing cv2
import cv2
import numpy

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)


width, height = img.shape[0:2]

#Contrast
contrastImg = cv2.addWeighted(img,2.5,numpy.zeros(img.shape,img.dtype),0,0)

# Displaying the image
cv2.imshow('contrastImg', contrastImg)
cv2.waitKey()