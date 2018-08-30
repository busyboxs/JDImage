import os
import shutil
import tqdm
from util import *


def write_list():
    with open('name_list.txt', 'w') as f:
        for i in range(1, 21):
            dir_name = "part{}_good".format(i)
            names = os.listdir(dir_name)
            names = ['{}\n'.format(name) for name in names]
            f.writelines(names)


def mkdir_need(path):
    if not os.path.exists(path):
        os.makedirs(path)


def move_good():
    with open('data/name_list.txt', 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
    for i in range(1, 45):
        img_dir = 'D:/8-13/color_near/add2/{}'.format(i)
        sub_dirs = get_sub_dir_list_zh(img_dir)
        for sub_dir in tqdm(sub_dirs):
            path = os.path.join(img_dir, sub_dir)
            good_dir = os.path.join(path, 'good')
            mkdir_need(good_dir.decode('utf-8'))
            not_need = os.path.join(path, 'not_need')
            mkdir_need(not_need.decode('utf-8'))

            imgs = get_sub_file_list_zh(path.decode('utf-8'))
            for img in imgs:
                if img in lines:
                    old_path = os.path.join(path, img).decode('utf-8')
                    new_path = os.path.join(good_dir, img).decode('utf-8')
                    shutil.move(old_path, new_path)


if __name__ == "__main__":

    png_dir = 'D:/8-13/color_near/png'
    img_dir = 'D:/8-7/train_all/images'
    images = os.listdir(img_dir)
    raw = [image for image in images if image.split('_')[1] == '0']
    trans = [image for image in images if image.split('_')[1] == '1']
    print(len(trans))
    print(len(raw))

    names = os.listdir(png_dir)
    indecs = [name.split('_')[0] for name in names]
    print(indecs)

    trans_list = []
    for img in trans:
        if img.split('_')[0] in indecs:
            trans_list.append(img)

    print(trans_list)
    print(names)
    print(len(names))

    for i in range(len(trans_list)):
        old_name = os.path.join(png_dir, names[i])
        new_name = os.path.join(png_dir, trans_list[i])
        os.rename(old_name, new_name)

