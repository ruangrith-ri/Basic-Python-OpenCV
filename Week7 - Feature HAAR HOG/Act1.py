import os
import cv2
import numpy as np 
from matplotlib import pyplot as plt 

#PART FILE
path1 = os.path.join(os.path.dirname(__file__), 'vdo\cat.mp4')
path2 = os.path.join(os.path.dirname(__file__), 'vdo\cat-feature-export.mp4')

path_feature = os.path.join(os.path.dirname(__file__), 'haarcascades\haarcascade_frontalcatface.xml')

capture = cv2.VideoCapture(path1)
output_file = path2

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(output_file,fourcc,25,(frame_width,frame_height))

cat_detect = cv2.CascadeClassifier(path_feature)

i = 0
while True:
    has_frame, frame = capture.read()
    i = i+1
    if not has_frame:
        print('Reached the end of the video.')
        print('Processed %d frames.'% i)
        break
        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects = cat_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
   
    ## print('Number of cat faces: %d'% len(rects))
    output = frame.copy()
    for (i, (x, y, w, h)) in enumerate(rects):
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 10)
        video.write(output)

capture.release()
video.release()