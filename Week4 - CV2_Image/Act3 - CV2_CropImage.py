# importing cv2
import cv2

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

width, height = img.shape[0:2]

#Crop
startRow=int(width*.15)
startCol=int(height*.15)
endRow=int(width*.85)
endCol=int(height*.85)

croppedImage=img[startRow:endRow,startCol:endCol]

# Displaying the image
cv2.imshow('Original Image',img)
cv2.imshow('Crpped Image',croppedImage)
cv2.waitKey()