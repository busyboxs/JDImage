import os
import glob
import shutil

well_save_dir = 'D:/7-30/txt/part3_bad'
repeat_dir = 'D:/7-30/txt/part3_bad_repeat'
single_dir = 'D:/7-30/txt/part3_bad_single'
imgs = glob.glob(os.path.join(well_save_dir, '*'))
imgs_origin = [imgs[i] for i in range(len(imgs)) if i % 2 == 0]
imgs_transparent = [imgs[i] for i in range(len(imgs)) if i % 2 == 1]
f_b = open('D:/7-2/single_t.txt', 'r')  # single transparent file

with open('D:/7-24/single_o.txt', 'r') as f:  # single origin file
    lines = f.readlines()
    for line in lines:
        line_b = f_b.readline().strip()
        origin_name = line.strip()
        # print(line)
        # print(line_b)
        # print('\n')
        shutil.copy(os.path.join(well_save_dir, origin_name), os.path.join(single_dir, origin_name))
        shutil.copy(os.path.join(well_save_dir, line_b), os.path.join(single_dir, line_b))

f_b.close()