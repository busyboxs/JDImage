import os
import glob
import shutil

root_dir = 'D:/7-30/change_name'

origin_dir = os.path.join(root_dir, 'origin')
origin_imgs = os.listdir(origin_dir)
print(origin_imgs)
print(len(origin_imgs))
with open(os.path.join(root_dir, 'origin.txt'), 'w') as f:
    for name in origin_imgs:
        f.write('{}\n'.format(name))

transparent_dir = os.path.join(root_dir, 'transparent')
transparent_imgs = glob.glob(os.path.join(transparent_dir, '*'))
print(transparent_imgs)

pair_dir = os.path.join(root_dir, 'pairs')
pair_imgs = glob.glob(os.path.join(pair_dir, '*'))
print(len(pair_imgs))

pair_origins = [pair_imgs[i] for i in range(len(pair_imgs)) if i % 2 == 0]
pair_transparent = [pair_imgs[i] for i in range(len(pair_imgs)) if i % 2 == 1]
print(len(pair_origins))

name_txt = os.path.join(root_dir, 'name.txt')
transparent_txt = os.path.join(root_dir, 'transparent.txt')
f_name = open(name_txt, 'w')
f_transparent = open(transparent_txt, 'w')
k = 0
for i in range(len(pair_origins)):
    base_name = os.path.basename(pair_origins[i])
    if base_name in origin_imgs:
        f_name.write('{}\n'.format(base_name))
        f_transparent.write('{}\n'.format(os.path.basename(pair_transparent[i])))
        index_o = base_name.split('_')[0]
        index_t = os.path.basename(pair_transparent[i]).split('_')[0]
        assert index_o == index_t, 'index not same!!'
        print(transparent_imgs[k])
        print(os.path.join(transparent_dir, os.path.basename(pair_transparent[i])))
        os.rename(transparent_imgs[k], os.path.join(transparent_dir, os.path.basename(pair_transparent[i])))
        k += 1

f_name.close()
f_transparent.close()
