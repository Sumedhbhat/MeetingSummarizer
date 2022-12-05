from PIL import Image,ImageChops
import math, operator
from functools import reduce
imgPath1 = 'D:\images/2.jpeg'
img_1 = Image.open(imgPath1)
imgPath2 = 'D:\images/15.jpeg'
img_2 = Image.open(imgPath2)

def rms_diff(im1, im2):
    "Calculate the root-mean-square difference between two images"

    h = ImageChops.difference(im1, im2).histogram()

    # calculate rms
    return math.sqrt(reduce(operator.add,
        map(lambda h, i: h*(i**2), h, range(256))
    ) / (float(im1.size[0]) * im1.size[1]))
#(left,upper,right,lower)
try:
    box = (14,15,754,424)
    cropped_Image = img_1.crop(box)
    cropped_Image_2 = img_2.crop(box)
    rms_diff(cropped_Image,cropped_Image_2)
except FileNotFoundError:
    print('Provided image path is not found')