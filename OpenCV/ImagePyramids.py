import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

# IMAGE PYRAMIDS

"""

Pyramids are a collection of images that are successively downsampled untill a
stopping point. There are two kinds: Gaussian and Laplacian pyramids. The
gaussian pyramids are used to downsample a image where as laplacian pyramids
are used to reconstruct an upsampled image from a lower image.

To downsample an image, we convolve it with a gaussian kernel then remove every even 
numbered row and column. As a result each image is one quarter of its predecessor. The
higher level is lower in resolution and the lower level is higher in resolution. Together
they make a gaussian pyramid. 

Laplacian Pyramids are formed from the Gaussian Pyramids. The formation of a
gaussian pyramid involves loss while going smaller in the size. In order to
restore the original (higher-resolution) image, we would require access to the
information that was discarded by the downsampling. This data forms the
Laplacian pyramid. The ith layer is defined as L[i] = G[i] - pyrUp(G[i+1])
where the subtraction is  cv2.subtract() and i+1 is the bigger image.

Similarily to reconstruct an image from a laplacian pyramid, successively


cv2.pyrDown(img) scales an image down 
cv2.pyrUp(img) scales an image up with loss compared to original

"""

img=cv2.imread('boi.jpg',cv2.IMREAD_COLOR)
lower_reso=cv2.pyrDown(img)
higher_reso=cv2.pyrUp(lower_reso) # loss occurs 

## building a gaussian pyramid

gaussian=[]
gaussian.append(img)
for cnt in range(1,4):
	gaussian.append(cv2.pyrDown(gaussian[cnt-1]))

## building a laplacian pyramid

laplacian=[]
for cnt in range(0,3):
	higher=cv2.pyrUp(gaussian[cnt+1])
	laplacian.append(cv2.subtract(gaussian[cnt],higher))
laplacian.append(gaussian[len(gaussian)-1])

# IMAGE BLENDING USING PYRAMIDS

"""

Load the two images of apple and orange
Find the Gaussian Pyramids for apple and orange (in this particular example, number of levels is 6)
From Gaussian Pyramids, find their Laplacian Pyramids
Now join the left half of apple and right half of orange in each levels of Laplacian Pyramids
Finally from this joint image pyramids, reconstruct the original image.

The joining is the inverse of the formation of the laplacian pyramid

"""

A = cv2.imread('roi.jpg')
B = cv2.imread('boi.jpg')
A = cv2.resize(A,(200,200))
B = cv2.resize(B,(200,200))

# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)

# generate Gaussian pyramid for B
G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A in a reverse order
lpA = [gpA[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1],GE)
    lpA.append(L)

# generate Laplacian Pyramid for B in a reverse order
lpB = [gpB[5]]
for i in range(5,0,-1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE)
    lpB.append(L)

# Now add left and right halves of images in each level
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    cols=cols/2
    cols=int(cols)
    ls = np.hstack((la[:,0:cols], lb[:,cols:]))
    LS.append(ls)

# now reconstruct the image by scaling up and adding
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# image with direct connecting each half
real = np.hstack((A[:,:cols],B[:,cols:]))

cv2.imwrite('Pyramid_blending2.jpg',ls_)
cv2.imwrite('Direct_blending.jpg',real)