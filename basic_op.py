import numpy as np
import cv2

img =cv2.imread('wall.jpeg')
img2 =cv2.imread('glow.jpg')
#print(img.size)
#print(img.dtype)
b,g,r=cv2.split(img)
img =cv2.merge((b,g,r))

#tree=img[280:340,330:388]
#img[245:256,100:150]= tree

img= cv2.resize(img,(600,600))
img2= cv2.resize(img2,(600,600))


#dst=cv2.add(img,img2);
dst=cv2.addWeighted(img,.8, img2, .5,0);
cv2.imshow('image', dst)

filename='ful.jpg'
cv2.imwrite(filename,dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
