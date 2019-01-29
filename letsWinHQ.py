import numpy as np
from PIL import ImageGrab, Image
import cv2
import time
import pytesseract


def read_question_and_answers():
    img = Image.open(image)
    image_text = pytesseract.image_to_string(img)
    image_text.replace("\n\n", "\n")
    text = image_text.split('\n')
    print(image_text)
    time.sleep(5)


def find_answer(question, a1, a2, a3):
    return


def main():
    img_path = 'output.png'
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

    last_time = time.time()

    question_screen = np.array(ImageGrab.grab(bbox=(30, 320, 472, 460)))
    a1 = np.array(ImageGrab.grab(bbox=(30, 470, 472, 550)))
    a2 = np.array(ImageGrab.grab(bbox=(30, 559, 472, 639)))
    a3 = np.array(ImageGrab.grab(bbox=(30, 648, 472, 728)))
    question_screen[np.where((question_screen <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]
    a1[np.where((a1 <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]
    a2[np.where((a2 <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]
    a3[np.where((a3 <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]

    cv2.imshow('Question', cv2.cvtColor(question_screen, cv2.COLOR_BGR2RGB))
    cv2.imshow('A1', cv2.cvtColor(a1, cv2.COLOR_BGR2RGB))
    cv2.imshow('A2', cv2.cvtColor(a2, cv2.COLOR_BGR2RGB))
    cv2.imshow('A3', cv2.cvtColor(a3, cv2.COLOR_BGR2RGB))
    cv2.imwrite('output.png', question_screen)

    while True:
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
        elif cv2.waitKey(82) & 0xFF == ord('r'):
            read_question_and_answers()


main()
