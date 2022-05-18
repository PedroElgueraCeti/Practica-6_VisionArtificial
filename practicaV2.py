from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils
import numpy as np

#img1 = cv2.VideoCapture(7)

img1 = cv2.imread('911.jpg', 1)
img1hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
red_mask = cv2.inRange(img1hsv, low_red, high_red)
red = cv2.bitwise_and(img1hsv,img1hsv, mask=red_mask)
low_blue = np.array([94, 80, 100])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(img1hsv, low_blue, high_blue)
blue = cv2.bitwise_and(img1hsv, img1hsv, mask=blue_mask)
low_green = np.array([40, 52, 72])
high_green = np.array([110, 255, 255])
green_mask = cv2.inRange(img1hsv, low_green, high_green)
green = cv2.bitwise_and(img1hsv, img1hsv, mask=green_mask)

#while(1):
    #_, frame = img1.read()
img1hsv = cv2.resize(img1,(400,300))
cv2.imshow('img1hsv',img1hsv)
red = cv2.resize(red,(400,300))
cv2.imshow('red',cv2.cvtColor(red,cv2.COLOR_HSV2BGR))
green = cv2.resize(green,(400,300))
cv2.imshow('green',cv2.cvtColor(green,cv2.COLOR_HSV2BGR))
blue = cv2.resize(blue,(400,300))
cv2.imshow('blue',cv2.cvtColor(blue,cv2.COLOR_HSV2BGR))
cv2.waitKey(0)

#img1.release()