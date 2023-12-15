import cv2
from PIL import Image
import time

try:
    camera1 = cv2.VideoCapture(0)
    camera2 = cv2.VideoCapture(1)
    camera3 = cv2.VideoCapture(2)
    camera4 = cv2.VideoCapture(3)
    w = camera3.get(cv2.CAP_PROP_FRAME_WIDTH)
    h = camera3.get(cv2.CAP_PROP_FRAME_HEIGHT)
    camera3.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    camera3.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    while True:
        taken1, output1 = camera1.read()
        taken2, output2 = camera2.read()
        taken3, output3 = camera3.read()
        taken4, output4 = camera4.read()
        if taken1:
            cv2.imwrite("test1.png", output1)
        if taken2:
            cv2.imwrite("test2.png", output2)
        if taken3 == True:
            cv2.imwrite("test3.png", output3)
        if taken4:
            cv2.imwrite("test4.png", output4)
        time.sleep(3)
except Exception as e:
    print(e)