import cv2
import numpy as np
img = cv2.imread("cards.jpg")
width,height = 250,350
#To check the cordinates use your paint and track the cordinates.
pts1 = np.float32([[48,138],[297,58],[145,460],[301,414]])
# Here we are giving the sequence that which one is the height and the width and acc to this it will show the wrap image in proper manner.
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))
#orginal image
cv2.imshow("Cards", img)
#wraped image
cv2.imshow("warp", imgOutput)

cv2.waitKey(0)
