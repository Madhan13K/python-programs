import cv2
import numpy as np
def ntg(x):
    pass
img=cv2.imread('smarties.png',1)
cv2.namedWindow('smarties')
cv2.createTrackbar('lh','smarties',0,255,ntg)
cv2.createTrackbar('ls','smarties',0,255,ntg)
cv2.createTrackbar('lv','smarties',0,255,ntg)
cv2.createTrackbar('uh','smarties',255,255,ntg)
cv2.createTrackbar('us','smarties',255,255,ntg)
cv2.createTrackbar('uv','smarties',255,255,ntg)

while True:
    frame=img
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_h=cv2.getTrackbarPos('lh','smarties')
    l_s=cv2.getTrackbarPos('ls','smarties')
    l_v=cv2.getTrackbarPos('lv','smarties')
    u_h=cv2.getTrackbarPos('uh','smarties')
    u_s=cv2.getTrackbarPos('us','smarties')
    u_v=cv2.getTrackbarPos('uv','smarties')

    l_b=np.array((l_h,l_s,l_v))
    u_b=np.array((u_h,u_s,u_v))
    mask=cv2.inRange(hsv,l_b,u_b)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    cv2.imshow('frame',frame)
    key=cv2.waitKey(0)
    if key==27:
        break
cv2.destroyAllWindows()

