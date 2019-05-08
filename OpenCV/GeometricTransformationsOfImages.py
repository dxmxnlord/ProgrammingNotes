import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

"""

OpenCV provides two transformation functions, cv2.warpAffine and
cv2.warpPerspective, with which you can have all kinds of transformations.
cv2.warpAffine takes a 2x3 transformation matrix while cv2.warpPerspective
takes a 3x3 transformation matrix as input.

"""

# SCALING

"""

Scaling is just resizing of the image. OpenCV comes with a function
cv2.resize() for this purpose. The size of the image can be specified
manually, or you can specify the scaling factor. Different interpolation
methods are used. Preferable interpolation methods are cv2.INTER_AREA for
shrinking and cv2.INTER_CUBIC (slow) & cv2.INTER_LINEAR for zooming. By
default, interpolation method used is cv2.INTER_LINEAR for all resizing
purposes.

You can specify the resulting image size or specify the x,y scaling factor

Shrinking - INTER_AREA
Growing - INTER_LINEAR | INTER_CUBIC(slower)

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_COLOR)
height,width=img.shape[:2]
# using custom pixel values; pass as (width,height)
scaleup=cv2.resize(img,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
scaledown=cv2.resize(img,(width-100,height-100),interpolation=cv2.INTER_AREA)
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('img',scaleup)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('img',scaledown)
cv2.waitKey(0)
cv2.destroyAllWindows()
# using the scaling factor
scaleup=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
cv2.imshow('img',scaleup)
cv2.waitKey(0)
cv2.destroyAllWindows()
scaledown=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
cv2.imshow('img',scaledown)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

--- shrink image to fit a max height/width (keeping aspect ratio) ---

height, width = img.shape[:2]
max_height = 300
max_width = 300

# only shrink if img is bigger than required
if max_height < height or max_width < width:
    # get scaling factor
    scaling_factor = max_height / float(height)
    if max_width/float(width) < scaling_factor:
        scaling_factor = max_width / float(width)
    # resize image
    img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)

cv2.imshow("Shrinked image", img)
key = cv2.waitKey()

"""

# TRANSLATION

"""

Translation is the shifting of object’s location. If you know the shift in
(x,y) direction, let it be (t_x,t_y), you can create the transformation matrix
M as follows:

	M = np.array([[1,0,t_x],[0,1,t_y]],dtype='float32')

Then pass M into the warpAffine() function (takes a 2x3 matrix !)

Third argument of the cv2.warpAffine() function is the size of the output
image, which should be in the form of (width, height). Remember width = number
of columns, and height = number of rows. 

"""

img=cv2.imread('roi.jpg',0)
rows,cols = img.shape
# shift of (100,50) pixels
M = np.float32([[1,0,100],[0,1,50]])
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ROTATION

"""

Rotation of an image for an angle $ is achieved by the transformation matrix (sin cos)

OpenCV provides scaled rotation with adjustable center of rotation so that you
can rotate at any location you prefer. The rotation is anti-clockwise

The modified rotation matrix is a 2x3 matrix with 4 parameters : 

	x_center y_center angle scale
	
	- the scale is an isotropic scale factor. When the scale factor is a positive
	  number smaller than 1, scaling is sometimes also called contraction and vice-versa

To find this transformation matrix, OpenCV provides a function, cv2.getRotationMatrix2D()

"""

img=cv2.imread('roi.jpg',0)
rows,cols = img.shape
# 90 degrees around center and same size
M = cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

#  AFFINE TRANSFORMATION

"""

In affine transformation, all parallel lines in the original image will still
be parallel in the output image. To find the transformation matrix, we need
three points from input image and their corresponding locations in output
image. Then cv2.getAffineTransform will create a 2x3 matrix which is to be
passed to cv2.warpAffine.

"""

img=cv2.imread('roi.jpg',0)
rows,cols = img.shape
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
dst = cv2.warpAffine(img,M,(cols,rows))
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# PERSPECTIVE TRANSFORMATION

"""

For perspective transformation, you need a 3x3 transformation matrix. Straight
lines will remain straight even after the transformation. To find this
transformation matrix, you need 4 points on the input image and corresponding
points on the output image. Among these 4 points, 3 of them should not be
collinear. Then transformation matrix can be found by the function
cv2.getPerspectiveTransform. Then apply cv2.warpPerspective with this 3x3
transformation matrix.

ex. boundaries of a zoomed out sudoku box where the new points are the edge pixels of
the new image; streches the sudoku box out to fill the space while preserving the
straight lines

"""

img=cv2.imread('sudoku.jpg',0)
rows,cols = img.shape
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]]) # boundaries of box
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]]) # image boundaries
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(300,300))