from matplotlib import pyplot as plt
import numpy as np
import cv2

path = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\video\ball_tracking.mp4'
pathExport = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\video\ball_tracking_Result.mp4'

capture = cv2.VideoCapture(path)
output_file = (pathExport)

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')

video = cv2.VideoWriter(output_file,fourcc,25,(frame_width,frame_height))

i = 0
while True:
    has_frame,frame = capture.read()

    i = i+1

    if not has_frame:
        print('Reached the end of the video.')
        print('Processed %d frames.'%i)
        break
        
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lower_color = np.array([29,86,6])
    upper_color = np.array([64,255,255])

    mask = cv2.inRange(hsv,lower_color,upper_color)

    res = cv2.bitwise_and(frame, frame, mask = mask)

    video.write(res)

capture.release()
video.release()