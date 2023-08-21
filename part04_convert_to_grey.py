import cv2
import numpy as np
import os
from pathlib import Path

# Path to image file
img_path = str(Path('C:\\Users\\Alkashi\\Desktop\\ML_Project\\Open_CV\\images\\image_1.jpg'))

# Reading the orginal color image file. By default of color images 1 is used as parameter.
img = cv2.imread(f'{img_path}')

# Converting original color image to Gray scale image.
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# We read image as np array
print("Color Image as array\n",img_gray)
print("Type of Image as read by CV2: ",type(img_gray))
print("Dimensions of Image: ",img_gray.ndim)
print("Shape of Image: ", img_gray.shape)

# Showing the gray scale image.
cv2.imshow('Gray Image',img_gray)

# to hold the image for display 0 means delay is infinite.
cv2.waitKey(0)