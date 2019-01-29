import numpy as np
from PIL import ImageGrab, Image
import cv2
import time
import pytesseract


def read_question(image):
    img = Image.open(image)
    image_text = pytesseract.image_to_string(img)
    print(image_text)


def main():
    img_path = 'output.png'
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    last_time = time.time()
    while True:
        question_screen = np.array(ImageGrab.grab(bbox=(65, 172, 290, 400)))
        # question_screen = cv2.cvtColor(question_screen, cv2.COLOR_BGR2GRAY)
        mask = (question_screen == [230, 230, 230]).all(axis=2)
        question_screen[mask] = [255, 255, 255]
        new_mask = (question_screen >= [160, 160, 160]).all(axis=2)
        question_screen[new_mask] = [0, 0, 0]

        cv2.imshow('HQ', cv2.cvtColor(question_screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite('output.png', question_screen)

        print('loop took {} seconds'.format(time.time() - last_time))
        last_time = time.time()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(82) & 0xFF == ord('r'):
            read_question(img_path)


main()