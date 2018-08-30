import os

imgs_dir = 'D:/7-31/train_add'

imgs = os.listdir(imgs_dir)
print(len(imgs))

jpgs = [imgs[i] for i in range(len(imgs)) if i % 2 == 0]
pngs = [imgs[i] for i in range(len(imgs)) if i % 2 == 1]
pngs = [png.replace('_0_', '_1_') for png in pngs]
pngs = [png[:-21] + png[-21:-4][::-1] + png[-4:] for png in pngs]
print(len(jpgs))
print(len(pngs))
print(jpgs)
print(pngs)

for i in range(len(jpgs)):
    old_name = os.path.join(imgs_dir, jpgs[i].replace('jpg', 'png'))
    new_name = os.path.join(imgs_dir, pngs[i])
    os.rename(old_name, new_name)

# for i in range(len(jpgs)):
#     old_jpg = os.path.join(imgs_dir, jpgs[i])
#     old_png = os.path.join(imgs_dir, jpgs[i].replace('jpg', 'png'))
#     new_jpg = str(i + 3000) + '_0_' + jpgs[i]
#     new_png = str(i + 3000) + '_1_' + pngs[i]
#     new_jpg = os.path.join(imgs_dir, new_jpg)
#     new_png = os.path.join(imgs_dir, new_png)
#     # os.rename(old_jpg, new_jpg)
#     # os.rename(old_png, new_png)

