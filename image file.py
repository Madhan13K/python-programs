import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
print(cap.isOpened())
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret==True:

       print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
       print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
       # cap.set(3,720)
       # cap.set(4,720)
       # print(cap.get(3))
       # print(cap.get(4))
       out.write(frame)
       gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame',gray)
       if cv2.waitKey(0)&0xFF==ord('q'):
           break
cap.release()
out.release()
cv2.destroyAllWindows()