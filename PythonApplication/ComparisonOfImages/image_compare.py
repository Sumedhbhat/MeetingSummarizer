from PIL import Image,ImageChops
import math, operator
import os
from functools import reduce

def rms_diff(im1, im2):
    "Calculate the root-mean-square difference between two images"
    img_loc1=os.path.join(os.getcwd(),"..","Output","Screenshots",im1)
    img_loc2=os.path.join(os.getcwd(),"..","Output","Screenshots",im2)
    image_file1=Image.open(img_loc1)
    image_file2=Image.open(img_loc2)

    h = ImageChops.difference(image_file1, image_file2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))
#(left,upper,right,lower)
box = (14,15,754,424)
cropped_Image = img_1.crop(box)
cropped_Image_2 = img_2.crop(box)
rms_diff(cropped_Image,cropped_Image_2)