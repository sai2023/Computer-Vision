import cv2
import numpy as np
circles = np.zeros((4,2),np.int32)
c= 0
def mousePoints(event,x,y,flags,params):
    global c
    if event == cv2.EVENT_LBUTTONDOWN:

        #print(x,y)
        circles[c]=x,y
        c = c+1
        print(circles)

img=cv2.imread("Resources/Sample2.jpg")


while True:
    if c==4:
        width, height = 300, 600
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput=cv2.warpPerspective(img,matrix,(width,height))
        cv2.imshow("Warpimage", imgOutput)
        for i in range(0,4):
            cv2.circle(img,(circles[i][0],circles[i][1]),5,(0,0,255),cv2.FILLED)


    cv2.imshow("Perspective",img)
    cv2.setMouseCallback("Perspective",mousePoints)
    # cv2.imshow("Warpimage",imgOutput)
    cv2.waitKey(1)
