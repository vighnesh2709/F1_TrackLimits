'''import cv2 as cv
#import numpy as np

video=cv.VideoCapture("track3.mp4")
ret,frame=video.read()
frame=cv.resize(frame,(500,500))
x1,y1=244,133
x2,y2=167, 124
#roi=frame[y1:y2,x1:x2]
while True:
   
    
    
    isTrue,frames=video.read()
    roi=frames[y1:y2, x1:x2]
    cv.imshow("roi",roi)
    
   
    key=cv.waitKey(20)&0xFF
    if key==ord('d'):
        break
video.release()
cv.destroyAllWindows()'''

import cv2

# Load the video
cap = cv2.VideoCapture('track3.mp4')

# Check if the video was opened successfully
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()
ret,frame=cap.read()
op=cv2.selectROI(frame)
print(op)
# Define the coordinates of the top-left and bottom-right corners of the ROI rectangle
x1, y1 = 298, 117  # Top-left corner
x2, y2 = 152, 137  # Bottom-right corner

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Extract the ROI using slicing
    roi = frame[y1:y2, x1:x2]

    # Display the ROI
    cv2.imshow('ROI', roi)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(25) & 0xFF == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()


