import cv2
import numpy as np

cap = cv2.VideoCapture(1)

while True:
	_, frame = cap.read()
	
	#ROI
	gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	_, threshold = cv2.threshold(gray_frame, 80, 255, cv2.THRESH_BINARY)

	#belt = frame[209:327, 137:530]
	_, contours, _= cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 	#1703
	for cnt in contours:
		#print(cnt)
		(x, y, w, h) = cv2.boundingRect(cnt)

		#calculating area
		area = cv2.contourArea(cnt)
		#small and big nuts
		if area > 500:
			#Big nuts
			cv2.rectangle(belt, (x,y), (x+w, y+h), (0,0,255),2)
		# else:
		# 	cv2.rectangle(belt, (x, y), (x + w, y + h), (255,0,0), 2)
		# 	cv2.putText(belt, str(area), (x,y), 0, 1, (0,0,255))

		elif 100<area<500:
			cv2.rectangle(belt, (x, y), (x + w, y + h), (255,0,0), 2)
			cv2.putText(belt, str(area), (x,y), 0, 1, (0,0,255))
	
	#belt
	#x = 137 , y = 209
	#x2 = 530, y = 327
	cv2.imshow("Gray", gray_frame)
	cv2.imshow("Frame", threshold)
	cv2.imshow("Nuts", contours)

	key = cv2.waitKey(1)
	if key == 27:
		break

cap.release()
cv2.destroyAllWindows()
