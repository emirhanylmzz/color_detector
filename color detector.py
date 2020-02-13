"""
@author: emirhanylmzz
"""
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

#blue and red colors
boundaries=[
        ([161, 155, 84], [179, 255, 255]), 
        ([94, 80, 2], [126, 255, 255])]
color = 0

while True:
    _, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower = np.array(boundaries[color][0])
    upper = np.array(boundaries[color][1])
    
    mask = cv2.inRange(hsv, lower, upper)
    o = cv2.bitwise_and(frame, frame, mask=mask)
    
    cv2.imshow("Detector", np.hstack([frame, o]))

    if cv2.waitKey(1) & 0xFF == ord('e'):
       if color != 1:
           color = 1
       else:
           color = 0
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
exit()
