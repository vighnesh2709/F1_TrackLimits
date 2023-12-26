import cv2 as cv
import numpy as np
import time

video=cv.VideoCapture("track3.mp4")

while True:
 try:   
    
    
    isTrue,og_frames=video.read() 
    frames=cv.GaussianBlur(og_frames,(5,5), 0)
    gray=cv.cvtColor(frames,cv.COLOR_BGR2GRAY)
    low_white=np.array([215])
    high_white=np.array([250])
    mask=cv.inRange(gray,low_white,high_white)
    edges=cv.Canny(mask,70,150)




    lines=cv.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)
    if lines is not None:
       for line in lines:
          x1,y1,x2,y2=line[0]
          cv.line(og_frames,(x1,y1),(x2,y2),(0,255,0),5)

         
   

    cv.imshow("blur",frames) 
    cv.imshow("final",og_frames)
    cv.imshow("gray",gray)
    cv.imshow("edge",edges)

   
    key=cv.waitKey(20)&0xFF
    if key==ord('d'):
        break
        capture.release
        cv.destroyAllWindows
 except:
    break

