import cv2
import numpy as np

img=cv2.imread("Resources/Sample2.jpg")

width, height= 300,600
pts1 = np.float32([[497,154],[586,168],[476,274],[570,292]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
print(pts2)
print(pts1)
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput=cv2.warpPerspective(img,matrix,(width,height))
for i in range(0,4):
    cv2.circle(img,(int(pts1[i][0]),int(pts1[i][1])),5,(0,0,255),cv2.FILLED)


cv2.imshow("Perspective" ,img)
cv2.imshow("Warpimage",imgOutput)
cv2.waitKey(0)