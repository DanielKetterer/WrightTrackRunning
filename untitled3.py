# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 22:18:57 2019

@author: dtket
"""

import imageio as iio
from skimage import filters
from skimage.color import rgb2gray  # only needed for incorrectly saved images
from skimage.measure import regionprops
import matplotlib.pyplot as plt
from skimage.color import label2rgb

image = rgb2gray(iio.imread('cube.png'))
threshold_value = filters.threshold_otsu(image)
labeled_foreground = (image > threshold_value).astype(int)
properties = regionprops(labeled_foreground, image)
center_of_mass = properties[0].centroid
weighted_center_of_mass = properties[0].weighted_centroid


colorized = label2rgb(labeled_foreground, image, colors=['black'], alpha=0.1)
fig, ax = plt.subplots()
ax.imshow(colorized)
# Note the inverted coordinates because plt uses (x, y) while NumPy uses (row, column)
ax.scatter(center_of_mass[1], center_of_mass[0], s=160, c='C0', marker='+')
plt.show()
