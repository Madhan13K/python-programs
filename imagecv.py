import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread("lena.jpg",1)
cv.imshow('image',img)
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25
dst=cv.filter2D(img,-1,kernel)
blur=cv.blur(img,(5,5))
plt.imshow(blur)
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
