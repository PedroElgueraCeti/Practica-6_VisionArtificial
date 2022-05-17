from matplotlib import pyplot as plt
from matplotlib import pylab 
import cv2
import imutils
import numpy as np


img1 = cv2.imread('challenger.jpg', 1)
img1hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
low_red = np.array([161, 155, 84])
high_red = np.array([179, 255, 255])
red_mask = cv2.inRange(img1hsv, low_red, high_red)
red = cv2.bitwise_and(img1hsv,img1hsv, mask=red_mask)
low_blue = np.array([94, 80, 2])
high_blue = np.array([126, 255, 255])
blue_mask = cv2.inRange(img1hsv, low_blue, high_blue)
blue = cv2.bitwise_and(img1hsv, img1hsv, mask=blue_mask)
low_green = np.array([25, 52, 72])
high_green = np.array([102, 255, 255])
green_mask = cv2.inRange(img1hsv, low_green, high_green)
green = cv2.bitwise_and(img1hsv, img1hsv, mask=green_mask)

img1hsv = cv2.resize(img1hsv,(400,300))
cv2.imshow('img1hsv',img1hsv)
red = cv2.resize(red,(400,300))
cv2.imshow('red',red)
green = cv2.resize(green,(400,300))
cv2.imshow('green',green)
blue = cv2.resize(blue,(400,300))
cv2.imshow('blue',blue)
cv2.waitKey(0)