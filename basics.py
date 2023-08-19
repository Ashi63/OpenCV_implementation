import cv2
import numpy as np
from pathsfortut import openCV_tut_dir,campusX_tut_dir,image_files_dir,video_files_dir
import os
from pathlib import Path
img_path = str(Path('C:\\Users\\Alkashi\\Desktop\\ML_Project\\Open_CV\\images\\image_1.jpg'))

img = cv2.imread(f'{img_path}')
gray_img = cv2.imread(f'{img_path}',0)
print("Image as array\n",img)
print("Gray Image as array\n",gray_img)
print("Dimensions of Image: ",img.ndim)
print("Dimensions of Gray Image: ",gray_img.ndim)
print("Shape of Image: ", img.shape)
print("Shape of Gray Image: ",gray_img.shape)



