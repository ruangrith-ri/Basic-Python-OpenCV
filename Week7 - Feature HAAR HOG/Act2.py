import os
import cv2

#PART FILE
path1 = os.path.join(os.path.dirname(__file__), 'img\cat1.jpg')

path_feature = os.path.join(os.path.dirname(__file__), 'haarcascades\haarcascade_frontalcatface.xml')

frame = cv2.imread(path1,cv2.IMREAD_COLOR)

img = frame.copy()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

cat_detect = cv2.CascadeClassifier(path_feature)

rects = cat_detect.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=5, minSize=(50, 50))

for (i,(x,y,w,h)) in enumerate(rects):
    cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.rectangle(frame,(x,y),(x+15,y-15),(0,255,0),-1)
    cv2.putText(frame,str(i+1),(x+2,y-2),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,0,0),2)

cv2.imshow('Cat Faces',frame)
cv2.waitKey()