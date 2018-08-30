# -*- coding:utf-8 -*-
import os
import glob
import shutil
from tqdm import tqdm
import logging

logging.basicConfig(filename='log/logger.log', level=logging.INFO)


def valid_index(list_origin, list_trans):
    assert len(list_origin) == len(list_trans), 'Length is not same. Please check the input.'
    for i in range(len(list_origin)):
        index_o = get_index_from_name(list_origin[i])
        index_t = get_index_from_name(list_trans[i])
        if index_t != index_o:
            print(index_o, index_t)
        assert index_o == index_t, 'Index are not same.'


def get_index_from_name(name):
    return name.split('_')[0]


def get_name_list(img_dir):
    return os.listdir(img_dir)


def mkdir(dir):
    if not os.path.exists(dir):
        os.makedirs(dir)


def split_trans_raw(image_dir):
    parent_dir = image_dir + '/..'
    raw_dir = os.path.join(parent_dir, 'origin')
    trans_dir = os.path.join(parent_dir, 'transparent')
    mkdir(raw_dir)
    mkdir(trans_dir)
    img_list = get_name_list(image_dir)
    raw_imgs = img_list[::2]
    trans_imgs = img_list[1::2]
    for i in tqdm(range(len(raw_imgs))):
        shutil.copy(os.path.join(image_dir, raw_imgs[i]), os.path.join(raw_dir, raw_imgs[i]))
        shutil.copy(os.path.join(image_dir, trans_imgs[i]), os.path.join(trans_dir, trans_imgs[i]))


def get_sub_dir_list_zh(root_dir):
    sub_dir = []
    for _, dirs, _ in os.walk(root_dir):
        sub_dir.extend(dirs)
        break
    sub_dir = [sub.decode('gbk').encode('utf-8') for sub in sub_dir]
    return sub_dir


def get_sub_file_list_zh(root_dir):
    sub_files = []
    for _, _, files in os.walk(root_dir):
        sub_files.extend(files)
        break
    sub_files = [sub.decode('gbk').encode('utf-8') for sub in sub_files]
    return sub_files


def get_sub_file_list(root_dir):
    sub_files = []
    for _, _, files in os.walk(root_dir):
        sub_files.extend(files)
        break
    # sub_files = [sub.decode('gbk').encode('utf-8') for sub in sub_files]
    return sub_files


def test_get_sub_dir_list():
    ll = get_sub_dir_list_zh('origin')
    print(ll)
    print(ll[1].decode('utf-8'))


def make_dir_for_train_all():
    for i in tqdm(range(1, 21)):
        img_dir = 'D:/8-7/train_all/part/part' + str(i)
        sub_dirs = get_sub_dir_list_zh(img_dir)
        # print(sub_dirs)
        for sub_dir in sub_dirs:
            bad_dir = os.path.join(img_dir, sub_dir.decode('utf-8'), 'bad')
            well_dir = os.path.join(img_dir, sub_dir.decode('utf-8'), 'well')
            white_dir = os.path.join(img_dir, sub_dir.decode('utf-8'), 'white')
            repeat_dir = os.path.join(img_dir, sub_dir.decode('utf-8'), 'repeat')
            mkdir(bad_dir)
            mkdir(well_dir)
            mkdir(white_dir)
            mkdir(repeat_dir)

def move_repeat():
    for i in tqdm(range(1, 21)):
        img_dir = 'D:/8-7/train_all/part/part' + str(i)
        sub_dirs = get_sub_dir_list_zh(img_dir)
        for sub_dir in sub_dirs:
            path = os.path.join(img_dir, sub_dir)
            ll = get_sub_file_list_zh(path.decode('utf-8'))
            raw_names = ll[::2]
            trans_names = ll[1::2]
            base_name_list = []
            for i in range(len(raw_names)):
                base_name = raw_names[i][-21:-4]
                if base_name not in base_name_list:
                    base_name_list.append(base_name)
                else:
                    old_path = os.path.join(path, raw_names[i]).decode('utf-8')
                    new_path = os.path.join(path, 'repeat', raw_names[i]).decode('utf-8')
                    shutil.move(old_path, new_path)
                    old_path = os.path.join(path, trans_names[i]).decode('utf-8')
                    new_path = os.path.join(path, 'repeat', trans_names[i]).decode('utf-8')
                    shutil.move(old_path, new_path)


def move_repeat_out():
    for i in tqdm(range(1, 21)):
        img_dir = 'D:/8-7/train_all/part/part' + str(i)
        sub_dirs = get_sub_dir_list_zh(img_dir)
        for sub_dir in sub_dirs:
            path = os.path.join(img_dir, sub_dir)
            repeat = os.path.join(path, 'repeat')
            # print(get_sub_file_list(repeat.decode('utf-8')))
            for f in get_sub_file_list_zh(repeat.decode('utf-8')):
                old_path = os.path.join(repeat, f).decode('utf-8')
                new_path = os.path.join(path, f).decode('utf-8')
                # print(old_path)
                # print(new_path)
                shutil.move(old_path, new_path)

def move_subdir_to_root():
    img_dir = 'D:/PycharmProjects/Jdimage/images'
    save_dir = 'D:/8-7/train_all/images'
    sub_dirs = get_sub_dir_list_zh(img_dir)
    for sub_dir in sub_dirs:
        path = os.path.join(img_dir, sub_dir)
        # print(get_sub_file_list(repeat.decode('utf-8')))
        for f in tqdm(get_sub_file_list_zh(path.decode('utf-8'))):
            old_path = os.path.join(path, f).decode('utf-8')
            new_path = os.path.join(save_dir, f)
            logging.info('{}'.format(new_path))
            # print(old_path)
            # print(new_path)
            shutil.copy(old_path, new_path)

def lll():
    root_dir = 'D:/8-13/'
    img_all_dir = root_dir + 'touming/'
    txt = root_dir + 'touming_s_sku_list.txt'
    with open(txt, 'r') as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]
        file_names = os.listdir(img_all_dir)
        for name in tqdm(file_names):
            sku = name.split('.')[0]
            if sku in lines:
                old_path = img_all_dir + name
                new_path = root_dir + 'img_std_more_cid3_res_08_08/' + name.replace('.', '_1_.')
                shutil.copy(old_path, new_path)

def find_repeat_and_move():
    img_dir = 'D:/PycharmProjects/Jdimage/images'
    sub_dirs = get_sub_dir_list_zh(img_dir)
    for sub_dir in sub_dirs:
        path = os.path.join(img_dir, sub_dir)
        repeat = os.path.join(path, 'repeat')
        if not os.path.exists(repeat.decode('utf-8')):
            os.makedirs(repeat.decode('utf-8'))
        imgs = get_sub_file_list_zh(path.decode('utf-8'))
        raw_names = [img for img in imgs if img.split('_')[1] == '0']  # get all raw image names
        trans_names = [img for img in imgs if img.split('_')[1] == '1']  # get all transparent image names
        assert len(raw_names) == len(trans_names), "Length not equal"
        base_name_list = []
        for i in range(len(raw_names)):
            base_name = raw_names[i][-21:-4]
            if base_name not in base_name_list:
                base_name_list.append(base_name)
            else:
                old_path = os.path.join(path, raw_names[i]).decode('utf-8')
                new_path = os.path.join(path, 'repeat', raw_names[i]).decode('utf-8')
                shutil.move(old_path, new_path)
                old_path = os.path.join(path, trans_names[i]).decode('utf-8')
                new_path = os.path.join(path, 'repeat', trans_names[i]).decode('utf-8')
                shutil.move(old_path, new_path)


if __name__ == '__main__':
    # split_trans_raw('D:/8-7/fcn_raw_data_08_07')
    with open('D:/8-13/all_part11_cid3_nums.txt', 'r') as f:
        lines = f.readlines()
        cd_less = []
        cd_num = {}
        for line in lines:
            cd = line.strip().split()[0]
            num = line.strip().split()[2]
            # print(cd, num)
            
            cd_less.append(cd)
            cd_num[cd] = num
        print(len(cd_less))
    img_dir = 'D:/PycharmProjects/Jdimage/images'
    sub_dirs = get_sub_dir_list_zh(img_dir)
    for sub_dir in tqdm(sub_dirs):
        path = os.path.join(img_dir, sub_dir)
        cd_i = sub_dir.split('-')[0]
        if cd_i in cd_less:
            new_path = os.path.join('D:/8-13/color_near/add2/{}'.format(cd_num[cd_i]), sub_dir)
            shutil.copytree(path.decode('utf-8'), new_path.decode('utf-8'))









