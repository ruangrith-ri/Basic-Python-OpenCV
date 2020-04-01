import os
import cv2

#DEFINE FIND CONTOURS
def findContours(img,t1,t2):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edge = cv2.Canny(gray,t1,t2)
    contours,hierarchy = cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    return contours,edge

#DEFINE DRAW COUNT CONTOURS
def drawCountContours(contours,img):
    count = 0
    for c in contours:
        rect = cv2.boundingRect(c)
        x,y,w,h = rect
        count = count + 1
        cv2.rectangle(img, (x, y), (x+w, y+h), (0,255,0), 1)
        cv2.putText(img,str(count),(x,y),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),2)

    height,width = img.shape[0:2]

    cv2.rectangle(img, (0, height-20), (120, height), (0,0,0), -1)
    cv2.putText(img,'Contours : ' + str(len(contours)),(0,height-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)


#PART IMAGE
path1 = os.path.join(os.path.dirname(__file__), 'img\coin.jpg')
img = cv2.imread (path1)

#FIND CONTOURS
contours,edge = findContours(img,400,150)

#DRAW CONTOURS
cv2.drawContours(img,contours,-1,(0,0,255),2)

#DRAW COUNT CONTOURS
drawCountContours(contours,img)

#SHOW CONTOURS
cv2.imshow('Edge',edge)
cv2.imshow('Contours',img)

#SAVE RESULT
k = cv2.waitKey()
if k == ord('s'):
    pathExport = os.path.join(os.path.dirname(__file__), r'img\result.jpg')
    cv2.imwrite(pathExport, img)


