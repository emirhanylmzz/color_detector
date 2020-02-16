"""
Created on Thu Feb 13 23:12:01 2020

@author: emirhanylmzz
"""
import cv2
import numpy as np

video_capture = cv2.VideoCapture(0)

boundiries=[
        ([161, 155, 84], [179, 255, 255]), #red, 
        ([94, 80, 2], [126, 255, 255]), #blue
        ([25, 52, 72], [102, 255, 255]) #green
        ]
color = 0 #variable for choosing color
color2 = ["RED", "BLUE", "GREEN"] #variable for printing text to screen
while True:
    _, frame = video_capture.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower = np.array(boundiries[color][0])
    upper = np.array(boundiries[color][1])
    
    mask = cv2.inRange(hsv, lower, upper)
    o = cv2.bitwise_and(frame, frame, mask=mask)
    o = cv2.putText(o, color2[color], (50,50), cv2.FONT_HERSHEY_SIMPLEX , 1, (255, 255, 255), 2)
    cv2.imshow("Detector", np.hstack([frame,o]))
    
    if cv2.waitKey(1) & 0xFF == ord('r'):
        color = 0
    elif cv2.waitKey(1) & 0xFF == ord('b'):
        color = 1
    elif cv2.waitKey(1) & 0xFF == ord('g'):
        color = 2
    elif cv2.waitKey(1) & 0xFF == ord('q'):
        break
#print(np.transpose(mask.nonzero())) coordinates
video_capture.release()
cv2.destroyAllWindows()
