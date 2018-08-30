import os
import glob
import shutil

root_dir = 'D:/7-31/'

origin_dir = os.path.join(root_dir, 'origin')
trans_dir = os.path.join(root_dir, 'transparent')

origin_txt = os.path.join(root_dir, 'origin.txt')
trans_txt = os.path.join(root_dir, 'transparent.txt')

origin_images = os.listdir(origin_dir)
trans_images = os.listdir(trans_dir)

trans_images_new = [trans_image.replace('_0_', '_1_') for trans_image in trans_images]
trans_images_new = [trans_image[:-21] + trans_image[-21:-4][::-1] + trans_image[-4:] for trans_image in trans_images_new]
print(trans_images_new)

print(origin_images)
print(trans_images)

assert len(origin_images) == len(trans_images), 'Length of list are different!'

for i in range(len(origin_images)):
    index_o = origin_images[i].split('_')[0]
    index_t = trans_images[i].split('_')[0]
    if index_t != index_o:
        print(index_o)
    assert index_o == index_t, 'Index are not same!'


with open(origin_txt, 'w') as f:
    for img in origin_images:
        base_name = img.split('.')[0]
        f.write('{}\n'.format(base_name))

with open(trans_txt, 'w') as f:
    for img in trans_images:
        base_name = img.split('.')[0]
        f.write('{}\n'.format(base_name))

old_txt = os.path.join(root_dir, 'old.txt')
new_txt = os.path.join(root_dir, 'new.txt')

f_old = open(old_txt, 'w')
f_new = open(new_txt, 'w')
for i in range(len(trans_images)):
    old_name = os.path.join(trans_dir, trans_images[i])
    new_name = os.path.join(trans_dir, trans_images_new[i])
    f_old.write('{}\n'.format(old_name))
    f_new.write('{}\n'.format(new_name))
    os.rename(old_name, new_name)

f_old.close()
f_new.close()

