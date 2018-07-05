import tkinter
from collections import Counter

from task3.model.Color import Color


class CarTrafficLightWidget(tkinter.Canvas):

    def __init__(self, **kw):
        super().__init__(**kw)
        self.colors = Counter()
        self.init_colors()

    def init_colors(self):
        self.config(width=47, height=127, bg='black')
        self.colors[Color.RED] = self.create_oval(5, 5, 45, 45, fill=Color.RED, tags="carColorRed")
        self.colors[Color.YELLOW] = self.create_oval(5, 45, 45, 85, fill=Color.YELLOW, tags="carColorYellow")
        self.colors[Color.GREEN] = self.create_oval(5, 85, 45, 125, fill=Color.GREEN, tags="carColorGreen")

    def set_color(self, color):
        for key in self.colors:
            if key == color:
                self.itemconfigure(self.colors[key], fill=key)
            else:
                self.itemconfigure(self.colors[key], fill='grey')
