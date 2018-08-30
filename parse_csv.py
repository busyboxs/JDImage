# -*- coding:utf-8 -*-
import pandas as pd
import os
from util import *

data = pd.read_csv('data/data.csv',  sep='\x01', names=['sku', 'url', 'img_path', 'item_third_cate_cd',
                                                        'item_third_cate_name', 'rand_num', 'rn'])
# data.to_csv('data/data_new.csv', sep=',', encoding='utf-8')

cat = []
category = []
cd = []
cd_cat = []
url_1 = []
url_2 = []
need_cate = ['银手镯', '饰品', '珍珠项链', '珍珠吊坠', '珍珠耳饰', '珍珠手链', '珍珠戒指', '珍珠胸针',
             'K金吊坠', 'K金项链', '黄金转运珠', 'K金手镯/手链/脚链', 'K金戒指', 'K金耳饰', '银耳饰',
             '琥珀/蜜蜡', '碧玺', '红宝石/蓝宝石', '祖母绿', '黄金项链', '黄金吊坠', '黄金手镯/手链/脚链',
             '黄金戒指', '黄金耳饰', '银吊坠/项链', '银手链/脚链', '银戒指', '宝宝银饰', '裸钻', '钻戒',
             '钻石项链/吊坠', '钻石耳饰', '钻石手镯/手链', '项链/吊坠', '手镯/手串', '戒指', '耳饰', '玉石孤品',
             '手镯/手链/脚链', '手镯/手链', '头饰/胸针', '摆件/挂件', '项链', '手链/脚链', '花卉', '苗木',
             '绿植盆栽', '多肉植物', '植物类']
# cd_txt = 'C:/Users/yangshun/Desktop/cd.txt'
# cd_need = [line.strip() for line in open(cd_txt, 'r').readlines()]
# print(cd_need)

# need_cate = [line.strip() for line in open('book.txt', 'r').readlines()]

rest = []

s = data.iloc[:, :7]
cat_list = s.values
print('category list length: ' + str(len(cat_list)))
for i in range(len(cat_list)):
    # print(cat_list[i])
    cat.append(cat_list[i])  # 所有的信息

    # if cat_list[i][4] not in need_cate:
    #     rest.append(cat_list[i])  # 除去指定类别后，剩余类别

    # if cat_list[i][4] in need_cate:  # 获取指定类别的url和img_path
    #     if cat_list[i][1] not in url_1:
    #         url_1.append(cat_list[i][1])
    #         url_2.append(cat_list[i][2])

    if cat_list[i][3] not in cd_cat:
        # category.append(cat_list[i][4])
        category.append(str(cat_list[i][3]) + '-' + cat_list[i][4])
        cd_cat.append(cat_list[i][3])
        if cat_list[i][4] in need_cate:
            cd.append((str(cat_list[i][3]) + '-' + cat_list[i][4]).replace('/', '_'))
        # if str(cat_list[i][3]) in cd_need:
        #     cd.append((str(cat_list[i][3]) + '-' + cat_list[i][4]).replace('/', '_'))

print('url1 length: {}'.format(len(url_1)))
print('url2 length: {}'.format(len(url_2)))

print(len(category))
print(len(rest))


# with open('data/category.txt', 'w') as f:
#     for i in range(len(category)):
#         f.write('{}\n'.format(category[i]))
#
# with open('data/info.txt', 'w') as f:
#     for i in range(len(cat)):
#         f.write('{} {} {} {} {} {}\n'.format(cat[i][0], cat[i][1], cat[i][2],
#                                              cat[i][3], cat[i][4], cat[i][5]))
#
# with open('data/cd.txt', 'w') as f:
#     for i in range(len(cd)):
#         f.write('{}\n'.format(cd[i]))
#
# with open('data/url.txt', 'w') as f:
#     for i in range(len(url_1)):
#         f.write('{} {}\n'.format(url_1[i], url_2[i]))

image_dir = 'D:/8-7/train_all/images'
save_dir = 'D:/8-7/train_all/done'
if not os.path.exists(save_dir):
    os.makedirs(save_dir)
all_dir_list = get_sub_dir_list(image_dir)
print(len(all_dir_list))
print(all_dir_list[0])

for l in all_dir_list:
    if l in cd:
        shutil.move(os.path.join(image_dir, l.decode('utf-8')), os.path.join(save_dir, l.decode('utf-8')))
