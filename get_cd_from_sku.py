import os
import pandas as pd
import glob
import shutil
from tqdm import tqdm

with open('data/test.txt', 'r') as f:
    lines = f.readlines()
    sku_cd_pair = {}
    for line in lines:
        line = line.strip()
        sku, _, _, cd = line.split('\t')[0:4]
        sku_cd_pair[sku] = cd

    print(len(sku_cd_pair))

bad_dir = 'D:/8-21/bad'
paths = glob.glob(os.path.join(bad_dir, '*.jpg'))
print(len(paths))

txt_file = 'data/txt/bad.txt'

cd_list = []
cd_count_pair = {}

with open('D:/8-13/all_part11_cid3_nums.txt', 'r') as f:
    lines = f.readlines()
    cd_by_count = [line.strip().split()[0] for line in lines]
    for line in lines:
        cd, name, count = line.strip().split()
        cd_count_pair[cd] = (name, count)
    print(cd_count_pair)

imgs_dir = 'D:/8-13/color_near/add2'
save_dir = 'D:/8-21/add'

for path in tqdm(paths):
    path = os.path.basename(path)
    sku = path.split('.')[0]
    if sku_cd_pair[sku] not in cd_list and sku_cd_pair[sku] in cd_by_count:
        cd_list.append(sku_cd_pair[sku])
        src_path = os.path.join(imgs_dir, cd_count_pair[sku_cd_pair[sku]][1],
                                sku_cd_pair[sku] + '-' + cd_count_pair[sku_cd_pair[sku]][0].replace('/', '_'))
        dst_path = os.path.join(save_dir,
                                sku_cd_pair[sku] + '-' + cd_count_pair[sku_cd_pair[sku]][0].replace('/', '_'))
        shutil.copytree(src_path.decode('utf-8'), dst_path.decode('utf-8'))
        # print(src_path)
        # print(dst_path)

print(len(cd_list))

with open(txt_file, 'w') as f:
    for cd in cd_list:
        f.write('{}\n'.format(cd))

