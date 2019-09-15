# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 17:54:12 2019

@author: dtket
"""
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from scipy import misc
from PIL import Image, ImageEnhance 
from skimage import feature
from skimage import io
from skimage.color import rgb2gray


im  = Image.open('C:/Users/dtket/.spyder-py3/Captureline.png')
enhancer = ImageEnhance.Contrast(im)
eim = enhancer.enhance(20.0)
eim.save("Capture7.png")
imw = np.array(eim)
imw = ndi.gaussian_filter(imw, 10)

#def color_thresh_combined(img, s_thresh, l_thresh, v_thresh, b_thresh):
#    V_binary = HSV_thresh(img, v_thresh)
#    S_binary = HLS_thresh(img, s_thresh)
#    L_binary = LUV_thresh(img, l_thresh)
#    color_binary = np.zeros_like(V_binary)                           
#    color_binary[(V_binary == 1) & (S_binary == 1) & (L_binary == 1)] = 1
#return color_binary




height=imw.shape[0]
width=imw.shape[1]
left, top, right, bottom = 0, 100, width-4, height-4
cropped = im.crop( ( left, top, right, bottom ) )  # size: 45, 45

imw2 = np.array(cropped)
finalimage = rgb2gray(imw2)
edges = feature.canny(finalimage, sigma=5)
#misc.imsave('cube.png', im) # uses the Image module (PIL)
plt.imshow(edges)
plt.show()

histogram = np.sum(edges[edges.shape[0]//2:,:], axis=0)
plt.plot(histogram)
t=statistics.median(histogram)
tt=sum(histogram)/histogram.shape[0]


# Generate noisy image of a square
#im = np.zeros((128, 128))
#im[32:-32, 32:-32] = 1
#
#im = ndi.rotate(im, 15, mode='constant')

##im += 0.2 * np.random.random(im.shape)
#
## Compute the Canny filter for two values of sigma
#
#
#
#edges1 = feature.canny(im)
#edges2 = feature.canny(im, sigma=3)
#
## display results
#fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
#                                    sharex=True, sharey=True)
#
#ax1.imshow(im, cmap=plt.cm.gray)
#ax1.axis('off')
#ax1.set_title('noisy image', fontsize=20)
#
#ax2.imshow(edges1, cmap=plt.cm.gray)
#ax2.axis('off')
#ax2.set_title('Canny filter, $\sigma=1$', fontsize=20)
#
#ax3.imshow(edges2, cmap=plt.cm.gray)
#ax3.axis('off')
#ax3.set_title('Canny filter, $\sigma=3$', fontsize=20)
#
#fig.tight_layout()
#
#plt.show()
