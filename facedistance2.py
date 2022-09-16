import pyttsx3
import cv2
import time
import sys
import cvzone
from FaceMeshModule import FaceMeshDetector

nk = 1
while (True):
    s = {}
    s[1] = "none"
    f = open("face_distance.txt", "r")
    s = f.readlines()
    print(int(s[0]))
    time.sleep(1)
    if (int(s[0]) == 1):
        f.close()

        engine = pyttsx3.init()
        # getting details of current speaking rate
        rate = engine.getProperty('rate')
        engine.setProperty('rate', 200)     # setting up new voice rate
        voices = engine.getProperty('voices')
        # 1 for female and 0 for male
        engine.setProperty('voice', voices[1].id)

        def talk(text):
            engine.say(text)

            engine.runAndWait()

        cap = cv2.VideoCapture(0)
        detector = FaceMeshDetector(maxFaces=1)

        while True:
            nk = nk + 1
            # print(nk)
            success, img = cap.read()
            img, faces = detector.findFaceMesh(img, draw=False)

            if faces:
                face = faces[0]
                pointLeft = face[145]
                pointRight = face[374]
                # Drawing
                # cv2.line(img, pointLeft, pointRight, (0, 200, 0), 3)
                # cv2.circle(img, pointLeft, 5, (255, 0, 255), cv2.FILLED)
                # cv2.circle(img, pointRight, 5, (255, 0, 255), cv2.FILLED)
                w, _ = detector.findDistance(pointLeft, pointRight)
                W = 6.3

                # # Finding the Focal Length
                # d = 50
                # f = (w*d)/W
                # print(f)

                # Finding distance
                f = 840
                d = (W * f) / w
                # print(int(d))

                cvzone.putTextRect(img, f'Depth: {int(d)}cm',
                                   (face[10][0] - 100, face[10][1] - 50),
                                   scale=2)
                if (d < 70):
                    talk("your are too close")

                print("in")
                nk = 0
                f = open("face_distance.txt", "r")
                s = f.readlines()
                if (int(s[0]) == 0):
                    print("in sdfjlaksfdj")
                    # cv2.destroyWindow('')
                    # sys.exit()
                    cv2.destroyAllWindows()
                    cap.release()

            cv2.imshow("Image", img)
            cv2.waitKey(1)
