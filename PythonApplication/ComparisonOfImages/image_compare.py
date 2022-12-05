from PIL import Image,ImageChops
import math, operator
import os
from functools import reduce

def rms_diff(im1, im2):
    "Calculate the root-mean-square difference between two images"
    # img_loc1=os.path.join(os.getcwd(),"..","Output","Screenshots",im1)
    # img_loc2=os.path.join(os.getcwd(),"..","Output","Screenshots",im2)
    # print(img_loc2)
    # image_file1=Image.open(img_loc1)
    # image_file2=Image.open(img_loc2)
    try:
        image_file1=Image.open(im1)
        image_file2=Image.open(im2)
        box = (14,15,754,424)
        cropped_Image_1 = image_file1.crop(box)
        cropped_Image_2 = image_file2.crop(box)
        h = ImageChops.difference(image_file1, image_file2).histogram()

        # calculate rms
        rms=math.sqrt(reduce(operator.add,
            map(lambda h, i: h*(i**2), h, range(256))
        ) / (float(image_file1.size[0]) * image_file2.size[1]))
        return rms
    except FileNotFoundError:
        print('Provided image path is not found')
        return 0
    except:
        return 0

# print(rms_diff('screenshot3.png','screenshot2.png'))