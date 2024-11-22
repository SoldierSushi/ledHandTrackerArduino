import cv2
from cvzone.HandTrackingModule import HandDetector
import mediapipe as mp
import pyfirmata

detector=HandDetector(detectionCon=0.8,maxHands=1)
video=cv2.VideoCapture(0)

comport='/dev/cu.usbmodem11301'
board=pyfirmata.Arduino(comport)
led_1=board.get_pin('d:8:o')
led_2=board.get_pin('d:9:o')
led_3=board.get_pin('d:10:o')
led_4=board.get_pin('d:11:o')
led_5=board.get_pin('d:12:o')

while True:
    ret,frame=video.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    hands,img=detector.findHands(frame)

    if hands:
        lmList=hands[0]
        fingerUp=detector.fingersUp(lmList)

        print(fingerUp)

        fingerCount = sum(fingerUp)

        if fingerCount == 0:
            cv2.putText(frame,'Finger count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(0)
            led_2.write(0)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)
        elif fingerCount == 1:
            cv2.putText(frame,'Finger count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(1)
            led_2.write(0)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0)  
        elif fingerCount == 2:
            cv2.putText(frame,'Finger count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(1)
            led_2.write(1)
            led_3.write(0)
            led_4.write(0)
            led_5.write(0) 
        elif fingerCount == 3:
            cv2.putText(frame,'Finger count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(0)
            led_5.write(0)
        elif fingerCount == 4:
            cv2.putText(frame,'Finger count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(0)
        elif fingerCount == 5:
            cv2.putText(frame,'Finger count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            led_1.write(1)
            led_2.write(1)
            led_3.write(1)
            led_4.write(1)
            led_5.write(1)
            
    cv2.imshow("frame",frame)
    k=cv2.waitKey(1)
    if k==ord("k"):
        break

video.release()
cv2.destroyAllWindows()
