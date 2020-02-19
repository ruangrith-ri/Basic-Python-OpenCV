# importing cv2
import cv2

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

#find data type
print(type(img))

#show size
print(img.shape[0:2])

# Displaying the image
cv2.imshow('image', img)
cv2.waitKey()