import pytesseract
import PIL.Image
import cv2
import os

# Default Configuration of the image to text model
myconfig = r'--psm 1 --oem 3'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def image_to_text(fileLocation):
    text = pytesseract.image_to_string(
        PIL.Image.open(fileLocation), config=myconfig)
    print(text)
    return text


# image_path = os.path.join(os.getcwd(), 'Tests', 'file2.png')

# image_to_text(image_path)


def recognized_image_boxes(image_file_name):
    image_path = os.path.join(os.curdir, "..", "ScreenShots", image_file_name)
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    boxes = pytesseract.image_to_boxes(img, config=myconfig)
    for box in boxes:
        box = box.split(" ")
        img = cv2.rectangle(
            img, (int(box[1], height-int(box[2]))), (int(box[3]), height-int(box[4])), (0, 255, 0), 2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    return boxes


def recognized_words_outline_with_text(image_file_name):
    image_path = os.path.join(os.curdir, "..", "ScreenShots", image_file_name)
    img = cv2.imread(image_path)
    height, width, _ = img.shape
    img_data = pytesseract.image_to_data(
        img, config=myconfig, output_type=Output.DICT)
    amount_boxes = len(img_data['text'])
    for i in range(amount_boxes):
        if (float(img_data['conf'][i])) > 80:
            (x, y, width, height) = (
                img_data["left"][i], img_data["right"][i], img_data["width"][i], img_data["height"][i])
            img = cv2.rectangle(
                img, (x, y), (x+width, y+height), (0, 255, 0), 2)
            img = cv2.putText(
                img, img_data['text'], (x, y+height+20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2, cv2.LINE_AA)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    return img_data
