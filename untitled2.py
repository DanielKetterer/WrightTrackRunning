# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 21:46:47 2019

@author: dtket
"""

# import the necessary packages
from skimage.segmentation import slic
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
from skimage import io
import matplotlib.pyplot as plt
import argparse
from PIL import Image
# construct the argument parser and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "Path to the image")
#args = vars(ap.parse_args())
# 
## load the image and convert it to a floating point data type

 
image  = Image.open('C:/Users/dtket/.spyder-py3/Capture.png')
plt.imshow(image)
plt.show()
image = img_as_float(image)
segments = slic(image,n_segments=10, compactness=0.1, enforce_connectivity=True)
plt.imshow(segments)
#
## loop over the number of segments
#for numSegments in (10, 2, 3):
#	# apply SLIC and extract (approximately) the supplied number
#	# of segments
#	segments = slic(image, n_segments = numSegments, sigma = 5)
# 
#	# show the output of SLIC
#	fig = plt.figure("Superpixels -- %d segments" % (numSegments))
#	ax = fig.add_subplot(1, 1, 1)
#	ax.imshow(mark_boundaries(image, segments))
#	plt.axis("off")
# 
## show the plots
#plt.show()