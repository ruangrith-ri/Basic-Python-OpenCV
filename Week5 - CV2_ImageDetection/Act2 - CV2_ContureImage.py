# importing cv2
import cv2
import numpy as np

# path
path = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\img\sampleImage.png'
pathHSV = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\img\HSV.png'

# Using cv2.imread() method
img = cv2.imread(path)
hsvChart = cv2.imread(pathHSV)

#rows cols
width, height = img.shape[0:2]
width, height = hsvChart.shape[0:2]

hsvImg = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
hsvChartImg = cv2.cvtColor(hsvChart,cv2.COLOR_BGR2HSV)

lower = np.array([100,200,200])
upper = np.array([135,255,255])

marking = cv2.inRange(hsvImg,lower,upper)
markingChart = cv2.inRange(hsvChartImg,lower,upper)

# Displaying the image
cv2.imshow('Image',img)
cv2.imshow('HSV',marking)
cv2.imshow('Mark Image HSV',markingChart)

cv2.waitKey()