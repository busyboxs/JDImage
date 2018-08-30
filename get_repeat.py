import os
import cv2
import glob
import shutil

well_save_dir = 'D:/7-30/part3_bad'
well_origin_dir = 'D:/7-30/part3_bad_todo'
if not os.path.exists(well_origin_dir):
    os.makedirs(well_origin_dir)
imgs = glob.glob(os.path.join(well_save_dir, '*'))
imgs_origin = [imgs[i] for i in range(len(imgs)) if i % 2 == 0]
imgs_transparent = [imgs[i] for i in range(len(imgs)) if i % 2 == 1]

for i in range(len(imgs)/2):
    # print(os.path.basename(imgs_origin[i]))
    # print(os.path.basename(imgs_transparent[i]))
    # print('\n')
    index_origin = os.path.basename(imgs_origin[i]).split('_')[0]
    index_transparent = os.path.basename(imgs_transparent[i]).split('_')[0]
    assert index_origin == index_transparent, "different:{}-{}".format(index_origin, index_transparent)

    # copy origin images to a new folder
    print(os.path.basename(imgs_origin[i]))
    shutil.copy(imgs_origin[i], os.path.join(well_origin_dir, os.path.basename(imgs_origin[i])))