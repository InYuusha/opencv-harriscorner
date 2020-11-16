import cv2
import numpy as np 

box=cv2.imread("  ")    #image location
if box.all()==None:
     raise IOError("Image Cant be opened")


gray=cv2.cvtColor(box,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)

dst=cv2.cornerHarris(gray,8,5,0.04) #( float array(gray),blocks in the image , c=0.04)
#dst=cv2.dilate(dst,None)
box[dst>0.01*dst.max()]=[0,0,255]
cv2.imshow("Harris Corner",box)
cv2.waitKey(0)
