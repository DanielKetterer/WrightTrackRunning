# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 19:41:51 2019

@author: dtket
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from skimage import data
from skimage.filters import threshold_otsu, threshold_adaptive
from skimage.color import rgb2gray
from skimage import feature
import statistics as st
from scipy import ndimage as ndi
from sklearn.cluster import KMeans
import skimage.segmentation as seg
from skimage.color import label2rgb


initial  = Image.open('C:/Users/dtket/.spyder-py3/Capture.png')
plt.imshow(initial)
plt.show()
init_arr = np.array(initial)
#init_arr = ndi.gaussian_filter(init_arr, 10)
height=init_arr.shape[0]
width=init_arr.shape[1]
crop = 90     # EXPERIMENTAL PARAMETER
left, top, right, bottom = 0, crop, width, height
cropped = initial.crop( ( left, top, right, bottom ) )
crop_arr = np.array(cropped)
gray_image = rgb2gray(crop_arr)

sigma = 5     # EXPERIMENTAL PARAMETER
edges = feature.canny(gray_image, sigma,None,None)
plt.imshow(edges)
plt.show()
histogram = np.sum(edges[edges.shape[0]//2:,:], axis=0)
plt.plot(histogram)
plt.show()



#PLOTTING
global_thresh = threshold_otsu(gray_image)
binary_global = gray_image > global_thresh
test = np.sum(binary_global[binary_global.shape[0]//2:,:], axis=0)


fig, ax = plt.subplots()
ax.imshow(colorized)
# Note the inverted coordinates because plt uses (x, y) while NumPy uses (row, column)
ax.scatter(center_of_mass[1], center_of_mass[0], s=160, c='C0', marker='+')
plt.show()
















#KMEANS
print("kmeans")
kmeans = KMeans(n_clusters=1,random_state = 0).fit(binary_global)
pic2show=kmeans.cluster_centers_[kmeans.labels_]
plt.imshow(pic2show)


#
sexything=seg.slic(initial,n_segments = 3)
plt.imshow(sexything)




fig, axes = plt.subplots(nrows=2, figsize=(7, 8))
ax0, ax1, = axes
plt.gray()

ax0.imshow(gray_image)
ax0.set_title('Image')

ax1.imshow(binary_global)
ax1.set_title('Global thresholding')


for ax in axes:
    ax.axis('off')

plt.show()
####

plt.plot(test)
plt.show()

sigma = 1    # EXPERIMENTAL PARAMETER
edges = feature.canny(binary_global, sigma,None,None)
plt.imshow(edges)
plt.show()
histogram = np.sum(edges[edges.shape[0]//2:,:], axis=0)
plt.plot(histogram)
plt.show()

global_thresh2 = threshold_otsu(histogram)
binary_global2 = histogram > global_thresh2
plt.plot(binary_global2)
plt.show()
ndi.measurements.center_of_mass(binary_global)
segments = slic(binary_global,n_segments=4, compactness=.1, enforce_connectivity=True)
plt.imshow(segments)


#
#cray = test
#avg = 0
##count = 0
#def LineMaker3000(graph):
# for c in range(graph.shape[0]):
#     for r in range(graph.shape[1]):
         
#avg = avg/count
#center = width/2
#plt.plot(cray)
#plt.show()
#err = (avg - center)
#
#print("difference between camera center and track center is", err)