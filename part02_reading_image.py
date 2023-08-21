import cv2
import numpy as np
import os
from pathlib import Path

# Path to image file
img_path = str(Path('C:\\Users\\Alkashi\\Desktop\\ML_Project\\Open_CV\\images\\image_1.jpg'))

# Reading the orginal color image file. By default of color images 1 is used as parameter.
img = cv2.imread(f'{img_path}')

# Reading the original image in gray scale format. We give 0 as parameter.
gray_img = cv2.imread(f'{img_path}',0)

# We read image as np array
print("Color Image as array\n",img)
print("Gray Image as array\n",gray_img)
print("Type of Image as read by CV2: ",type(img))
print("Type of Image as read by CV2: ",type(gray_img))
print("Dimensions of Image: ",img.ndim)
print("Dimensions of Gray Image: ",gray_img.ndim)
print("Shape of Image: ", img.shape)
print("Shape of Gray Image: ",gray_img.shape)

# Showing image
cv2.imshow("Original Image ",img)
cv2.imshow("Gray Image ",gray_img)

# to hold the image for display 0 means delay is infinite.
cv2.waitKey(0)
