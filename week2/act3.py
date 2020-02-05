import numpy as np
import cv2
from matplotlib import pyplot as plt

# path 
path = r'C:\Users\admin\Desktop\MDT425\week2\geeksforgeeks.png'

# Using cv2.imread() method 
img = cv2.imread(path) 

plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
plt.xticks([]),plt.yticks([])
plt.show()