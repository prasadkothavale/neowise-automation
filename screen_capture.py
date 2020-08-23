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
    img = pyscreenshot.grab()
    # print(time.time() - start)
    frame = numpy.array(img)
    return frame
