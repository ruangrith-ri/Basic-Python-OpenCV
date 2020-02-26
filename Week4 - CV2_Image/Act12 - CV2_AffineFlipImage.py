# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\Week2 - BasicCapture\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
rows,cols = img.shape[:2]

src_points = np.float32([[0,0],[cols-1,0],[0,rows-1]])
dst_points = np.float32([[cols-1,0],[0,0],[cols-1,rows-1]])

affine_matrix = cv2.getAffineTransform(src_points,dst_points)
outputImg = cv2.warpAffine(img,affine_matrix,(cols,rows))

# Displaying the image
cv2.imshow('Image',img)
cv2.imshow('Output Image',outputImg)
cv2.waitKey()