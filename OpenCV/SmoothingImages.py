import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

"""

images also can be filtered with various low-pass filters (LPF), high-pass
filters (HPF), etc. A LPF helps in removing noise, or blurring the image. A
HPF filters helps in finding edges in an image.

OpenCV provides a function, cv2.filter2D(), to convolve a kernel with an image.

"""

# IMAGE FILTERING

"""

Uses a nxn ones matrix divided by n^2

ex. for each pixel, a 5x5 window is centered on this pixel, all pixels falling
within this window are summed up, and the result is then divided by 25. This
equates to computing the average of the pixel values inside that window. This
operation is performed for all the pixels in the image to produce the output
filtered image.

greater the kernel size, more the filtering as the pixels are averaged more

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_COLOR)
kernel=np.ones((5,5),dtype='float32')/25
dst=cv2.filter2D(img,-1,kernel) # -1 means the same depth as src img
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# IMAGE BLURRING / SMOOTHING

"""

Image blurring is achieved by convolving the image with a low-pass filter
kernel. It is useful for removing noise. It actually removes high frequency
content (e.g: noise, edges) from the image resulting in edges being blurred
when this is filter is applied

There are 4 types of filtering in openCV

"""

## AVERAGING

"""

This is done by convolving the image with a normalized box filter. It simply
takes the average of all the pixels under kernel area and replaces the central
element with this average. This is done by the function cv2.blur() or
cv2.boxFilter().

boxFilter args : 	srcimg		numpy array
					-1
					kernelsize	--> (n,n)
					normalize=	--> true/false

blur args :		srcimg
				kernelsize

blur() automatically uses a normalized kernel to smoothen an image 

blur() and boxFilter() are equivalent in this case

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_COLOR)
dst=cv2.blur(img,(3,3)) # 3x3 kernel
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 

## GAUSSIAN FILTERING

"""

The central difference, depending on algorithm, is that Gaussian blur takes a
weighted average around the pixel, while normal "box" blur just averages all the
pixels in the radius of the single pixel together 

In this approach, instead of a box filter consisting of equal filter
coefficients, a Gaussian kernel is used. It is done with the function,
cv2.GaussianBlur()

You have to specify the kernel size (the width and height CAN differ but they have to both
be odd and positive), std deviation in X direction [, std deviation in Y direction (if its
0, it is set equal to stdX; if both are 0, they are calculated from the kernel) ]

If you want, you can create a Gaussian kernel with the function, cv2.getGaussianKernel().

Gaussian filtering is highly effective in removing Gaussian noise from the image.

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_COLOR)
dst=cv2.GaussianBlur(img,(3,3),0) # 3x3 kernel
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 

# MEDIAN FILTERING

"""

Here, the function cv2.medianBlur() computes the median of all the pixels
under the kernel window and the central pixel is replaced with this median
value. This is highly effective in removing salt-and-pepper noise.

One interesting thing to note is that, in the Gaussian and box filters, the
filtered value for the central element can be a value which may not exist in
the original image. However this is not the case in median filtering, since
the central element is always replaced by some pixel value in the image. This
reduces the noise effectively.

kernel size is an aperture linear size; it must be odd and greater than 1

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_COLOR)
dst=cv2.medianBlur(img,3)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 

## BILATERAL FILTER

""" 

The Average,Gaussian, and Median filters all blur out edges. They do not
consider whether pixels have almost the same intensity value and do not
consider whether the pixel lies on an edge or not.

If you want the edges to remain, use the bilateral filter

The bilateral filter also uses a Gaussian filter in the space domain, but it
also uses one more Gaussian filter component which is a
function of pixel intensity differences

The Gaussian function of space makes sure that only pixels are ‘spatial
neighbors’ are considered for filtering, while the Gaussian component applied
in the intensity domain (a Gaussian function of intensity differences) ensures
that only those pixels with intensities similar to that of the central pixel
(‘intensity neighbors’) are included to compute the blurred intensity value

As a result, this method preserves edges, since for pixels lying near edges,
neighboring pixels placed on the other side of the edge, and therefore
exhibiting large intensity variations when compared to the central pixel, will
not be included for blurring.

bilateralfilter() args :	srcimg
							d 		--> diameter of each pixel neighbourhood
							sigmaColor	--> A larger value of the parameter means that farther colors within the pixel neighborhood will be mixed together, resulting in larger areas of semi-equal color.
							sigmaSpace	--> Filter sigma in the coordinate space. A larger value of the parameter means that farther pixels will influence each other as long as their colors are close enough.

"""

img=cv2.imread('roi.jpg',cv2.IMREAD_COLOR)
dst = cv2.bilateralFilter(img,9,75,75)
cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows() 

### NOTES FROM Gary Bradsky - Adrian Kaehler

"""

It is also called blurring, and is done to reduce noise or camera artefacts or
reduce the resolution in a proper way

// The actual function is now obsolete, but the theory still holds

cv.Smooth(src, dst, smoothtype=<type>, param1=3, param2=0, param3=0, param4=0)

	param1, param2 - size of the smoothing kernel(all 1s)
	param3 - color sigma
	param4 - spatial sigma

	smoothtype :

		CV_BLUR - Each pixel in the output is the simple mean of all of the pixels
		in a window around the corresponding pixel in the input. The scaling factor is
		1/(param1xparam2) which is what the sum of pixels is divided by, hence, the mean

		CV_BLUR_NO_SCALE - Same as the normal blur but with no scaling done. The src image
		should be only 8u where as the output image is 16u for 8u. It is faster than 
		normal blurring.

		CV_MEDIAN - Each pixel is replaced by its median pixel in a square neighbourhood
		around the center pixel. Normal blurring can be sensitive to noisy images with
		large isolated 'outlier-points' which unnecessarily bring up the mean, but the 
		median method overcomes this. Not as clean smoothing as normal blur

		CV_GAUSSIAN - Each pixel is convolved with a gaussian kernel and then summed
		up. The 3rd (half width at half max) and 4th sigma parameters of the kernel 
		are optional. If left blank (0,0), they are automatically determined. If the
		kernel is asymmetrical, they reperesent horizontal and vertical sigma values.
		If the 1st and 2nd params are zero but sigma params are not then their values
		are appropriately determined. Gaussian has higher optimization for the 3x3,
		5x5, 7x7 kernels with (0,0) sigma values. Main idea is that pixels in a real 
		image should vary slowly over space and thus be correlated to their neighbors.

		CV_BILATERAL - Edge-preserving smoothing process. Unlike the gaussian filter which 
		reduces noise since it varies greatly from one pixel to the next and gets adjusted
		by the mechanism, the very mechanism itself breaks down near the edges, where pixels
		are expected to be uncorrelated to their neighbours, and it smooths them as well.
		Like gaussian smoothing, a weighted average is constructed for a pixels and its 
		neighbours, but another compnent is used which is the difference in intensity from
		the center pixel. In a way, similar pixels are weighed more highly than dissimilar
		ones. The 1st param is width in spatial domain and 2nd is width in color domain.
		the larger the second parameter, the broader is the range of intensities that is 
		included in the smoothing.

		""" 

