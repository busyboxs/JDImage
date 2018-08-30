from wand.image import Image
from wand.display import display
import glob
import os
from PIL import Image as PImage
import PIL.ImageOps

trans_dir = 'data'  # transparent images path
mask_dir = 'mask'  # path to save mask label images
if not os.path.exists(mask_dir):
    os.makedirs(mask_dir)
images = glob.glob(os.path.join(trans_dir, '*'))
# trans_images = [images[i] for i in range(len(images)) if i % 2 == 1]
trans_images = images

for image in trans_images:
    mask = os.path.join(mask_dir, os.path.basename(image))
    with Image(filename=image) as img:
        img.alpha_channel = 'extract'
        img.save(filename=mask)
        # print(img)
        # display(img)
