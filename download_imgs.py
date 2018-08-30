# -*- coding:utf-8 -*-
import urllib
import os
import glob
from tqdm import tqdm
import shutil

exp = 'https://img14.360buyimg.com/n1/'
save_dir = 'images'

if not os.path.exists(save_dir):
    os.makedirs(save_dir)
else:
    shutil.rmtree(save_dir)
    os.makedirs(save_dir)


with open('data/info.txt', 'r') as f:
    lines = f.readlines()
    for i, line in tqdm(enumerate(lines)):
        line = line.strip()
        trans, raw, cd = line.split(' ')[1:4]
        cate = line.split(' ')[4].replace('/', '_').decode("utf-8")
        cate_dir = os.path.join(save_dir, cd + '-' + cate)
        if not os.path.exists(cate_dir):
            os.makedirs(cate_dir)
        trans_url = exp + trans
        raw_url = exp + raw
        try:
            urllib.urlretrieve(trans_url, cate_dir + '/' + str(i) + '_1_' + os.path.basename(trans_url))
            urllib.urlretrieve(raw_url, cate_dir + '/' + str(i) + '_0_' + os.path.basename(raw_url))
        except:
            print(i)


