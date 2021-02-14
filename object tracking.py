import cv2
import numpy as np
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _,dframe=cap.read()
    frame=cv2.resize(dframe,(400,300))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, tresh = cv2.threshold(gray, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow("tresh",tresh)
    dilated = cv2.dilate(tresh, (5, 5), iterations=2)
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerhsv=np.array([0,71,79])
    upperhsv=np.array([11,225,225])

    mask= cv2.inRange(hsv,lowerhsv,upperhsv)
    finalhsv = cv2.bitwise_and(frame,frame,mask=mask)

    contour,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    contour=sorted(contour,key=lambda x:cv2.contourArea(x),reverse=True)

    for cnt in contour:
        (x,y,w,h)=cv2.boundingRect(cnt)
        xmeduim=int((x+x+w)/2)
        cv2.line(frame, (xmeduim, 0), (xmeduim, 480), (0, 255, 0), 2)
        print(x,y,w)

        break


    cv2.imshow("mask",mask)

    if cv2.waitKey(1) ==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()