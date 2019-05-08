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

# SOBEL AND SCHARR DERIVATIVES

