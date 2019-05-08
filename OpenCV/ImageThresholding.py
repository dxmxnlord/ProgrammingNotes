import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

# SIMPLE THRESHOLDING

"""

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

img=cv2.imread('roi.jpg',cv2.IMREAD_GRAYSCALE)
imglist=[]
imglist.append(cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1])
imglist.append(cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)[1])
imglist.append(cv2.threshold(img,127,255,cv2.THRESH_TRUNC)[1])
imglist.append(cv2.threshold(img,127,255,cv2.THRESH_TOZERO)[1])
imglist.append(cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)[1])
for image in imglist:
    cv2.imshow('img',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# ADAPTIVE THRESHOLDING

"""

When the image has different lighting conditions, the threshold constant
should differ per area. Hence we use adaptive thresholding. In this, the
algorithm calculates the threshold for a small regions of the image

It has three ‘special’ input params and only one output argument.

Adaptive Method - It decides how thresholding value is calculated.
	cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.
Block Size - It decides the size of neighbourhood area. ODD NUMBER ALWAYS
C - It is just a constant which is subtracted from the mean or weighted mean calculated

Along with the adaptive method you also have to give the threshold method

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_GRAYSCALE)
imglist=[]
imglist.append(cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1])
imglist.append(cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
    cv2.THRESH_BINARY,11,0))
imglist.append(cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
    cv2.THRESH_BINARY,11,0))
for image in imglist:
    cv2.imshow('img',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# OTSU'S BINARIZATION

"""

Used when you want to find the threshold constant in the globlal thresholding method
For a bimodal image(an image whose histogram has two peaks) the binarization is very
accurate.

For this, our cv2.threshold() function is used, but pass an extra flag,
cv2.THRESH_OTSU. For threshold value, simply pass zero. Then the algorithm
finds the optimal threshold value and returns you as the second output,
retVal. If Otsu thresholding is not used, retVal is same as the threshold
value you used.

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_GRAYSCALE)
imglist=[]
imglist.append(cv2.threshold(img,127,255,cv2.THRESH_BINARY)[1])
imglist.append(cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1])
for image in imglist:
    cv2.imshow('img',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()