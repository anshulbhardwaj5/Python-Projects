import cv2
import numpy as np

img = cv2.imread("anshul.JPG")

imgResize = cv2.resize(img,(300,200)) # Here width comes first

imgCropped = img[0:200,200:500] #while cropping height comes first

cv2.imshow("cropped",imgCropped) #cropped image showing

cv2.imshow("Resize", imgResize)
print(imgResize.shape) #Resized image showing

cv2.imshow("Shapes", img)
print(img.shape)
cv2.waitKey(0)
