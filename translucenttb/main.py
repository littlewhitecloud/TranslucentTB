from re import match
from tkinter import Event, Tk
from tkinter.colorchooser import askcolor
from tkinter.ttk import Button, Combobox, Entry, Frame, Label, Separator

from darkdetect import isDark
from sv_ttk import set_theme

from .blur import blur, byref, c_int, sizeof, windll


class Settings(Tk):
    """Window to choose effect for taskbar"""

    def __init__(self):
        super().__init__()

        self.option_add("*font", ("Cascadia Mono", 9))
        set_theme("dark" if isDark() else "light")
        self.title("TranslucentTb")
        self.geometry("570x120")
        self.resizable(False, False)
        self.iconbitmap("")

        if isDark():
            windll.dwmapi.DwmSetWindowAttribute(
                windll.user32.GetParent(self.winfo_id()),
                20,
                byref(c_int(2)),
                sizeof(c_int(2)),
            )
            self.withdraw()
            self.deiconify()

        selectframe = Frame(self)

        chooseframe = Frame(selectframe)
        choose = Label(
            chooseframe,
            text="Choose a effect you'd like to apply to the taskbar:",
        )
        effectchooser = Combobox(
            chooseframe, value=("clear", "noeffect", "blur", "acrylic")
        )

        colorframe = Frame(selectframe)
        color = Label(
            colorframe, text="Choose or input a hexcolor you'd like to use:"
        )
        colorentry = Entry(colorframe)
        colorbutton = Button(
            colorframe, text="🎨", command=lambda: self.choose(colorentry)
        )

        bottomframe = Frame(self)
        exittcl = Button(bottomframe, text="Exit", command=self.quit)
        applytb = Button(
            bottomframe,
            text="Apply",
            style="Accent.TButton",
            command=lambda: self.apply(effectchooser.get(), colorentry.get()),
        )
        sep = Separator(bottomframe, orient="horizontal")

        bottomframe.pack(side="bottom", fill="x")
        sep.pack(side="top", fill="x")
        for widget in (exittcl, applytb):
            widget.pack(side="right", fill="y", padx=1, pady=1)

        choose.pack(side="left", padx=7)
        effectchooser.pack(side="left")
        chooseframe.grid(row=1, column=0, sticky="nw")

        color.pack(side="left", padx=7)
        colorentry.pack(side="left")
        colorbutton.pack(side="left", padx=3)
        colorframe.grid(row=2, column=0, sticky="nw")

        selectframe.pack(side="top")

        colorentry.bind("<KeyPress>", self.check)

    def apply(self, effect: str, hexColor: str = None):
        """Apply effect to the window"""
        blur(blurtype=effect, hexColor=hexColor)

    def choose(self, entry: Entry):
        """Choose a color for blur"""
        entry.delete(0, "end")
        entry.insert("insert", askcolor()[-1])

    def check(self, event: Event) -> None:
        if match(r"^#(?:[0-9a-fA-F]{3}){1,2}$", event.widget.get()):
            event.widget.state(["invalid"])
        else:
            event.widget.state(["!invalid"])
