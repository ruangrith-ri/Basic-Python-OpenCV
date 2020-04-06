import os
import cv2

#PART FILE
path1 = os.path.join(os.path.dirname(__file__), 'img\cat1.jpg')

path_feature = os.path.join(os.path.dirname(__file__), 'haarcascades\haarcascade_frontalcatface.xml')


cat_detect = cv2.CascadeClassifier(path_feature)

frame = cv2.imread(path1)

img = frame.copy()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

rects = cat_detect.detectMultiScale(gray, scaleFactor = 1.01 ,minNeighbors = 5 , minSize=(25, 25))

for (i,(x,y,w,h)) in enumerate(rects):
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.rectangle(frame,(x,y),(x+15,y-15),(0,255,0),-1)
    cv2.putText(frame,str(i+1),(x+2,y-2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

cv2.imshow('Cat Faces',frame)

#SAVE RESULT
k = cv2.waitKey()
if k == ord('s'):
    pathExport = os.path.join(os.path.dirname(__file__), r'img\result.jpg')
    cv2.imwrite(pathExport, frame)