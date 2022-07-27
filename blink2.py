import time
import cv2
from time import sleep
import numpy as np
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
from cvzone.PlotModule import LivePlot

start = time.time()
seconds = 0
temp = start - 1
# your code
stop = time.time()


cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces=1)
plotY = LivePlot(640, 360, [20, 50], invert=True)

idList = [22, 23, 24, 26, 110, 157, 158, 159, 160, 161, 130, 243]
ratioList = []
blinkCounter = 0
counter = 0
color = (255, 0, 255)
nk = 0

while True:

        
    start = time.time()
    if int(start) > int(temp):
        #print("The time of the run:",  int(start) )
        temp = temp + 1
        print(seconds)
        seconds = seconds + 1
        nk = nk + 1

    if  nk >= 10 :
        blank_image = 255*np.ones(shape=[100, 120, 3], dtype=np.uint8)
        nk = 0
    # print(blank_image.shape)
        while(1):
            cv2.imshow("Black Blank", blank_image)
            cv2.waitKey(500)
            cv2.destroyAllWindows()
        
            sleep(0.2)
            nk = nk + 1
            if(nk >= 3):
                break
                #ye sab band krne ke liye
                # cv2.destroyAllWindows()
                # cap.release()
                # break   

    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    success, img = cap.read()
    img, faces = detector.findFaceMesh(img, draw=False)

    if faces:
        face = faces[0]
        for id in idList:
            cv2.circle(img, face[id], 5,color, cv2.FILLED)

        leftUp = face[159]
        leftDown = face[23]
        leftLeft = face[130]
        leftRight = face[243]
        lenghtVer, _ = detector.findDistance(leftUp, leftDown)
        lenghtHor, _ = detector.findDistance(leftLeft, leftRight)

        cv2.line(img, leftUp, leftDown, (0, 200, 0), 3)
        cv2.line(img, leftLeft, leftRight, (0, 200, 0), 3)

        ratio = int((lenghtVer / lenghtHor) * 100)
        ratioList.append(ratio)
        
        if len(ratioList) > 3:
            ratioList.pop(0)
        ratioAvg = sum(ratioList) / len(ratioList)
        #print(ratioAvg)
        if ratioAvg < 32 and counter == 0:
            blinkCounter += 1
            nk = 0
            #mustblink += 1
            color = (0,200,0)
            counter = 1
        if counter != 0:
            counter += 1
            if counter > 10:
                counter = 0
                color = (255,0, 255)

        cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100),
                           colorR=color)
        
        #cvzone.putTextRect(img, f'Blink Count: {blinkCounter}', (50, 100),
          #                 colorR=color)                           


        imgPlot = plotY.update(ratioAvg, color)
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, imgPlot], 2, 1)
    else:
        img = cv2.resize(img, (640, 360))
        imgStack = cvzone.stackImages([img, img], 2, 1)

    cv2.imshow("Image", imgStack)
    cv2.waitKey(1)




