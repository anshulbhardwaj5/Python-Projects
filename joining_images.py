import cv2
import numpy as np
img = cv2.imread("img.png")

imghor = np.hstack((img,img))
imgvir = np.vstack((img,img))
cv2.imshow("Horizontal",imghor)
cv2.imshow("Vertical Image",imgvir)

cv2.waitKey(0)
