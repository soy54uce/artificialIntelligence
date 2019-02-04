import numpy as np
from PIL import ImageGrab, Image
import cv2
import pytesseract


def read_question_and_answers():
    question_screen = np.array(ImageGrab.grab(bbox=(100, 275, 530, 460)))
    a1 = np.array(ImageGrab.grab(bbox=(130, 520, 450, 580)))
    a2 = np.array(ImageGrab.grab(bbox=(130, 600, 450, 660)))
    a3 = np.array(ImageGrab.grab(bbox=(130, 680, 450, 740)))
    question_screen[np.where((question_screen <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]
    a1[np.where((a1 <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]
    a2[np.where((a2 <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]
    a3[np.where((a3 <= [220, 220, 220]).all(axis=2))] = [0, 0, 0]

    cv2.imwrite('hqGame/question.png', question_screen)
    cv2.imwrite('hqGame/ans1.png', a1)
    cv2.imwrite('hqGame/ans2.png', a2)
    cv2.imwrite('hqGame/ans3.png', a3)

    quest_img = Image.open('hqGame/question.png')
    ans1_img = Image.open('hqGame/ans1.png')
    ans2_img = Image.open('hqGame/ans2.png')
    ans3_img = Image.open('hqGame/ans3.png')
    question = pytesseract.image_to_string(quest_img)
    ans_1 = pytesseract.image_to_string(ans1_img)
    ans_2 = pytesseract.image_to_string(ans2_img)
    ans_3 = pytesseract.image_to_string(ans3_img)
    answer = find_answer(question, ans_1, ans_2, ans_3)
    print(question, '\n', ans_1, '\n', ans_2, '\n', ans_3)
    print(answer)


def find_answer(question, a1, a2, a3):
    ans = 42

    return ans


def main():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
    loop_var = 'go'
    while loop_var != 'stop':
        loop_var = input("Ready?")
        read_question_and_answers()


main()
