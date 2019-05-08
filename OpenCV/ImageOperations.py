import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

# ACCESS AND MODIFY PIXEL VALUES

"""

You can access a pixel value by its row and column coordinates.
For BGR image, it returns an array of Blue, Green, Red values.
For grayscale image, just corresponding intensity is returned.

for an image read in bgr: 
	>> img[x-pix,y-pix] --> [b-val g-val r-val]
for an image read in grayscale:
	>> img[x-pix,y-pix] --> intensity

"""

img=cv2.imread('image_0001.jpg',1)
px=img[50,50]
px2=img[0:50,0:50]
print(px)
img[50,50]=[255,0,255]
print(px)
img=cv2.imread('image_0001.jpg',0)
gpx=img[50,50]
gpx2=img[0:50,0:50]
print(gpx)
img[50,50]=50
print(gpx)

img=cv2.imread('image_0001.jpg',1)
# accessing only r or g or b value of a pixel
bluepx=img[50,50,0]
greenpx=img[50,50,1]
redpx=img[50,50,2]

"""

The above mentioned method is normally used for selecting a region of array, say
first 5 rows and last 3 columns like that. For individual pixel access, Numpy
array methods, array.item() and array.itemset() is considered to be better.
But it always returns a scalar. So if you want to access all B,G,R values, you
need to call array.item() separately for all.

Better pixel accessing and editing method :

# accessing RED value
>>> img.item(10,10,2)
59

# modifying RED value
>>> img.itemset((10,10,2),100)
>>> img.item(10,10,2)
100

"""

# IMAGE PROPERTIES

"""

Shape of image is accessed by img.shape. It returns a tuple of number of rows,
columns and channels (if image is color)

Total number of pixels is accessed by img.size

Image datatype is obtained by img.dtype

"""

print(img.shape) # (xdim,ydim,NofC) ; NofC = 3{RGB ~ 1}, 4{ARGB ~ -1} ; if GS, no third argument(good GS test)
print(img.size)
print(img.dtype) #img.dtype is very important while debugging because a large number of errors in OpenCV-Python code is caused by invalid datatype.

# REGION OF IMAGES

area=img[0:50,50:100]
img[50:100,100:150]=area # Should be same size
cv2.imshow('image1',img)
cv2.waitKey(0)
cv2.destroyWindow('image1')

img=cv2.imread('image_0001.jpg',1)

img[0:50, 50:100]=np.full((50,50,3),255,dtype='uint8') # manually changing pixels

img[0:50,50:100,0] = 255
img[0:50,50:100,1] = 255 #same effect
img[0:50,50:100,2] = 255

# SPLITTING AND MERGING CHANNELS

"""

The B,G,R channels of an image can be split into their individual planes when
needed. Then, the individual channels can be merged back together to form a
BGR image again. 

cv2.split() is a costly operation (in terms of time), so only use it if
necessary. Numpy indexing is much more efficient and should be used if
possible.

"""

img=cv2.imread('image_0001.jpg',1)
blue,green,red = cv2.split(img)
img = cv2.merge((blue,green,red))

# ADDING BORDERS TO IMAGES OR TO PARTS OF AN IMAGES

"""

If you want to create a border around the image, something like a photo frame,
you can use cv2.copyMakeBorder() function. But it has more applications for
convolution operation, zero padding etc. This function takes following
arguments:

	src - input image
	top, bottom, left, right - border width in number of pixels in corresponding directions
	borderType - Flag defining what kind of border to be added. It can be following types:
		cv2.BORDER_CONSTANT - Adds a constant colored border. The value should be given as next argument.
		cv2.BORDER_REFLECT - Border will be mirror reflection of the border elements, like this : fedcba|abcdefgh|hgfedcb
		cv2.BORDER_REFLECT_101 or cv2.BORDER_DEFAULT - Same as above, but with a slight change, like this : gfedcb|abcdefgh|gfedcba
		cv2.BORDER_REPLICATE - Last element is replicated throughout, like this: aaaaaa|abcdefgh|hhhhhhh
		cv2.BORDER_WRAP - Can’t explain, it will look like this : cdefgh|abcdefgh|abcdefg
	value - Color of border if border type is cv2.BORDER_CONSTANT

"""
img1=cv2.imread('image_0001.jpg',1)

replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=[255,0,0])

cv2.imshow('image',replicate)
# cv2.imshow('image',reflect)
# cv2.imshow('image',reflect101)
# cv2.imshow('image',wrap)
# cv2.imshow('image',constant)
cv2.waitKey(0)
cv2.destroyWindow('image')