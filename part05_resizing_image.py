import os
import cv2
import numpy as np
from pathlib import Path

# Path to image file.
img_path = str(Path('C:\\Users\\Alkashi\\Desktop\\ML_Project\\Open_CV\\images\\image_1.jpg'))

# Reading the orginal color image file. By default of color images 1 is used as parameter.
img = cv2.imread(f'{img_path}')

# Resizing the image
#resized_img = cv2.resize(img,(420,700))
resized_img = cv2.resize(img,(img.shape[1]//2,img.shape[0]//2))

# Showing the gray scale image.
cv2.imshow('Original Image', img)
cv2.imshow('Resized Image', resized_img)

# to hold the image for display 0 means delay is infinite.
cv2.waitKey(0)