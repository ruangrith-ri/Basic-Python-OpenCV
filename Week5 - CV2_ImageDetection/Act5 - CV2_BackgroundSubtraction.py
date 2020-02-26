from matplotlib import pyplot as plt
import numpy as np 
import cv2

#FRAME DIFF
path1 = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\workshop\highway1.png'
path2 = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\workshop\highway2.png'

frame1 = cv2.imread(path1,cv2.IMREAD_COLOR)
frame2 = cv2.imread(path2,cv2.IMREAD_COLOR)

gray1 = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

frame_diff = cv2.subtract(gray1,gray2)

ret, mark = cv2.threshold(frame_diff,0,255,cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.imshow(mark,'gray')
plt.show()


#BACKGROUND SUBTRACTION
path = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\workshop\highway.mp4'
pathExport = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\workshop\highwayResult.mp4'

capture = cv2.VideoCapture(path)
output_file = (pathExport)

frame_width = int(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'XVID')
video = cv2.VideoWriter(output_file, fourcc, 25, (frame_width, frame_height))

#CREATE MODEL
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()

i = 0

while(True):
    has_frame, frame = capture.read()

    i = i + 1

    if not has_frame:
        print('Reached the end of the video.')
        print('Processed %d frames.'%i)
        break
    
    #ESTIMATE BACKGROUND
    fgmask = fgbg.apply(frame)
    out = cv2.cvtColor(fgmask,cv2.COLOR_GRAY2BGR)
    video.write(out)

capture.release()
video.release()
