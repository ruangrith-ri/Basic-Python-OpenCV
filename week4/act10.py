# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\week2\export5-1.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
width, height = img.shape[0:2]

grayImg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

moment = cv2.moments(grayImg)
X = int(moment["m10"]/moment["m00"])
Y = int(moment["m01"]/moment["m00"])
cv2.circle(img,(X,Y),15,(205,114,101),1)

# Displaying the image
cv2.imshow('Center of the Image',img)
cv2.waitKey()