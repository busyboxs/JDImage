# find images repeat ignore

import os
import glob
import shutil

images_dir = 'D:/7-24/fcn_train_06_13'
bad_dir = 'D:/7-24/bad'
imgs = glob.glob(os.path.join(images_dir, '*'))
imgs_origin = [imgs[i] for i in range(len(imgs)) if i % 2 == 0]
imgs_transparent = [imgs[i] for i in range(len(imgs)) if i % 2 == 1]
f_b = open('D:/7-24/b.txt', 'w')

with open('D:/7-24/a.txt', 'r') as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    print(len(lines))

for img in imgs_origin:
    name_origin = os.path.basename(img).split('_')[2].split('.')[0]
    if name_origin in lines:
        f_b.write('{}\n'.format(os.path.basename(img)))
        shutil.move(img, os.path.join(bad_dir, os.path.basename(img)))

