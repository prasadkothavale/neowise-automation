import pyautogui
import numpy
# import time
import pyscreenshot


def read_screen():
    # start = time.time()
    img = pyautogui.screenshot()
    # print(time.time() - start)
    frame = numpy.array(img)
    return frame


def read_screen_2():
    # start = time.time()
    img = pyscreenshot.grab(bbox=(0, 0, 1920, 1080))
    # print(time.time() - start)
    frame = numpy.array(img)
    return frame
