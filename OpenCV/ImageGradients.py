import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

"""

An image gradient is a directional change in the intensity or color in an
image. The gradient of the image is one of the fundamental building blocks in
image processing 

The magnitude of the gradient tells us how quickly the image is changing,
while the direction of the gradient tells us the direction in which the image
is changing most rapidly.

OpenCV provides three types of gradient filters or High-pass filters, Sobel,
Scharr and Laplacian

"""

# SOBEL DERIVATIVES AND THE SCHARR FILTER

"""

Help convolve an image and compute its deriative. Exist for any order derivative and even mixed derivatives

cv2.Sobel (src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst

	ddepth - depth of output image. ( -1 ) for same depth, refer docs for others
	dx - the order of differentiation of x direction
	dy - the order of differentiation of y direction
	ksize - size of the SOBEL kernel ( 1, 3, 5, 7 ) ; ( -1 ) for a SCHARR kernel [[ better results  ]]

The Sobel operators combine Gaussian smoothing and differentiation, so the
result is more or less resistant to the noise.

In all cases except one, the ksize times ksize separable kernel is used to
calculate the derivative. When ksize = 1 , the 3 times 1 or 1 times 3 kernel
is used (that is, no Gaussian smoothing is done). ksize = 1 can only be used
for the first or the second x- or y- derivatives.

if dx=0 and dy=1 or 2 , the filter is applied in the y direction and the horizontal lines are more prominent
if dx=1 or 2 and dy=0 , the filter is applied in the x direction and the vertical lines are more prominent

Sobel derivatives have the nice property that they can be defined for kernels of any
size, and those kernels can be constructed quickly and iteratively. The larger kernels
give a better approximation to the derivative because the smaller kernels are very sen-
sitive to noise.

What the Sobel operator actually represents is a fit to a polynomial. That is, the Sobel deriva-
tive of second order in the x-direction is not really a second derivative; it is a local fit to a
parabolic function. This explains why one might want to use a larger kernel: that larger
kernel is computing the fit over a larger number of pixels.

The downside of the sobel operation is that it is less accurate for small kernels. 

cv2.Scharr(src, ddepth, dx, dy[, dst[, scale[, delta[, borderType]]]]) → dst

	- the arguments are the same as sobel() but the kernel is fixed as the scharr filter



"""

img=cv2.imread('boi.jpg',cv2.IMREAD_GRAYSCALE)
imsobely=cv2.Sobel(img,-1,0,1,3)  # only horizontal remain since the deriv is d/dy
imsobelx=cv2.Sobel(img,-1,1,0,3)  # only vertical remain since the deriv is d/dx
imsobelxy=cv2.Sobel(img,-1,0,1,3)  # only points with both changing x and y remain since the deriv is d2/dxdy
imscharrx=cv2.Sobel(img,-1,1,0,-1)  # only vertical remain since the deriv is d/dx
imscharry=cv2.Sobel(img,-1,0,1,-1) # only horizontal remain since the deriv is d/dy
cv2.imshow('image',imsobelx)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',imsobely)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',imsobelxy)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',imscharrx)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('image',imscharry)
cv2.waitKey(0)
cv2.destroyAllWindows()

# LAPLACIAN

"""

cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]]) → dst

	src - source image
	ddepth - output image depth ( -1 for same ddepth )

The laplacian operator uses the operation d2/dx2 + d2/dy2

The function calculates the Laplacian of the source image by adding up the
second x and y derivatives calculated using the Sobel operator:

This is done when ksize > 1 . When ksize == 1 , the Laplacian is computed by
filtering the image with a 3x3 matrix 

It can also be used as a kind of edge detector. 

 """

imlap=cv2.Laplacian(img,-1)
cv2.imshow('image',imlap)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

When using uint8 images., the transitions from black to white are taken as
positive whereas the transitions from white to black are taken as negative. So
you miss the negative values. Hence it is better to use cv2.CV_64F or
cv2.CV_16S depth in the sobel or laplacian operations and then convert them to
uint8 afterwords.

Converting can be done by taking an absolute value and then converting to
cv2.CV_8U or using the function below

"""

imx64sobely = cv2.Sobel(img,cv2.CV_64F,0,1,3)
imx64sobely_abs=np.absolute(imx64sobely)
im8usobel=np.uint8(imx64sobely_abs)

"""

In order to avoid overflow it is better to use 16bit depth instead of the
source ( assuming it is 8bit ) in order to avoid overflow . After applying the derivative operations, 
you can convert it back to 8bit by using the function :

cv2.convertScaleAbs(src[, dst[, alpha[, beta]]]) → dst

	alpha - scale factor 
	beta - added after scaling

It converts an any-depth image to an 8bit range.

"""