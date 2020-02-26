import numpy as np
import cv2

img = np.zeros((200,200,3),np.uint8)

cv2.line(img,(100,10),(100,190),(0,100,255),5)
cv2.line(img,(10,100),(190,100),(0,100,255),5)

cv2.circle(img,(100,100),90,(0,100,255),5)


cv2.ellipse(img,(100,100),(50, 90), 180, 0, 360, (0,100,255), 5)
cv2.ellipse(img,(100,100),(90, 50), 180, 0, 360, (0,100,255), 5)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'HelloWorld',(20,110),font,1,(255,255,255),2)

cv2.imshow("img",img)
cv2.waitKey(0)
