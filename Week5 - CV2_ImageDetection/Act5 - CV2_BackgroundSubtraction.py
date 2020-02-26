from matplotlib import pyplot as plt
import numpy as np 
import cv2

path1 = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\workshop\highway1.png'
path2 = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\workshop\highway2.png'

frame1 = cv2.imread(path1,cv2.IMREAD_COLOR)
frame2 = cv2.imread(path2,cv2.IMREAD_COLOR)

gray1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

frame_diff = cv2.subtract(gray1,gray2)

ret, mark = cv2.threshold(frame_diff,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.imshow(mark,'gray')
plt.show()