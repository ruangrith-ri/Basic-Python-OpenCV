from matplotlib import pyplot as plt
import cv2
import os
import numpy as np

#PART IMAGE
path1 = r'C:\Users\Jeeno\source\repos\python-CV-basic\Week6 - Morphology\img\coin.jpg'

gray_image = cv2.imread(path1,0)
thresh_val,thresh = cv2.threshold(gray_image,0,255,cv2.THRESH_OTSU)
plt.axis('off')
plt.imshow(thresh,'gray')
plt.show()
