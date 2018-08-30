import os
import cv2
import glob
import shutil

well_save_dir = 'D:/7-30/part3_all'
txt_dir = 'D:/7-30/txt/part3_all'
if not os.path.exists(txt_dir):
    os.makedirs(txt_dir)
imgs = glob.glob(os.path.join(well_save_dir, '*'))
imgs_origin = [imgs[i] for i in range(len(imgs)) if i % 2 == 0]
imgs_transparent = [imgs[i] for i in range(len(imgs)) if i % 2 == 1]
name_list = []
f_b = open(os.path.join(txt_dir, 'repeat_t.txt'), 'w')  # file to save the name of repeat transparent images
f_c = open(os.path.join(txt_dir, 'single_o.txt'), 'w')  # file to save the name of single origin images
f_d = open(os.path.join(txt_dir, 'single_t.txt'), 'w')  # file to save the name of single transparent images
f_e = open(os.path.join(txt_dir, 'a.txt'), 'w')

with open(os.path.join(txt_dir, 'repeat_o.txt'), 'w') as f:

    for i in range(len(imgs)/2):
        # print(os.path.basename(imgs_origin[i]))
        # print(os.path.basename(imgs_transparent[i]))
        # print('\n')
        index_origin = os.path.basename(imgs_origin[i]).split('_')[0]
        index_transparent = os.path.basename(imgs_transparent[i]).split('_')[0]
        assert index_origin == index_transparent, "different:{}-{}".format(index_origin, index_transparent)

        name_origin = os.path.basename(imgs_origin[i]).split('_')[2].split('.')[0]
        if name_origin not in name_list:
            name_list.append(name_origin)
            for j in range(len(imgs)/2):
                if i == j:
                    f_c.write('{}\n'.format(os.path.basename(imgs_origin[j])))
                    f_e.write('{}\n'.format(name_origin))
                    f_d.write('{}\n'.format(os.path.basename(imgs_transparent[j])))
                    continue
                name_origin_j = os.path.basename(imgs_origin[j]).split('_')[2].split('.')[0]
                if name_origin == name_origin_j:
                    f.write('{}\n'.format(os.path.basename(imgs_origin[j])))
                    f_b.write('{}\n'.format(os.path.basename(imgs_transparent[j])))
            # f.write('\n')
f_b.close()