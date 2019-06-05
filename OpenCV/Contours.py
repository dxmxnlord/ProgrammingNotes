import os
import numpy as np 
import cv2
from matplotlib import pyplot as plt


os.chdir("/home/rishikesh/Desktop/101_ObjectCategories")
os.chdir("./airplanes")

"""

Contours can be explained simply as a curve joining all the continuous points
(along the boundary), having same color or intensity

For better accuracy, use binary images. So before finding contours, apply
threshold or canny edge detection. findContours function modifies the source
image. So if you want source image even after finding contours, already store
it to some other variables. In OpenCV, finding contours is like finding white
object from black background. So remember, object to be found should be white
and background should be black.

cv2.findContours(image, mode, method) → image, contours, hierarchy

mode –
	Contour retrieval mode (if you use Python see also a note below).

	CV_RETR_EXTERNAL retrieves only the extreme outer contours. It sets
	hierarchy[i][2]=hierarchy[i][3]=-1 for all the contours. 

	CV_RETR_LIST retrieves all of the contours without establishing any hierarchical
	relationships.

	CV_RETR_CCOMP retrieves all of the contours and organizes them into a
	two-level hierarchy. At the top level, there are external boundaries of the
	components. At the second level, there are boundaries of the holes. If there
	is another contour inside a hole of a connected component, it is still put at
	the top level.

	 CV_RETR_TREE retrieves all of the contours and reconstructs a
	full hierarchy of nested contours. This full hierarchy is built and shown in
	the OpenCV contours.c demo.


method –
	Contour approximation method (if you use Python see also a note below).

	CV_CHAIN_APPROX_NONE stores absolutely all the contour points. That is, any 2
	subsequent points (x1,y1) and (x2,y2) of the contour will be either
	horizontal, vertical or diagonal neighbors, that is,
	max(abs(x1-x2),abs(y2-y1))==1.

	CV_CHAIN_APPROX_SIMPLE compresses horizontal,
	vertical, and diagonal segments
	and leaves only their end points. For example, an up-right rectangular
	contour is encoded with 4 points.
	
	CV_CHAIN_APPROX_TC89_L1,CV_CHAIN_APPROX_TC89_KCOS applies one of the flavors
	of the Teh-Chin chain approximation algorithm.

there are three arguments in cv2.findContours() function, first one is source
image, second is contour retrieval mode, third is contour approximation
method. And it outputs the image, contours and hierarchy. contours is a Python
list of all the contours in the image. Each individual contour is a Numpy
array of (x,y) coordinates of boundary points of the object.

The hierarchy is the contour appproximation. If you pass
cv2.CHAIN_APPROX_NONE, all the boundary points are stored. But actually do we
need all the points? For eg, you found the contour of a straight line. Do you
need all the points on the line to represent that line? No, we need just two
end points of that line. This is what cv2.CHAIN_APPROX_SIMPLE does. It removes
all redundant points and compresses the contour, thereby saving memory.



To  actually draw the contours we use the function:

cv2.drawcontour(srcimg,contour,contourno,color,thickness)

contourno - ith contour to be shown ( -1 to draw all contours)
color - tuple of rgb
thickness line thickness

"""
img=cv2.imread('toi.jpg',cv2.IMREAD_GRAYSCALE)
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,35,0)
contour,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.imshow('image',thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()
imag = cv2.drawContours(img, contour, -1, (0,255,0), 3)
cv2.imshow('image',imag)
cv2.waitKey(0)
cv2.destroyAllWindows()

# CONTOUR FEATURES

"""

In image processing, computer vision and related fields, an image moment is a
certain particular weighted average (moment) of the image pixels' intensities,
or a function of such moments, usually chosen to have some attractive property
or interpretation.

They are raw moments:

	M[i,j] = sigmax sigmay x^i . y^j . I (x,y)

	whre I is the intensity function with x and y 

	from this we get :

		Area = M[0,0] or cv2.contourArea(contourvector)
		Centroid( xbar , ybar ) = { M[1,0]/M[0,0] , M[0,1]/M[0,0] }

Central Moments :

	mu[i,j] = sigmax sigmay ( x - xbar ) ^ i . ( y - ybar ) ^ j . I (x,y)
	mu[0,0]=M[0,0]
	mu[0,11 = mu[1,0] = 0
	mu[1,1] = M[1,1] - xbar . M[0,1]

	or a general formula: 

		mu[p,q] = sigmam->p sigman->q ( p m )' . ( q n )' . ( -xbar ) ^ ( p - m ) . ( -ybar ) ^ ( q - n ) . M[m,n] 

cv2.moments(contourvector) - takes a single contour vector on returns a dictionary with its moment values

cv2.arcLength(contourvector,bool) - perimeter of contour; true if closed; false if an open curve

"""

img=cv2.imread('toi.jpg',cv2.IMREAD_GRAYSCALE)
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,35,0)
contour,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
sample=contour[4]
moment=cv2.moments(sample)
print(moment['m00'],moment['mu20'])
centroidx=moment['m10']/moment['m00']
centroidy=moment['m01']/moment['m00']
area=moment['m00']

# CONTOUR APPROXIMATION 

"""

It approximates a contour shape to another shape with less number of vertices
depending upon the precision we specify. It is an implementation of
Douglas-Peucker algorithm. Check wikipedia. 

The starting curve is an ordered set of points or lines and the distance
dimension ε > 0.

The algorithm recursively divides the line. Initially it is given all the
points between the first and last point. It automatically marks the first and
last point to be kept. It then finds the point that is furthest from the line
segment with the first and last points as end points; this point is obviously
furthest on the curve from the approximating line segment between the end
points. If the point is closer than ε to the line segment, then any points not
currently marked to be kept can be discarded without the simplified curve
being worse than ε.

If the point furthest from the line segment is greater than ε from the
approximation then that point must be kept. The algorithm recursively calls
itself with the first point and the furthest point and then with the furthest
point and the last point, which includes the furthest point being marked as
kept.

When the recursion is completed a new output curve can be generated consisting
of all and only those points that have been marked as kept.

The  second argument is called epsilon, which is maximum distance from contour
to approximated contour. It is an accuracy parameter. A wise selection of
epsilon is needed to get the correct output.

cv2.approxPolyDP(vector,epsion.bool) is the function

"""

img=cv2.imread('toi.jpg',cv2.IMREAD_GRAYSCALE)
thresh=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
cv2.THRESH_BINARY,35,0)
contour,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
sample=contour[4]

epsilon=0.1*cv2.arcLength(sample,True) # epsilon is 10% of arc length
approx1 = cv2.approxPolyDP(sample,epsilon,True)
epsilon=0.01*cv2.arcLength(sample,True) # epsilon is 1% of arc length
approx2 = cv2.approxPolyDP(sample,epsilon,True)

# CONVEX HULL

"""

Here, cv2.convexHull() function checks a curve for convexity defects and
corrects it. Generally speaking, convex curves are the curves which are always
bulged out, or at-least flat. And if it is bulged inside, it is called
convexity defects.

cv2.convexHull(points,returnpoints=true)

	points  - the contour vector
	returnPoints : By default, True. Then it returns the coordinates of the hull points. If False, it returns the indices of contour points corresponding to the hull points.

But if you want to find convexity defects, you need to pass returnPoints = False
Discussed later on.

"""

sample=cv2.convexHull(sample)
imag = cv2.drawContours(img, [sample], -1, (0,255,0), 3)


# CHECK CONVEXITY

"""

There is a function to check if a curve is convex or not,
cv2.isContourConvex(vector). It just return whether True or False.

"""

# BOUNDING SHAPES

"""

Straight bounding rectangle:

	It is a straight rectangle, it doesn’t consider the rotation of the object.
	So area of the bounding rectangle won’t be minimum.

	cv2.boundingRect(vector) - returns the top left coordinate and the width and height

	Then you can use the rectangle function to plot it

Rotated bounding rectangle :

	Here, bounding rectangle is drawn with minimum area, so it considers the
	rotation also. It returns a Box2D structure which contains following detals -
	( top-left corner(x,y), (width, height), angle of rotation.But to draw this
	rectangle, we need 4 corners of the rectangle

Minimum bounding circle:

	It is a circle which completely covers the object with minimum area.
	Get the centre tuple and radius and plot the circle.

Fitting an elipse: 

	It returns the rotated rectangle in which the ellipse is inscribed.
	Get the ellipse with the fusampleion and plot

Fitting a line:

	Similarly we can fit a line to a set of points. If an image contains a set of
	white points, we can approximate a straight line to it.
	Draw the line with the line function
	
"""

x,y,w,h=cv2.boundingRect(sample)
image=cv2.rectangle(thresh,(x,y),(x+w,y+h),(0,255,0),2) # draw rectangle

rect = cv2.minAreaRect(sample) # Box2D structure
box = cv2.boxPoints(rect) # gets the 4 edge points
box = np.int0(box) # makes a numpy array int0~=int64
image = cv2.drawContours(imgage,[box],0,(0,0,255),2)

(x,y),radius = cv2.minEnclosingCircle(sample)
center = (int(x),int(y))
radius = int(radius)
img = cv2.circle(img,center,radius,(0,255,0),2) # draw circle

ellipse = cv2.fitEllipse(sample) # returns (x,y),(MajAxis,MinAxis),angle
image = cv2.ellipse(image,ellipse,(0,255,0),2)

# rows,cols = img.shape[:2]
# [vx,vy,x,y] = cv2.fitLine(sample, cv2.DIST_L2,0,0.01,0.01)
# lefty = int((-x*vy/vx) + y)
# righty = int(((cols-x)*vy/vx)+y)
# img = cv2.line(img,(cols-1,righty),(0,lefty),(0,255,0),2)

# CONTOUR PROPERTIES

## ASPECT RATIO

"""

Ratio of width to heigtht of an image. 
For a contour get its surrounding rectangle and calculate.

"""

x,y,w,h = cv2.boundingRect(sample)
aspect_ratio = float(w)/h

## EXTENT

"""

Ratio of contour area to bounding rectangle area.

"""

x,y,w,h = cv2.boundingRect(sample)
conArea=cv2.contourArea(sample)
extent=float(conArea)/(w*h)

## SOLIDITY

"""

Solidity is the ratio of contour area to its convex hull area.

"""

conArea=cv2.contourArea(sample)
hull = cv2.convexHull(sample)
hull_area = cv2.contourArea(hull)
solidity = float(area)/hull_area

## EQUIVALENT DIAMETER

""" 
Equivalent Diameter is the diameter of the circle whose area is same as
the contour area. That is root of 4 times Contour Area by PI

"""

area = cv2.contourArea(sample)
equi_diameter = np.sqrt(4*area/np.pi)

## ORIENTATION

"""
Orientation is the angle at which object is directed. Use fit ellipse.

"""

(x,y),(MA,ma),angle = cv2.fitEllipse(sample)

## MASK AND PIXEL POINTS

"""
Gets all the points which comprises that object

"""

mask = np.zeros(imgray.shape,np.uint8)
cv2.drawContours(mask,[sample],0,255,-1)
pixelpoints = np.transpose(np.nonzero(mask))  # gets only non zero points ie object
alsopixelpoints = cv2.findNonZero(mask) # alternate way

"""

Results are also same, but with a slight difference. Numpy gives coordinates
in (row, column) format, while OpenCV gives coordinates in (x,y) format. So
basically the answers will be interchanged. Note that, row = x and column = y.

"""

## MAX AND MIN VALUE AND LOCATION

"""

you can use a mask to find it in a particular area too with a [mask=mask] arg

"""

min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(imgray)

## MEAN COLOR OR AVERAGE INTENSITY FOR GS

mean_val = cv2.mean(img)

## EXTREME POINTS

leftmost = tuple(sample[sample[:,:,0].argmin()][0])
rightmost = tuple(sample[sample[:,:,0].argmax()][0])
topmost = tuple(sample[sample[:,:,1].argmin()][0])
bottommost = tuple(sample[sample[:,:,1].argmax()][0])

# CONVEXITY DEFECTS

