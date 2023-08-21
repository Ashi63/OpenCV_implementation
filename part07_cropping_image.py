import cv2
import numpy as np
from pathlib import Path

# Path to image file
img_path = str(Path('C:\\Users\\Alkashi\\Desktop\\ML_Project\\Open_CV\\images\\image_1.jpg'))

# Reading the orginal color image file. By default of color images 1 is used as parameter.
img = cv2.imread(f'{img_path}')
img = cv2.resize(img,(600,600))

# Display the image.
cv2.imshow('Original Color',img)

# Hold the display.
cv2.waitKey(0)

 