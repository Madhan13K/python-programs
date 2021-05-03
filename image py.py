import cv2 as cv
import numpy as np
def ntg(x):
    print(x)
img=np.zeros((300,512,3),np.uint8)
cv.namedWindow('image')
cv.createTrackbar('B','image',0,255,ntg)
cv.createTrackbar('G','image',0,255,ntg)
cv.createTrackbar('R','image',0,255,ntg)
switch='0:off\n 1:on'
cv.createTrackbar(switch,'image',0,1,ntg)
while 1:
    cv.imshow('image',img)
    k=cv.waitKey(1)&0xFF
    if k==27:
        break
    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    r=cv.getTrackbarPos('R','image')
    s=cv.getTrackbarPos(switch,'image')
    if s==0:
        img[:]=0
    else:

        img[:]=[b,g,r]
cv.destroyAllWindows()
