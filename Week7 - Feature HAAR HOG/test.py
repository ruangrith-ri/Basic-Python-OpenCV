from matplotlib import pyplot as plt
import cv2
import os
import numpy as np

capture = cv2.VideoCapture(('cat.mp4'))
output_file = ('cat1.avi')

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(output_file,fourcc,25,(frame_width,frame_height))

cat_detect = cv2.CascadeClassifier ('haarcascades\haarcascade_frontalcatface.xml')

i = 0
while True:
    has_frame,frame = capture.read()
    i = i + 1
    if not has_frame:
        print('Reached the end of the video')
        print('Processed %d frames.'%i)
        break
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    rects = cat_detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))
    output = frame.copy()
    for(i,(x,y,w,h)) in enumerate(rects):
        cv2.rectangle(output,(x,y),(x+w,y+h),(0,255,0),10)
        video.write(output)
capture.release()
video.release()