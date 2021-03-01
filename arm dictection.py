import cv2
import numpy as np
import math
def nothing(x):
    pass
#open camera

cap = cv2.VideoCapture(0)
cv2.namedWindow("tracker")
cv2.createTrackbar("lh","tracker",0,200,nothing)
while cap.isOpened():
    _,frame=cap.read()


    cropimg=frame[100:300,100:300]

    blurimg=cv2.GaussianBlur(cropimg,(3,3),0)

    hsv=cv2.cvtColor(blurimg,cv2.COLOR_BGR2HSV)
    lh=cv2.getTrackbarPos("lh","tracker")
    ls = cv2.getTrackbarPos("ls", "tracker")
    lv = cv2.getTrackbarPos("lv", "tracker")
    uh = cv2.getTrackbarPos("uh", "tracker")
    us= cv2.getTrackbarPos("us", "tracker")
    uv = cv2.getTrackbarPos("uv", "tracker")




    mask = cv2.inRange(hsv,np.array([lh,ls,lv]),np.array([uh,us,uv]))

    kernal=np.array((5,5))

    dilatedimg=cv2.dilate(mask,kernal,iterations=1)

    erosionimg=cv2.erode(dilatedimg,kernal,iterations=1)

    filterted=cv2.GaussianBlur(erosionimg,(3,3),0)

    _,thresh=cv2.threshold(filterted,127,255,0)

    cv2.imshow("threshold",thresh)

    contours,hiechy=cv2.findContours(thresh.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    try:
        contour = max(contours,key=lambda x: cv2.contourArea(x))

        x,y,w,h =cv2.boundingRect(contour)
        cv2.rectangle(cropimg,(x,y),(x+w,y+h),(0,0,255),0)

        hull=cv2.convexHull(contour)
        drawing=np.zeros(cropimg.shape,np.uint8)
        cv2.drawContours(drawing,[contour],-1,(0,255,0),0)
        cv2.drawContours(drawing,[hull],-1,(0,0,255),0)

        hull=cv2.convexHull(contour,returnPoints=False)
        defects=cv2.convexityDefects(contour,hull)

        countdefects = 0
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i,0]
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])

            a=math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1] )** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
            c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)

            angle = (math.acos((b**2+c ** 2 -a ** 2)/(2*b*c)) * 180) /3,14

            if angle <=90:
                countdefects +=1
                cv2.circle(cropimg,far,1,[0,0,255],-1)

            cv2.line(cropimg,start,end,[0,255,0],-2)

        if countdefects ==0:
            cv2.putText(frame,"ONE",(100,100),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        elif countdefects==1:
            cv2.putText(frame,"TWO",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        elif countdefects==2:
            cv2.putText(frame,"three",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        elif countdefects==3:
            cv2.putText(frame,"four",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        elif countdefects==4:
            cv2.putText(frame,"five",(50,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,255),2)
        else:
            pass
    except:
        pass


        cv2.imshow("output",frame)
        allimg=np.hstack((drawing,cropimg))
        cv2.imshow("countours",allimg)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()