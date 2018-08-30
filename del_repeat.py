import os
import cv2
import glob
import shutil

img_type = 'single'
basename = 'part3_all'

well_save_dir = 'D:/7-30/' + basename
txt_dir = 'D:/7-30/txt/' + basename
repeat_dir = 'D:/7-30/' + basename + '_' + img_type
if not os.path.exists(repeat_dir):
    os.makedirs(repeat_dir)

imgs = glob.glob(os.path.join(well_save_dir, '*'))
imgs_origin = [imgs[i] for i in range(len(imgs)) if i % 2 == 0]
imgs_transparent = [imgs[i] for i in range(len(imgs)) if i % 2 == 1]
f_b = open(os.path.join(txt_dir, img_type + '_t.txt'), 'r')

with open(os.path.join(txt_dir, img_type + '_o.txt'), 'r') as f:
    lines = f.readlines()
    for line in lines:
        line_b = f_b.readline().strip()
        origin_name = line.strip()
        # print(line)
        # print(line_b)
        # print('\n')
        shutil.copy(os.path.join(well_save_dir, origin_name), os.path.join(repeat_dir, origin_name))
        shutil.copy(os.path.join(well_save_dir, line_b), os.path.join(repeat_dir, line_b))

f_b.close()
