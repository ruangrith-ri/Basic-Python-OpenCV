# Python program to explain cv2.imread() method 
  
# importing cv2  
import cv2

# path 
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method 
img = cv2.imread(path) 

# Displaying the image 
cv2.imshow('image', img) 
cv2.waitKey()

# Using 0 to read image in grayscale mode 
img = cv2.imread(path, 0) 
  
# Displaying the image 
cv2.imshow('image', img) 
cv2.waitKey()