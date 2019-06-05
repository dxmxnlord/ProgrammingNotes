import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

# LAPLACE METHOD 

"""

With this in mind, the Laplace operator can also be used as a kind of edge
detector. To see how this is done, consider the first derivative of a
function, which will (of course) be large wherever the function is changing
rapidly. Equally important, it will grow rapidly as we approach an edge-like
discontinuity and shrink rapidly as we move past the discontinuity. Hence the
derivative will be at a local maximum somewhere within this range. Therefore
we can look to the 0s of the second derivative for locations of such local
maxima. Got that? Edges in the original image will be 0s of the Laplacian.
Unfortunately, both substantial and less meaningful edges will be 0s of the
Laplacian, but this is not a problem because we can simply filter out those
pixels that also have larger values of the first (Sobel) derivative. Figure
6-6 shows an example of using a Laplacian on an image together with details of
the first and second derivatives and their zero crossings.

"""

# CANNY ALGORITHM

"""

Steps: 

- Noise reduction with a 5x5 gaussian filter

- The image is then convolved with the sobel operator in the x and y direction
  and the edge gradient is calculated for each pixel as the square root of the pixels
  x derivative and y derivative and the angle as arctan of y over x derivative of that 
  pixel. 

- After getting the gradient a all the non- edge pixels are removed and pixels which may
  constitute the edges are kept resulting in a binary image of edges.

- Following this hysterisis thresholding is peformed. A maxval and minval are set. Any pixel 
  above tbe maxval is definetely an edge and is kept. Any pixel between the thresholds is kept 
  if its associated with any pure edge. This results in a pure edge image.The canny ratio of
  high : low threshold is recommended between 2:1 and 3:1 

Function:

cv2.Canny(img,threshold1,threshold2[,apertureforsobel]) → edges

- it also has a fourth argument which is L2gradient=true/false
	
	- true for the square root gradient calculation
	- false (default) for |Xderiv| + |Yderiv| calculation

"""

img=cv2.imread('boi.jpg',cv2.IMREAD_GRAYSCALE)
canny=cv2.Canny(img,150,100)
cv2.imshow('image',canny)
cv2.waitKey(0)
cv2.destroyAllWindows()