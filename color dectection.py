 # DURING THE RUN TIME , YOY CAN ADJECT THE TRACKBAR TO SELECT A
 # PARTICULAR COLOR.MAKE SURE THE COLOR YOU WANTED TO TRACK IS IN WHITE COLOR
 # THIS PROGRAM IS WRITTEN BY AMAL BENNY




import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0)
# creating a window fro trackbar
cv2.namedWindow("HSV")
cv2.resizeWindow("HSV",800,200)

# creating a trackbar in the window above
cv2.createTrackbar("HH","HSV",255,255,nothing)
cv2.createTrackbar("HS","HSV",255,255,nothing)
cv2.createTrackbar("HV","HSV",255,255,nothing)

cv2.createTrackbar("LH","HSV",0,255,nothing)
cv2.createTrackbar("LS","HSV",0,255,nothing)
cv2.createTrackbar("LV","HSV",0,255,nothing)

while True:
    _,frameo = cap.read()
    frame= cv2.resize(frameo,(300,200))

    blur = cv2.GaussianBlur(frame,(3,3),0)

    # FINDING THE HSV OF THE blur
    hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

    # getting values from the trackbar
    hh=cv2.getTrackbarPos("HH","HSV")
    hs=cv2.getTrackbarPos("HS","HSV")
    hv=cv2.getTrackbarPos("HV","HSV")

    lh=cv2.getTrackbarPos("LH","HSV")
    ls=cv2.getTrackbarPos("LS","HSV")
    lv=cv2.getTrackbarPos("LV","HSV")

    lowerhsv = np.array([lh,ls,lv])
    higherhsv = np.array([hh,hs,hv])

    # SELECTING THE COLOR BETWEEN THESE VALUES
    final = cv2.inRange(hsv,lowerhsv,higherhsv)

    # making a window fo showing mask
    result= cv2.bitwise_and(frame,frame,mask=final)

    #DRAWING RECTANGLE AROUND THE COLOR YOU WANT TO TRACK

    countour,_ = cv2.findContours(final,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in countour:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    # print the cap
    cv2.imshow("white on the color that you want to track",final)
    cv2.imshow("cap",frame)
    cv2.imshow("mask",result)


    # waiting till you press q
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()


