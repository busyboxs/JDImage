# -*- coding:utf-8 -*-
# Author : zhaijianwei
# Date : 2018/5/22 10:24

import urllib


def download_img(img_path_file, saved_path):
    file = open(img_path_file, "r")
    url_lines = file.readlines()
    skus = [url_line.strip().split('\t')[0] for url_line in url_lines]
    raw_imgs_prefix = [url_line.strip().split('\t')[1] for url_line in url_lines]
    trans_imgs_prefix = [url_line.strip().split('\t')[2] for url_line in url_lines]
    raw_img_urls = ["https://img14.360buyimg.com/n1/" + prefix.strip() for prefix in raw_imgs_prefix]
    trans_img_urls = ["https://img14.360buyimg.com/n1/" + prefix.strip() for prefix in trans_imgs_prefix]
    for i in range(len(raw_imgs_prefix)):
        try:
            urllib.urlretrieve(raw_img_urls[i], saved_path + str(i) + "_0_" + raw_img_urls[i].split("/")[-1])
            urllib.urlretrieve(trans_img_urls[i], saved_path + str(i) + "_1_" + trans_img_urls[i].split("/")[-1])
        except:
            print(skus[i] + " download failed!!!")
        if i % 1000 == 0:
            print(str(i) + " image pairs have been downloaded!")

    file.close()

download_img("fcn_img_path_08_06_add", "fcn_raw_data_08_06/")


