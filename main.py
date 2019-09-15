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
import statistics
from scipy import ndimage as ndi

initial  = Image.open('C:/Users/dtket/.spyder-py3/Capture.png')
plt.imshow(initial)
plt.show()
init_arr = np.array(initial)
#init_arr = ndi.gaussian_filter(init_arr, 10)
height=init_arr.shape[0]
width=init_arr.shape[1]
crop = 85      # EXPERIMENTAL PARAMETER
left, top, right, bottom = 0, crop, width, height
cropped = initial.crop( ( left, top, right, bottom ) )
crop_arr = np.array(cropped)
gray_image = rgb2gray(crop_arr)

sigma = 5     # EXPERIMENTAL PARAMETER
edges = feature.canny(gray_image, sigma,25.5,51)
plt.imshow(edges)
plt.show()
histogram = np.sum(edges[edges.shape[0]//2:,:], axis=0)
plt.plot(histogram)
plt.show()
#plt.imshow(edges)
#plt.show()




#PLOTTING
global_thresh = threshold_otsu(gray_image)
binary_global = gray_image > global_thresh
test = np.sum(binary_global[binary_global.shape[0]//2:,:], axis=0)
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

cray = test
avg = 0
count = 0

for r in range(test.shape[0]):
    if test[r] > 25:
        cray[r] = 1
        avg = avg + r
        count = count + 1
    else:
        cray[r] = 0
        
        
avg = avg/count
center = width/2
plt.plot(cray)
plt.show()
err = (avg - center)

print("difference between camera center and track center is", err)




