from matplotlib import pyplot as plt
import numpy as np 
import cv2

height = 320
width = 640 

canvas = np.zeros((height,width,3),np.uint8)

cv2.circle(canvas,(100,100),90,(0,100,255),5)

plt.imshow(canvas)
plt.show()