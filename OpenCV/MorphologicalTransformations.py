import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

"""

Morphological transformations are some simple operations based on the image
shape. It is normally performed on binary images. It needs two inputs, one is
our original image, second one is called structuring element or kernel which
decides the nature of operation.

"""

img=cv2.imread('roi.jpg',cv2.GRAYSCALE)
bimg=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,0)
cv2.imshow('img',mask)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

We can manually create structuring elements with help
of Numpy. It is rectangular shape. But in some cases, you may need
elliptical/circular shaped kernels. So for this purpose, OpenCV has a
function, cv2.getStructuringElement(). You just pass the shape and size of the
kernel, you get the desired kernel.

The types are :	MORPH_RECT, MORPH_ELLIPSE, MORPH_CROSS

"""

Rkernel=cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
Ekernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
Ckernel=cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))

# EROSION

"""

The kernel slides through the image (as in 2D convolution). A pixel in the
original image (either 1 or 0) will be considered 1 only if all the pixels
under the kernel is 1, otherwise it is eroded (made to zero).

So what happends is that, all the pixels near boundary will be discarded
depending upon the size of kernel. So the thickness or size of the foreground
object decreases or simply white region decreases in the image. It is useful
for removing small white noises (as we have seen in colorspace chapter),
detach two connected objects etc.

the no of times to iterate and erode can be specified

"""

kernel=np.ones((5,5),dtype='uint8')
eimg=cv2.erode(bimg,kernel,iterations=1)
cv2.imshow('img',eimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# DILATION

"""

Has the opposite effect of erosion

Here, a pixel element is ‘1’ if atleast one pixel under the kernel is ‘1’. So
it increases the white region in the image or size of foreground object
increases. 

Normally, in cases like noise removal, erosion is followed by dilation.
Because, erosion removes white noises, but it also shrinks our object. So we
dilate it. Since noise is gone, they won’t come back, but our object area
increases. It is also useful in joining broken parts of an object.

"""

kernel=np.ones((3,3),dtype='uint8')
dimg=cv2.dilate(bimg,kernel,iterations=1)
cv2.imshow('img',dimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

# OPENING / CLOSING / GRADIENT

"""

Opening is erosion followed by dilation and is useful in removing noise.
Structured removal of image region boundary pixels

Closing is reverse of Opening, Dilation followed by Erosion. It is useful in
closing small holes inside the foreground objects, or small black points on
the object. Structured filling in of image region boundary pixels

Gradient is the difference between dilation and erosion of an image.The result
will look like the outline of the object.

Tophat is the difference between input image and Opening of the image.

Black hat is the difference between the closing of the input image and input image.

morphologyEx(src,operation,kernel[,iterations=])

operation: 	MORPH_OPEN - an opening operation
			MORPH_CLOSE - a closing operation
			MORPH_GRADIENT - a morphological gradient
			MORPH_HITMISS - “hit and miss”
			MORPH_TOPHAT - “top hat”
			MORPH_BLACKHAT - “black hat”

"""

kernel=np.ones((3,3),dtype='uint8')
oimg=cv2.morphologyEx(bimg, cv2.MORPH_OPEN, kernel)
cimg=cv2.morphologyEx(bimg, cv2.MORPH_CLOSE, kernel)
gimg=cv2.morphologyEx(bimg, cv2.MORPH_GRADIENT, kernel)
timg=cv2.morphologyEx(bimg, cv2.MORPH_TOPHAT, kernel)
bhimg=cv2.morphologyEx(bimg, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow('img',oimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('img',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('img',gimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('img',timg)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imshow('img',bhimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

### NOTES FROM Gary Bradsky - Adrian Kaehler

"""

Dilation is when you convolve some image with a kernel of any shape and size and an
anchor point(usually centre). The maximum value of in the kernel replaces the pixel
at the anchor. This causes bright regions to grow and dark to shrink. It is mostly
used with binary images after thresholding.

Erosion is the almost the same as dilation except it takes the minimum pixel value.

In general, whereas dilation expands region A, erosion reduces region A. Moreover, di-
lation will tend to smooth concavities and erosion will tend to smooth away protrusions.
Of course, the exact result will depend on the kernel, but these statements are generally
true for the fi lled convex kernels typically used. 

The erode operation is often used to eliminate “speckle” noise in an image.
The idea here is that the speckles are eroded to nothing while larger regions
that contain visually significant content are not affected. The dilate
operation is often used when attempting to find connected components (i.e.,
large discrete regions of similar pixel color or intensity). The utility of
dilation arises because in many cases a large region might otherwise be broken
apart into multiple components as a result of noise, shadows, or some other
similar effect. A small dilation will cause such components to “melt”
together into one.

These two are well-suited for binary images/masks but grayscale/color can use additional
operations. 

Opening is erosion followed by dilation. Opening is often used to separate closely
spaced identfiable parts of a binary image.

Closing is dilation followed by erosion. For connected components, usually an
erosion or closing operation is performed first to eliminate elements that
arise purely from noise and then an opening operation is used to connect
nearby large regions.

Although the end result of using open or close is similar to
using erode or dilate, these new operations tend to preserve the area of
connected regions more accurately. 

Both the opening and closing operations are approximately area-preserving: the
most prominent effect of closing is to eliminate lone outliers that are lower
than their neighbors whereas the effect of opening is to eliminate lone
outliers that are higher than their neighbors.

Ex.

	200	100	250	240	230	150 --> original intensities

Opening:

	100	100	100	240	150	150 --> erode (minimum intensity in kernel but here adjacent-to)

	100	100	240	240	240	150 --> dilate = opening

Closing: 

	200	250	250	250	240	230 --> dilate (max intensity bw left and right selected)

	200	200	250	240	230	230 --> erode = closing 

n iterations perform n dilations/erosions then 'n' erosions/dilations not alternatively.

The gradient is [ dilate - erode ] operation. It isolates perimeters of bright
regions. The complete perimeter of a region tends to be found because an
expanded version is subtracted from a contracted version of the region,
leaving a complete perimeter edge. 

The tophat is [ src - open ] operation. Whereas blackhat is [ close - src ]
operation. Tophat reveals areas that are lighter than the surrounding region.
The  bright local peaks are isolated. By isolated I mean that they exist in
the resultant image. Blackhat reveals areas that are darker than the 
surrounding region. The dark holes are isolated and are shown in the resultant
image. The rest of the image is empty. 

"""
