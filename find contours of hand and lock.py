import cv2
import math
import numpy as np

def NOTHING(x):
    pass
#cv2.namedWindow("A HSV")############################################################
cv2.resizeWindow("A HSV",500,400)
cv2.createTrackbar("lh","A HSV",0,179,NOTHING)
cv2.createTrackbar("ls","A HSV",0,255,NOTHING)
cv2.createTrackbar("lv","A HSV",0,255,NOTHING)
cv2.createTrackbar("uh","A HSV",179,179,NOTHING)
cv2.createTrackbar("us","A HSV",255,255,NOTHING)
cv2.createTrackbar("uv","A HSV",255,255,NOTHING)

###################################capture vedio########################################
cap=cv2.VideoCapture(0)

while cap.isOpened():
    _,frame=cap.read()
    frame=cv2.resize(frame,(400,300))
    blur=cv2.GaussianBlur(frame,(5,5),5)
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos("lh", "A HSV")
    ls = cv2.getTrackbarPos("ls", "A HSV")
    lv = cv2.getTrackbarPos("lv", "A HSV")
    uh = cv2.getTrackbarPos("uh", "A HSV")
    us = cv2.getTrackbarPos("us", "A HSV")
    uv = cv2.getTrackbarPos("uv", "A HSV")
################################################### selecting color of hand ###############
    samplelowerhsv=[lh,ls,lv]
    samplehigherhsv=[uh,us,uv]

    samplelowerhsv1=[10,26,67]
    samplehigherhsv1=[74,130,168]

    samplelowerhsv2=[9,21,66]
    samplehigherhsv2=[74,130,168]

    samplelowerhsv3=[14,0,71]
    samplehigherhsv3=[51,85,146]

    samplelowerhsv4=[5,0,72]
    samplehigherhsv4=[98,51,196]

    samplelowerhsv5=[6,33,36]
    samplehigherhsv5=[36,246,178]

    lowerhsv=np.array( samplelowerhsv5)  ####  change it to set the color of your hand
    higherhsv=np.array(samplehigherhsv5)

    mask=cv2.inRange(hsv,lowerhsv,higherhsv)


    ##############################################draw a rectangle on hand######################


    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    ###########################################################################################







    hull = cv2.convexHull(cnt,returnPoints=False)



###############################################################check defects################################

    defects=cv2.convexityDefects(cnt,hull)
    for i in range(defects.shape[0]):
        s,e,f,d = defects[i,0]
        start=tuple(cnt[s][0])
        end=tuple(cnt[e][0])
        far=tuple(cnt[f][0])
        cv2.line(frame,start,end,(0,255,0),2)
        cv2.circle(frame,far,5,(0,0,255),-1)
        break

            #cv2.drawContours(frame, hull, -1, (0, 255, 0))



###############################################finding convex hull#########################





###########################################################################################

#########################################show output#######################3################

    cv2.imshow("tresh",frame)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
