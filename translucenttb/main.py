from ctypes import windll
from tkinter import Tk

from blur import blur


class Settings(Tk):
    def __init__(self):
        super().__init__()  # TODO: add gui later

        self.hwnd = windll.user32.FindWindowW("Shell_TrayWnd", None)
        blur(self.hwnd, "acrylic")


Settings()
