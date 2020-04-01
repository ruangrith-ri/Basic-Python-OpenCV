import numpy as np
import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print()
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print()
        break

    hsvImg = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #marking
    lower = np.array([0,150,150])
    upper = np.array([15,255,255])

    marking = cv2.inRange(hsvImg,lower,upper)
    #endMarking

    #cv.imshow('HSVframe', hsvImg)
    #cv.imshow('RGBframe', frame)
    cv2.imshow('Markframe', marking)

    #exampleImg
    pathHSV = r'C:\Users\admin\Desktop\MDT425\Week5 - CV2_ImageDetection\img\HSV.png'
    hsvChart = cv2.imread(pathHSV)

    width, height = hsvChart.shape[0:2]
    hsvChartImg = cv2.cvtColor(hsvChart,cv2.COLOR_BGR2HSV)
    markingChart = cv2.inRange(hsvChartImg,lower,upper)

    cv2.imshow('HSV',markingChart)
    cv2.imshow('Mark Image HSV',hsvChart)
    #endExample

    k = cv2.waitKey(1)

    if k == ord('q'):
        break

cap.release()
cv.destroyAllWindows()