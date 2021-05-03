import cv2
import numpy as np
img=cv2.imread('messi5.jpg',-1)
img1=cv2.imread('lena.jpg')
print(img.shape)
print(img.dtype)
print(img.size)
b,g,r= cv2.split(img)
img=cv2.merge((b,g,r))
ball=img[280:340, 330:390]
img[273:333,100:160]=ball
img=cv2.resize(img,(512,512))
img1=cv2.resize(img1,(512,512))
dst=cv2.addWeighted(img,.5,img1,.5,0)
cv2.imshow('image',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2Library.xml
import numpy as np
img=cv2.imread('lena.jpg',1)
img=cv2.resize(img,(512,512))
face=img[280:340, 330:390]
# img1=cv.resize(img1,(512,512))
# print(img.shape)
# print(img1.shape)
# img1=cv2.resize(img1,(512,512))
# img=cv2.resize(img,(512,512))

img[273:333,100:160]=face
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
