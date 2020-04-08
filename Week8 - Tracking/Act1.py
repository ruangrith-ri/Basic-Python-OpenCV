import os
import cv2
import numpy as np 

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

has_frame, frame = capture.read()

#SETUP INITIAL LOCATION WINDOWS
r = 270
h = 120
c = 540
w = 120

track_window = (c,r,w,h)

#SETUP ROI FOR TRACKING
roi = frame[r:r+h,c:c+w]

hsv_roi = cv2.cvtColor(roi,cv2.COLOR_BGR2HSV)

mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)),np.array((180., 255., 255.)))

roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0,180])

cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)

#SETUP THE TERMINATION CRITERIA, EITHER 10 ITERATION OR MOVE BY ATLEAST 1 PT

term_crit = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 2)


i = 0
while True:
    has_frame, frame = capture.read()
    i = i+1
    if not has_frame:
        print('Reached the end of the video.')
        print('Processed %d frames.'% i)
        break
        
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    dst = cv2.calcBackProject([hsv], [0], roi_hist, [0,180],  1)

    #APPLY MEANSHIFT TO GET THE NEW LOCATION
    ret, track_window = cv2.meanShift(dst, track_window, term_crit)
   
    ## print('Number of cat faces: %d'% len(rects))
    output = frame.copy()

    x,y,w,h = track_window

    cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 10)
    video.write(output)

capture.release()
video.release()