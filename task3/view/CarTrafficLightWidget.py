import tkinter
from collections import Counter

from task3.model.Color import Color


class CarTrafficLightWidget(tkinter.Canvas):
    colors = Counter()

    def __init__(self, **kw):
        super().__init__(**kw)
        self.init_colors()
        self.set_color(Color.RED)

    def init_colors(self):
        self.config(width=47, height=127, bg='black')
        self.colors[Color.RED] = self.create_oval(5, 5, 45, 45, fill=Color.RED)
        self.colors[Color.YELLOW] = self.create_oval(5, 45, 45, 85, fill=str(Color.YELLOW))
        self.colors[Color.GREEN] = self.create_oval(5, 85, 45, 125, fill=str(Color.GREEN))

    def set_color(self, color):
        for key in self.colors:
            if key == color:
                self.itemconfigure(self.colors[key], fill=color)
            else:
                self.itemconfigure(self.colors[key], fill='grey')
