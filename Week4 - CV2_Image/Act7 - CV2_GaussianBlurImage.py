# importing cv2
import cv2

# path
path = r'C:\Users\admin\Desktop\MDT425\Week2 - BasicCapture\geeksforgeeks.png'

# Using cv2.imread() method
img = cv2.imread(path)

#rows cols
width, height = img.shape[0:2]

#Guessian Blur
blurImg = cv2.GaussianBlur(img,(3,3),0)
cv2.imshow('3x3 filter',blurImg)

blurImg = cv2.GaussianBlur(img,(5,5),0)
cv2.imshow('5x5 filter',blurImg)

blurImg = cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('7x7 filter',blurImg)

cv2.imshow('Identity filter',img)
cv2.waitKey()