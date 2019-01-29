import numpy as np
from PIL import ImageGrab, ImageFilter, ImageEnhance
import cv2
import time
import pytesseract


def screen_record():
    last_time = time.time()
    while(True):
        time.sleep(0.1)
        # 800x600 windowed mode
        question_screen =  np.array(ImageGrab.grab(bbox=(65,172,290,400)))

        print('loop took {} seconds'.format(time.time()-last_time))
        last_time = time.time()
        cv2.imshow('HQ',cv2.cvtColor(question_screen, cv2.COLOR_BGR2RGB))
        # read_question(question_screen)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(82) & 0xFF == ord('r'):
            read_question(question_screen)


def read_question(image):
    original_image = image
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = img.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(2)
    img = img.convert(1)
    cv2.imshow('HQGRay', cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    image_text = pytesseract.image_to_string(img)
    print(image_text)


def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    screen_record()

main()