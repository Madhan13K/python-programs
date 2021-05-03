# import cv2 as cv
# import numpy as np
# cap=cv.VideoCapture(0)
# fourcc=cv.VideoWriter_fourcc(*'XVID')
#
# out=cv.VideoWriter('output1.avi',fourcc,20.0,(640,480))
# print(cap.isOpened())
# while cap.isOpened():
#    ret,frame=cap.read()
#    # cv.imshow('frame',frame)
#    print(cap.get(3))
#    print(cap.get(4))
#    out.write(frame)
#
#    grey=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#    cv.imshow('grey',grey)
#    if cv.waitKey(1) &0xFF ==ord('q'):
#       break
# cap.release()
# out.release()
# cv.destroyAllWindows()




# import cv2 as cv
# import numpy as np
# # img=cv.imread('lena.jpg')
# img=np.zeros((512,512,3),np.uint8)
# img=cv.line(img,(0,0),(100,250),(255,0,0),2)
# img=cv.arrowedLine(img,(50,50),(255,255),(0,0,255),3)
# font=cv.FONT_HERSHEY_COMPLEX
# img=cv.putText(img,'opencv',(10,500),font,4,(147,157,167),10,cv.LINE_AA)
# cv.imshow('image',img)
# cv.waitKey(0)
# cv.destroyAllWindows()


import cv2 as cv
import numpy as np
# events=[i for i in dir(cv) if 'EVENT' in i]
# print(events)
def click_event(event,x,y,flag,parum):
   if event==cv.EVENT_LBUTTONDOWN:
      print(x, ',' ,y)
      font=cv.FONT_HERSHEY_COMPLEX
      strxy=str(x)+','+str(y)
      cv.putText(img,strxy,(x,y),font,1,(255,255,0),2)
      cv.imshow('image',img)
   if event==cv.EVENT_RBUTTONDOWN:
      blue=img[y,x,0]
      green=img[y,x,1]
      red=img[y,x,2]
      font=cv.FONT_HERSHEY_COMPLEX
      strxyz=str(blue)+','+str(green)+','+str(red)
      cv.putText(img,strxyz,(x,y),font,1,(255,255,0),2)
      cv.imshow('image',img)
img=np.zeros((512,512,3),np.uint8)
cv.imshow('image',img)
cv.setMouseCallback('image',click_event)
cv.waitKey(0)
cv.destroyAllWindows()