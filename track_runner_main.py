# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 13:07:21 2021

@author: Daniel Ketterer
"""

import numpy as np
import cv2
from datetime import datetime

from gpiozero import Motor
import matplotlib.pyplot as plt
from picamera.array import PiRGBArray
from picamera import PiCamera

from scipy import ndimage
from skimage.filters import threshold_otsu
from skimage.color import rgb2gray
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT) #speed control
GPIO.setup(16, GPIO.OUT) #steering
GPIO.setup(11 , GPIO.IN, pull_up_down=GPIO.PUD_UP)

print ("Waiting for 2 seconds")
time.sleep(2)
start = time.time()
old_err = 0
speedcontroller = GPIO.PWM(12,72)
speedcontroller.start(0)
steering = GPIO.PWM(16,72)
steering.start(0)
def get_video_filename():
    return 'test_video.h264'
# the timestamp when the video write started
video_time  = 0
# main logic
def InterruptHandler(channel):
  # Called if sensor output changes
  global start
  global speed
#   stamp = datetime.datetime.fromtimestamp(timestamp).strftime('%H:%M:%S')
  if GPIO.input(channel):
    # No magnet
     print("initializing")

  else:
    # Magnet
    end = time.time()
    T = end - start
    speed = (2*3.14159*3)/(44.704*T) # in cm per second
    print("Magnet detected, Sensor LOW")
    print("Speed " + str(speed)+" mph")
    start = time.time()
def steer(err,T):
     global old_err
#start PWM running, but with value of 0 (pulse off)
#      speedcontroller.start(0)
#      incoming err is from -20 to 20
      #We want scaled error to be between 7 and 11
# so 0 maps to 4, -320 maps to 9.3 and 320 maps to 5
#    0         8  -20 maps to 9.3  and 20 maps to 13
#there is 64 per each unit mapped with 7 as constant:
     kp= .05 #kp
     kd = 0.15
     errdot = (err-old_err)
     scaled_err = (kp*err+kd*errdot+10.0)
#      binary_global2.shape[0]/10 
#      time.sleep(.01)
#     print("SCALED ERR" + str(scaled_err))
     trunc_T = "{:.3f}".format(T)
     trunc_err = "{:.3f}".format(err)
     trunc_errdot = "{:.3f}".format(errdot)
     trunc_scaled_err = "{:.3f}".format(scaled_err)
     print("ERR: " + str(trunc_err)+ " ERRDOT: " + str(trunc_errdot) + " OUT: " + str(trunc_scaled_err)+" T: "+ str(trunc_T)+"kp: "+ str(kp)+ " kd: " + str(kd) )
     print()
     steering.ChangeDutyCycle(scaled_err)
         
     old_err = err
def auto_control(start):
    # initialize the camera and grab a reference
    # can also vary
    # allow the camera to warmup? try without it
#    time.sleep(0.1)
    # start recording using piCamera API
    
    camera.start_recording(get_video_filename())
    # grab one frame at the time from the stream
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image
      frame = frame.array
      end = time.time()
      T = end - start
      start = time.time()
#     init_arr       =  np.array(frame)      
        # add your magic here
      init_arr = frame
      init_arr = init_arr[::16,::16] #take only bottom 72, and take each 16th column
      gray_image     =  rgb2gray(init_arr)
      global_thresh  =  threshold_otsu(gray_image)
      binary_global  =  gray_image > global_thresh
      histogram      =  np.sum(binary_global[binary_global.shape[0]//2:,:], axis=0)
      standard       =  np.std(histogram, axis=0)
      global_thresh2 =  threshold_otsu(histogram) + standard
      binary_global2 =  histogram > global_thresh2
      binary_global2 =  1-binary_global2  
#       plt.plot(binary_global2)
#       plt.show() 
      camera_center  =  binary_global2.shape[0]/2
#       print(binary_global2.shape[0])
      track_center   =  ndimage.measurements.center_of_mass(binary_global2)
      err = track_center[0] - camera_center
      steer(err,T)

#       print(err)
      # send err to actuators,
      # if positive steer right 
      # if negative steer left
# clear the stream in preparation for the next frame
      rawCapture.truncate(0)      
a = datetime.now()
camera = PiCamera()
camera.resolution = (640, 480) # we can vary this as needed. A rougher image actually helps us
camera.framerate = 90
rawCapture = PiRGBArray(camera, size=(640, 480))
time.sleep(0.01)
InterruptHandler(11)
GPIO.add_event_detect(11, GPIO.FALLING, callback=InterruptHandler, bouncetime=1)
speed = 0
# speedcontroller.ChangeDutyCycle(7)
while True:
     try:   
      auto_control(start)
     except KeyboardInterrupt:
      speedcontroller.stop()
      steering.stop()
      camera.stop_recording()    
      GPIO.cleanup()
      print("Goodbye")
     finally:
      speedcontroller.stop()
      steering.stop()
      camera.stop_recording()   # save the last video file before shutting down
      GPIO.cleanup()
      print("Goodbye")
      
