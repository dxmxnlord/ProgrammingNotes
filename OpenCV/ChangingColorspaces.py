import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

# CHANGING COLORSPACE 

"""

For color conversion, we use the function cv2.cvtColor(input_image, flag)
where flag determines the type of conversion.

For BGR to Gray conversion we use the flags cv2.COLOR_BGR2GRAY.
Similarly for BGR to HSV, we use the flag cv2.COLOR_BGR2HSV

For HSV, Hue range is [0,179], Saturation range is [0,255] and Value range is
[0,255]. Different softwares use different scales. So if you are comparing
OpenCV values with them, you need to normalize these ranges.

You can convert BGR to HSV using the cvtColor function too

	green = np.uint8([[[0,255,0 ]]])
	hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
	Now you take [H-10, 100,100] and [H+10, 255, 255] as lower bound and upper bound respectively.

"""

# SIMPLE COLOUR TRACKING

"""

In HSV, it is more easier to represent a color than RGB color-space.

1. Convert from BGR to HSV
2. Threshold the image for a range of the desired colour ex. blue
3. extract the blue object alone

cv2.inRange(img,lower_array,upper_array) - creates binary mask [white if true ; black if false]
	note : the arrays have to be numpy arrays with a single H-S-V value 

"""

img=cv2.imread('roi.jpg')
hgvimg=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50],dtype='uint8')
upper_blue = np.array([130,255,255],dtype='uint8')

mask=cv2.inRange(hgvimg,lower_blue,upper_blue)

resimg=cv2.bitwise_and(img,img,mask=mask) # only blue colors left
cv2.imshow('win',resimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

invmask=cv2.bitwise_not(mask)
resimg=cv2.bitwise_and(img,img,mask=invmask) # only blue colors removed
cv2.imshow('win',resimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

lower_green=np.array([30,0,0],dtype='uint8')
upper_green=np.array([100,255,255],dtype='uint8')
mask2=cv2.inRange(hgvimg,lower_green,upper_green)
resimg2=cv2.bitwise_and(img,img,mask=mask2)
cv2.imshow('win',resimg2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# combine both masks to detect multiple colors
mask3=cv2.bitwise_or(mask,mask2)
resimg3=cv2.bitwise_and(img,img,mask=mask3)
cv2.imshow('win',resimg3)
cv2.waitKey(0)
cv2.destroyAllWindows()