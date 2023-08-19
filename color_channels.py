import os
import cv2
import numpy as np
from pathlib import Path

# Path to image file
img_path = str(Path('C:\\Users\\Alkashi\\Desktop\\ML_Project\\Open_CV\\images\\image_1.jpg'))

# Reading the orginal color image file. By default of color images 1 is used as parameter.
img = cv2.imread(f'{img_path}')
img = cv2.resize(img,(400,600))

#cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# here we are making  Blue channel as zero
#img[:,:,0] = 0
# here we are making  Green channel as zero
#img[:,:,1] = 0
# here we are making  Red channel as zero
#img[:,:,2] = 0

imgBlue  = img[:,:,0]
imgGreen = img[:,:,1]
imgRed   = img[:,:,2]

new_img = np.hstack((imgBlue,imgGreen,imgRed))

'''
# We read image as np array
print("Color Image as array\n",img)
print("Type of Image as read by CV2: ",type(img))
print("Dimensions of Image: ",img.ndim)
print("Shape of Image: ", img.shape)
'''
# We read image as np array
print("Color Image as array\n",new_img)
print("Type of Image as read by CV2: ",type(new_img))
print("Dimensions of Image: ",new_img.ndim)
print("Shape of Image: ", new_img.shape)

# Showing the gray scale image.
cv2.imshow('Original Image', img)
cv2.imshow('Stacked Image',new_img)

# to hold the image for display 0 means delay is infinite.
cv2.waitKey(0)