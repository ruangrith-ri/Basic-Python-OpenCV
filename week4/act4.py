# importing cv2
import cv2

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)


width, height = img.shape[0:2]

#Rotate matrix
resizeImg = cv2.resize(img,(0,0),fx = 0.75,fy = 0.5)

# Displaying the image
cv2.imshow('Resize image', resizeImg)
cv2.waitKey()