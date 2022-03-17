import cv2
path="Resources/sample.jpg"
img=cv2.imread(path)
print(img.shape)
width,height=800,800
imgRes=cv2.resize(img,(width,height))
print(imgRes.shape)
imgCropped = img[0:4000,4000:4624]
cv2.imshow("image",img)
cv2.imshow("Resize",imgRes)
cv2.imshow("Cropped",imgCropped)
cv2.waitKey(0)