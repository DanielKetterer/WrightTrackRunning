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

for num in range(100):
 filename = file_string_start+str(num)+file_string_end
 
 initial  = Image.open(filename)
 
 initial.thumbnail((304,405))
 
 init_arr       =  np.array(initial)

 gray_image     =  rgb2gray(init_arr)

 global_thresh  =  threshold_otsu(gray_image)

 binary_global  =  gray_image > global_thresh

 histogram      =  np.sum(binary_global[binary_global.shape[0]//2:,:], axis=0)

 standard       =  np.std(histogram, axis=0)

 global_thresh2 =  threshold_otsu(histogram) + standard
 
 binary_global2 =  histogram > global_thresh2
 
 camera_center  =  binary_global2.shape[0]/2

 track_center   =  ndimage.measurements.center_of_mass(binary_global2)

 err = track_center[0] - camera_center




###PLOTTING

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
