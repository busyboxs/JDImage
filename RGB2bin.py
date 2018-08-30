from wand.image import Image
from wand.display import display
import glob
import os
from PIL import Image as PImage
import PIL.ImageOps


def gray2binary(img, threshold):
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    binary = img.point(table, '1')
    return binary


mask_dir = 'mask'
mask = os.path.join(mask_dir, 'n.png')
im = PImage.open(mask)
# im = im.convert('L', dither=None)
im = PIL.ImageOps.invert(im)
print(im)
im = gray2binary(im, 254)
# im.show()
im.save('binary/n.png')

print(im)
