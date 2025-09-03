# Homework 1, CV
# Shenyao Jin, shenyaojin@mines.edu
#%% Import libs
import numpy as np
import matplotlib.pyplot as plt
from skimage.io import imread
#%% Define data path
data_path = "./data/IMG_5167.jpeg"

#%% Load image
image = imread(data_path)
rotated_image = np.rot90(image, k=3) # Need to rotate the image
#%% Show image
plt.figure()
plt.imshow(rotated_image)
plt.axis("off")
plt.show()

#%% Change the dtype to float32 and convert into grayscale
image_float = rotated_image.astype(np.float32)
image_gray = np.dot(image_float, [0.299, 0.587, 0.114])

#%% Show grayscale image
plt.figure()
plt.imshow(image_gray, cmap='gray')
plt.axis("off")
plt.show()

#%% Print the top left (3*5) pixels of the grayscale image
print(image_gray[:3,:5])

#%% Print index=(1,2) of image_gray. We assume the index start from 1.
print(image_gray[0,1])