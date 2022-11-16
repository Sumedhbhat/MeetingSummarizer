import pytesseract
import PIL.Image
import cv2

myconfig = r'--psm 1 --oem 3'


def image_to_text():
    text = pytesseract.image_to_string(
        PIL.Image.open('text.jpg'), config=myconfig)
    print(text)
    return text


def recognized_boxes_image():
    img = cv2.imread('someFile.jpg')
    height, width, _ = img.shape
    boxes = pytesseract.image_to_boxes(img, config=myconfig)
    for box in boxes:
        box = box.split(" ")
        img = cv2.rectangle(
            img, (int(box[1], height-int(box[2]))), (int(box[3]), height-int(box[4])), (0, 255, 0), 2)
    cv2.imshow("img", img)
    cv2.waitKey(0)
    return boxes


def recognized_words_outline_with_text():
    img = cv2.imread('someFile.jpg')
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
