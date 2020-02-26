# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\export5-1.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
width, height = img.shape[0:2]

yuvImg = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
rgbImg = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

# Displaying the image
cv2.imshow('YUV Image',yuvImg)
cv2.imshow('RGB Image',rgbImg)
cv2.waitKey()