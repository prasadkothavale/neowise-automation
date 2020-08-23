import tkinter
# import time
# import math

import PIL.Image
import PIL.ImageTk
from test_runner_scratch import process_image


REFRESH_WAIT = 100  # milli seconds
INITIAL_WAIT = 100  # milli seconds
SCREEN_HEIGHT = 1080
SCREEN_WIDTH = 1920


class Debugger:
    def __init__(self, read_screen):
        self.read_screen = read_screen

        self.window = tkinter.Tk()
        self.window.title("neowise debugger")
        self.canvas = tkinter.Canvas(self.window, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        self.canvas.pack()
        screen = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(read_screen()))
        # self.last_screen_read_time = time.time()
        self.canvas.create_image(0, 0, image=screen, anchor=tkinter.NW)

        self.window.after(INITIAL_WAIT, self.refresh)
        print(f"Initialized debugger with input: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")
        self.window.mainloop()

    def refresh(self):
        self.canvas.delete("all")
        screenshot = self.read_screen()
        self.canvas.img = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(screenshot))
        # screen_read_time = time.time()
        # fps = math.floor(1/(screen_read_time - self.last_screen_read_time))
        # print(fps)
        self.canvas.create_image(0, 0, image=self.canvas.img, anchor=tkinter.NW)
        process_image(screenshot)
        self.window.after(REFRESH_WAIT, self.refresh)
