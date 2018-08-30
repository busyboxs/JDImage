import os
import cv2
import glob
import shutil

img_dir = 'D:/work/fcn_data_07_13'
bad_save_dir = 'D:/work/valid/bad_bycode'
well_save_dir = 'D:/work/valid/well_bycode'
imgs_path = glob.glob(os.path.join(img_dir, '*'))
imgs_path = sorted(imgs_path)
length = len(imgs_path) / 2

for i in range(length):
    img_origin = imgs_path[i*2]
    img_transparent = imgs_path[i*2+1]
    print(os.path.basename(img_origin))
    im_origin = cv2.imread(img_origin)
    im_transparent = cv2.imread(img_transparent)
    cv2.imshow('origin', im_origin)
    cv2.imshow('transparent', im_transparent)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('b'):
        shutil.move(img_origin, os.path.join(bad_save_dir, os.path.basename(img_origin)))
        shutil.move(img_transparent, os.path.join(bad_save_dir, os.path.basename(img_transparent)))
    elif key == ord('w'):
        shutil.move(img_origin, os.path.join(well_save_dir, os.path.basename(img_origin)))
        shutil.move(img_transparent, os.path.join(well_save_dir, os.path.basename(img_transparent)))
    elif key == ord('q'):
        break
    else:
        continue

cv2.destroyAllWindows()
