import os
import numpy as np
import cv2

img_dir = 'D:/work/valid/repeat/true'

img1 = os.path.join(img_dir, '59_1_5b22259eN303f6296.png')
img2 = os.path.join(img_dir, '531_1_5b2225abN6057a517.png')

im1 = cv2.imread(img1)
im2 = cv2.imread(img2)

im1 = np.array(im1)
im2 = np.array(im2)

diff = im1-im2
w, h, c = diff.shape

for i in range(w):
    for j in range(h):
        for k in range(c):
            if diff[i, j, k] != 0:
                print(diff[i, j, k])