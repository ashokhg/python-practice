import cv2
import winsound
from datetime import datetime
import pywhatkit as pwt
from cv2.cv2 import threshold

flag = 0
now = datetime.now()
cam = cv2.VideoCapture(1)
while cam.isOpened():
    ret, frame1 = cam.read()
    ret, frame2 = cam.read()
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations = 20)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
    for c in contours:
        if cv2.contourArea(c) < 50000:
            continue
        else:
            if flag == 0:
                current_hour = now.strftime("%H")
                current_min = now.strftime("%M")
                nxt_min = int(current_min) + 2
                hour = int(current_hour)
                min = nxt_min
                print("Current hour when motion detected = ", current_hour)
                pwt.sendwhatmsg('+918884262621', 'Action Detected', hour, min)
                flag = 1

        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.Beep(1000, 200)
       #winsound.PlaySound('Y Y Y.mp3', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('Security Cam', frame1)

