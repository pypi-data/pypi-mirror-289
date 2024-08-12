import tkinter as tk
import typing
import platform

from .graphics import *
from .widgets import *

WidgetType = tuple[int, int]


class Window(tk.Tk):

    def __init__(self, position: tuple[int | float, int | float], size: tuple[int | float, int | float],
                 title: str = "Window", background: str | None = None, *, titlebar: bool = True, transparent: bool = False,
                 top: bool = False, fullscreen: bool = False, alpha: int | float = 1) -> None:
        super().__init__()

        self.x = position[0]
        self.y = position[1]

        self.width = size[0]
        self.height = size[1]

        self.wm_geometry(f"{self.width}x{self.height}+{self.x}+{self.y}")

        self.configs = {
            "titlebar": titlebar,
            "transparent": transparent,
            "title": title,
            "background": background,
            "state": None,
            "top": top,
            "fullscreen": fullscreen,
            "alpha": alpha,
            "transparentcolor": None,
        }

        self.wm_title(self.configs["title"])

        if titlebar is not True:
            self.wm_overrideredirect(titlebar)
        if transparent:
            if platform.system() == 'Darwin':
                self.wm_attributes("-transparent", transparent)
            else:
                raise ValueError("Your host OS is not supported transparent.")

        self.mainloop()

    def place(self, state: typing.Literal['center', 'top', 'left', 'bottom', 'right']) -> str:
        match state:
            case 'center':
                self.x = int(self.winfo_screenwidth()/2-self.width/2)
                self.y = int(self.winfo_screenheight()/2-self.height/2)
                self.wm_geometry(
                    f"{self.width}x{self.height}+{self.x}+{self.y}")
            case 'top':
                self.x = int(self.winfo_screenwidth()/2-self.width/2)
                self.y = 0
                self.wm_geometry(
                    f"{self.width}x{self.height}+{self.x}+{self.y}")
            case 'left':
                self.x = 0
                self.y = int(self.winfo_screenheight()/2-self.height/2)
                self.wm_geometry(
                    f"{self.width}x{self.height}+{self.x}+{self.y}")
            case 'bottom':
                self.x = int(self.winfo_screenwidth()/2-self.width/2)
                self.y = int(self.winfo_screenheight()-self.height)
                self.wm_geometry(
                    f"{self.width}x{self.height}+{self.x}+{self.y}")
            case 'right':
                self.x = int(self.winfo_screenwidth()-self.width)
                self.y = int(self.winfo_screenheight()/2-self.height/2)
                self.wm_geometry(
                    f"{self.width}x{self.height}+{self.x}+{self.y}")
            case _:
                raise ValueError(f'Invalid state: {state}')
        self.configs["state"] = state
        return state

    def titlebar(self, newBool: bool | None = None) -> bool:
        if newBool:
            self.wm_overrideredirect(newBool)
            self.configs["titlebar"] = newBool
            return True
        else:
            return self.configs["titlebar"]

    def size(self, newSize: tuple[int, int] | None = None) -> str | tuple[int, int]:
        if newSize:
            self.wm_geometry(f"{newSize[0]}x{newSize[1]}")
            self.width = newSize[0]
            self.height = newSize[1]
            return self.place(self.configs["state"])
        else:
            return [self.width, self.height]

    def position(self, newPosition: tuple[int, int] | None = None) -> bool | tuple[int, int]:
        if newPosition:
            self.wm_geometry(
                f"{self.width}x{self.height}+{newPosition[0]}+{newPosition[1]}")
            self.x = newPosition[0]
            self.y = newPosition[1]
            return True
        return [self.x, self.y]

    def alpha(self, value: int | float | None = None) -> bool | int | float:
        if value:
            self.wm_attributes("-alpha", value)
            return True
        return self.configs["alpha"]

    def title(self, newTitle: str | None = None) -> bool | typing.Any:
        if newTitle:
            self.wm_title(newTitle)
            self.configs["title"] = newTitle
            return True
        return self.configs["title"]

    def transparent(self, state: bool | None = None) -> bool:
        if state:
            if platform.system() == 'Darwin':
                self.wm_attributes("-transparent", state)
                self.configs["transparent"] = state
            else:
                raise ValueError("Your host OS is not supported transparent.")
            return True
        return self.configs["transparent"]

    def transparentcolor(self, color: str) -> bool:
        if color:
            if platform.system() == 'Windows':
                self.wm_attributes("-transparentcolor", color)
                self.configs["transparentcolor"] = color
            else:
                raise ValueError(
                    "Your host OS is not supported transparentcolor.")
            return True
        return self.configs["transparentcolor"]


class Frame(tk.Canvas):

    def __init__(self, master: Window, position: tuple[int, int], size: tuple[int, int], background: str) -> None:
        super().__init__(master)

        self.place(x=position[0], y=position[1], width=size[0], height=size[1])
        self.configure(bg=background)

        self.contents: list[Rectangle | PerfectCircle | Ellipse | RoundedRectangle | Text] = []

    def rectangle(self, position: tuple[int, int], size: tuple[int, int], backgruond: str) -> int:
        """Create a rectangle on Frame"""
        this = Rectangle(self, position, size, backgruond)
        self.contents.append(this)

        return self.contents.index(this)
    
    def circle(self, position: tuple[int, int], radius: int | float, background: str) -> int:
        """Create a circle on Frame"""
        this = PerfectCircle(self, position, radius, background)
        self.contents.append(this)

        return self.contents.index(this)
    
    def ellipse(self, position: tuple[int, int], radius: tuple[int | float, int | float, int | float, int | float],
                background: str) -> int:
        """Create a ellipse on Frame"""
        this = Ellipse(self, position, radius, background)
        self.contents.append(this)

        return self.contents.index(this)
    
    def rounded_rectangle(self, position: tuple[int, int], size: tuple[int, int],
                          radius: int | float, backgruond: str) -> int:
        """Create a rounded-rectangle on Frame"""
        this = RoundedRectangle(self, position, size, radius, backgruond)
        self.contents.append(this)

        return self.contents.index(this)
    
    def text(self, position: tuple[int, int], text: str, foreground: str) -> int:
        """Create a text on Frame"""
        this = Text(self, position, text, foreground)
        self.contents.append(this)

        return self.contents.index(this)
