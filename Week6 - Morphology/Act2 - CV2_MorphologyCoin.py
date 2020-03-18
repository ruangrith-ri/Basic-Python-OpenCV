from matplotlib import pyplot as plt
import cv2
import numpy as np

#PART IMAGE
path1 = r'C:\Users\Jeeno\source\repos\python-CV-basic\Week6 - Morphology\img\coin.jpg'

#Threshold
img = cv2.imread(path1,0)
thresh_val,img_thresh = cv2.threshold(img,0,255,cv2.THRESH_OTSU)

#EROSION
se = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_erosion =cv2.erode(img_thresh,se,iterations=1)

#DILATION
se = cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
img_dilation =cv2.dilate(img_thresh,se,iterations=1)

cv2.imshow('input',img_thresh)
cv2.imshow('erosion',img_erosion)
cv2.imshow('dilation',img_dilation)

cv2.waitKey()