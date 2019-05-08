import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

"""

Use the function cv2.imread() to read an image. The image should be in the
working directory or a full path of image should be given.

Second argument is a flag which specifies the way image should be read.

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

"""

img1 = cv2.imread('image_0001.jpg',0)
img2 = cv2.imread('image_0002.jpg',1)
img3 = cv2.imread('image_0003.jpg',-1)

"""

Use the function cv2.imshow() to display an image in a window. The window
automatically fits to the image size.

First argument is a window name which is a string. second argument is our
image. You can create as many windows as you wish, but with different window
names.

"""

cv2.imshow('image1',img1)
cv2.imshow('image2',img2)
cv2.imshow('image3',img3)

cv2.waitKey(0) # waits for key pressed, millisecond argument, 0 infinite wait
cv2.destroyWindow('image1') # destroy argument window
cv2.waitKey(0)
cv2.destroyAllWindows() # destroy all windows created at once

"""

There is a special case where you can already create a window and load image
to it later. In that case, you can specify whether window is resizable or not.
It is done with the function cv2.namedWindow(). By default, the flag is
cv2.WINDOW_AUTOSIZE. But if you specify flag to be cv2.WINDOW_NORMAL, you can
resize window. It will be helpful when image is too large in dimension and
adding track bar to windows.

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

"""

Use the function cv2.imwrite() to save an image.

First argument is the file name, second argument is the image you want to save.

"""

# Example program

img = cv2.imread('messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0) & 0xFF
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()

"""

Displaying using matplotlib

There is a slight difference in pixel ordering in OpenCV and Matplotlib.

OpenCV follows BGR order, while matplotlib likely follows RGB order.

Do this to convert: 

	img2 = img[:,:,::-1]

	cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

from matplotlib import pyplot as plt

img = cv2.imread('image_0001.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()

"""

