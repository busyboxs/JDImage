# -*- coding: utf-8 -*-
import requests
import os
import shutil
from tqdm import tqdm


def download_image_improved(url, save_path):
    """demo: 下载图片"""
    # 伪造headers信息
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/45.0.2454.101 Safari/537.36"}
    # 限定URL
    # response = requests.get(url, headers=headers, stream=True)
    from contextlib import closing
    # 用完流自动关掉
    with closing(requests.get(url, headers=headers, stream=True)) as response:
        # 打开文件
        with open(save_path, 'wb') as fd:
            # 每128写入一次
            for chunk in response.iter_content(128):
                fd.write(chunk)


# url = 'https://img14.360buyimg.com/n1/jfs/t19003/128/2346418904/328371/fa9e2be5/5aefc297N1661f490.jpg'
# download_image_improved(url, 'data/demo.jpg')


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

        download_image_improved(trans_url, cate_dir + '/' + str(i) + '_1_' + os.path.basename(trans_url))
        download_image_improved(raw_url, cate_dir + '/' + str(i) + '_0_' + os.path.basename(raw_url))