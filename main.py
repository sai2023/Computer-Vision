import cv2
import numpy as np
kernel=np.ones((5,5),np.uint8)
print(kernel)
print("Hello world")
frameWidth = 480
frameHeight =480
img = cv2.imread("Resources/sample.jpg",)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
imgBlur=cv2.GaussianBlur(img,(9,9),0)
imgcanny=cv2.Canny(imgBlur,150,100)
imgDialation=cv2.dilate(imgcanny,kernel,iterations=2)
imgEroded=cv2.erode(imgDialation,kernel,iterations=1)
cv2.imshow("sample",img)
cv2.imshow("Grayscale",imgGray)
cv2.imshow("Blurred",imgBlur)
cv2.imshow("canny",imgcanny)
cv2.imshow("Dialation",imgDialation)
cv2.imshow("Eroded",imgEroded)
cv2.waitKey(0)

# frameWidth = 480
# frameHeight =480
# cap = cv2.VideoCapture("Resources/sample.mp4")
# cap.set(3,frameWidth)
# cap.set(4,frameHeight)

# while True:
#     success,img = cap.read()
#     img = cv2.resize(img,(frameWidth,frameHeight))
#     cv2.imshow("video",img)
#
#
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
