# -*- coding: utf-8 -*-
"""
Created

@author: dtketterer
"""
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from scipy import ndimage
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
file_string_start = 'C:/Users/dtket/.spyder-py3//Photos/pic ('
file_string_end   = ').jpg'


def smoothTriangle(data, degree):
    triangle=np.concatenate((np.arange(degree + 1), np.arange(degree)[::-1])) # up then down
    smoothed=[]

    for i in range(degree, len(data) - degree * 2):
        point=data[i:i + len(triangle)] * triangle
        smoothed.append(np.sum(point)/np.sum(triangle))
    # Handle boundaries
    smoothed=[smoothed[0]]*int(degree + degree/2) + smoothed
    while len(smoothed) < len(data):
        smoothed.append(smoothed[-1])
    return smoothed

#def func(data, center, eps):
#    for x,y in data:
#        if (center-eps < x < center+eps ):
#            indicator(x,y)=1
#        else:
#            indicator(x,y)=0
#    return indicator


for num in range(190):
 filename = file_string_start+str(num)+file_string_end
 initial  = Image.open(filename)


 init_arr       =  np.array(initial)

 gray_image     =  rgb2gray(init_arr)

 global_thresh  =  threshold_otsu(gray_image)

 binary_global  =  gray_image > global_thresh

 histogram      =  np.sum(binary_global[binary_global.shape[0]//2:,:], axis=0)

 standard       =  np.std(histogram, axis=0)

 global_thresh2 =  threshold_otsu(histogram) + standard
 
 binary_global2 =  histogram > global_thresh2
 
# tester=smoothTriangle(histogram, 120)
 
 camera_center  =  binary_global2.shape[0]/2

 track_center   =  ndimage.measurements.center_of_mass(binary_global2)

 err = track_center[0] - camera_center





# Basically do the same but on a reduced set of the pixerls, ie sample every 10 or 130 or sop, we want 30 bins along the x and 10- 30 along the y




###PLOTTING
# fig, axes = plt.subplots(nrows=2, figsize=(7, 8))
# ax0, ax1 = axes
# plt.gray()
#
# ax0.imshow(gray_image)
# ax0.set_title('Image')
#
# ax1.imshow(binary_global)
# ax1.set_title('Global thresholding')
#
#
# for ax in axes:
#     ax.axis('off')
#
# plt.show()
# plt.gray()
# plt.imshow(binary_global)
# plt.show()
# plt.plot(histogram)
# plt.show()
 plt.plot(binary_global2)
 plt.show()
# plt.plot(tester)
# plt.show()
# plt.plot(tester2)
# plt.show()
 print(num,err,track_center[0],camera_center)
