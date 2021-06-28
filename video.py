import cv2
import numpy as np

#img =cv2.imread('flower.jpg',1)
img=np.zeros([512,512,3],np.uint8
             )

img=cv2.line(img, (0,0), (400,400),(0,255,0),5 )
img=cv2.arrowedLine(img,(0,255),(400,400),(255,0,0),10)
img=cv2.rectangle(img, (300,0),(510,128),(0,55,0),-1)
img=cv2.circle(img,(200,200),100,(0,255,255),10)
font=cv2.FONT_ITALIC
img=cv2.putText(img, 'OpenCV',(10,500),font,5,(255,255,255),15,cv2.LINE_AA)
cv2.imshow('image', img)



cv2.waitKey(0)
cv2.destroyAllWindows()