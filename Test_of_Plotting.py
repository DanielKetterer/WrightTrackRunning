# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 14:23:41 2021

@author: ecslogon
"""
import matplotlib.pyplot as plt
import numpy as np
err_array= []
err_dot_array = []
plt.figure()
N = 100
for index in range(N):      # will be replaced with our for loop over camera frames
    err = np.sin(index)*np.exp(-index/10)#   replace with calculated error
    err_dot = index*(100-index)#  replace with calculated err_dot
    

    #after computing error and err_dot plot them
    plt.subplot(211)
    err_array.append(err)
    plt.plot(err_array)
    
    plt.subplot(212)
    err_dot_array.append(err_dot)
    plt.plot(err_dot_array)
    
    plt.show()
    
    
    