import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

# IMAGE ADDITION/SUBTRACTION

"""

You can add two images by OpenCV function, cv2.add() or simply by numpy
operation, res = img1 + img2. Both images should be of same depth and type, or
second image can just be a scalar value.

There is a difference between OpenCV addition and Numpy addition. OpenCV
addition is a saturated operation while Numpy addition is a modulo operation.

uses cv2.add(img1,img2) and cv2.subtract(img1,img2)

"""

x = np.uint8([250])
y = np.uint8([10])

print(cv2.add(x,y)) # # 250+10 = 260 => 255
print(x+y) # 250+10 = 260 % 256 = 4 => 4

img=cv2.imread('image_0001.jpg',1)
img1=cv2.imread('image_0002.jpg',1)
res=img[0:100,0:200]+img1[0:100,0:200] # merely adds pixels and saturates them at 255
cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyWindow('image')

# IMAGE BLENDING

"""

This is also image addition, but different weights are given to images so that
it gives a feeling of blending or transparency

cv2.addWeighted() applies the equation:

	dst = X.img1+Y.img2+Z
	where Y=1-X and Z is initial offset

"""

img=cv2.imread('image_0001.jpg',1)
img1=cv2.imread('image_0002.jpg',1)
dst = cv2.addWeighted(img1[0:100,0:200],0.7,img2[0:100,0:200],0.3,0)
cv2.imshow('image',res)
cv2.waitKey(0)
cv2.destroyWindow('image')

# BITWISE OPERATIONS

"""
 
--- Image Thresholding ---

https://docs.opencv.org/3.4/d7/d4d/tutorial_py_thresholding.html

For every pixel, the same threshold value is applied. If the pixel value is
smaller than the threshold, it is set to 0, otherwise it is set to a maximum
value. The function cv.threshold is used to apply the thresholding. The first
argument is the source image, which should be a grayscale image. The second
argument is the threshold value which is used to classify the pixel values.
The third argument is the maximum value which is assigned to pixel values
exceeding the threshold. OpenCV provides different types of thresholding which
is given by the fourth parameter of the function. Types:

	cv.THRESH_BINARY
	cv.THRESH_BINARY_INV
	cv.THRESH_TRUNC
	cv.THRESH_TOZERO
	cv.THRESH_TOZERO_INV

The method returns two outputs. The first is the threshold that was used and
the second output is the thresholded image.

ex. ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

	sets any pixel > 127 to 255 and any pixel < 127 to 0

ex. ret,thresh2 = cv.threshold(img,127,255,cv.THRESH_BINARY_INV)

	same as above but opposite

ex. ret,thresh3 = cv.threshold(img,127,255,cv.THRESH_TRUNC)

	same as first but doesnt set less-than pixels to 0

"""

"""

This includes bitwise AND, OR, NOT and XOR operations. They will be highly
useful while extracting any part of the image, defining and working with
non-rectangular ROI etc

If you want to superimpose an image over another then the bitwise operations make it
possible to do so.

"""

# Load two images
img1 = cv2.imread('roi.jpg')
img2 = cv2.imread('boi.jpg') #color on black image, superimpose the colour part

# I want to put image2 on top-left corner, So I create a ROI of image 1
rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols ]

# Now create a mask of image2 and create its inverse mask also
img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY) # mask of image2 which is just the colour parts > thresh in white and rest in black
mask_inv = cv2.bitwise_not(mask) # creates an inverse of that mask

# Now black-out the area of image2 in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv) # when mask=0, ignores and makes 0, when mask != 0 does bit_and

# Take only region of image2 from logo image.
img2_fg = cv2.bitwise_and(img2,img2,mask = mask)

# Put image2 in ROI and modify the main image
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols ] = dst

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()