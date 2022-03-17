import cv2

import numpy as np

img=np.zeros((512,512,3),np.uint8)
# print(img)
img[:]=255,255,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),(2))
cv2.rectangle(img,(350,100),(450,200),(0,0,255),cv2.FILLED)
cv2.circle(img,(150,400),50,(0,0,255),3)
cv2.putText(img,"I am OPEN CV",(200,50),cv2.FONT_ITALIC,0.75,(0,0,255),2)
cv2.imshow("Blank",img)
cv2.waitKey(0)