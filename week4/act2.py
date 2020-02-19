# importing cv2
import cv2

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

width = 225
height = 225

#Rotate matrix
rotationMatrix = cv2.getRotationMatrix2D((width/2,height/2),120,1)
rotatedImg = cv2.warpAffine(img,rotationMatrix,img.shape[0:2])

# Displaying the image
cv2.imshow('Rotate image', rotatedImg)
cv2.waitKey()