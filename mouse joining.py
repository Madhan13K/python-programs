import cv2
import numpy as np
# events=[i for i in dir(cv2) if 'EVENT' in i]
# print(events)
def click_event(event,x,y,flags,parum):
    if event==cv2.EVENT_LBUTTONDOWN:
        # cv2.circle(img,(x,y),3,(0,255,255),-1)
        # points.append((x,y))
        # if len(points)>=2:
        #     cv2.line(img,points[-1],points[-2],(255,0,0),5)
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        cv2.circle(img,(x,y),3,(0,255,255),-1)
        mycolorimage=np.zeros((512,512,3),np.uint8)
        mycolorimage[:]=[blue,green,red]
        cv2.imshow('color',mycolorimage)
        # cv2.imshow('image',img)

# img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('lena.jpg',1)
cv2.imshow('image',img)
points=[]
cv2.setMouseCallback('image',click_event)
cv2.waitKey()
cv2.destroyAllWindows()