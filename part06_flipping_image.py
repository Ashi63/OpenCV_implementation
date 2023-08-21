import cv2
import numpy as np
import os
from pathlib import Path

# Path to image file
img_path = str(Path('C:\\Users\\Alkashi\\Desktop\\ML_Project\\Open_CV\\images\\image_1.jpg'))

# Reading the orginal color image file. By default of color images 1 is used as parameter.
img = cv2.imread(f'{img_path}')
img = cv2.resize(img,(800,600))
img_flip_vertial = cv2.flip(img,0)
img_flip_horizontal = cv2.flip(img,1)
img_flip_horizontal_vertical = cv2.flip(img,-1)
#img_flip_ = cv2.flip(img,0)
#img_flip_vertial = cv2.flip(img,0)
cv2.imshow('Original Image',img)
cv2.imshow('Flipped Image',img_flip_vertial)
cv2.imshow('Horizontal Image',img_flip_horizontal)
cv2.imshow('Vertical + Horizontal Image',img_flip_horizontal_vertical)

cv2.waitKey(0)

