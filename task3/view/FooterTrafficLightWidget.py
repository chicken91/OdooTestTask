from task3.model.Color import Color
from task3.view.CarTrafficLightWidget import CarTrafficLightWidget


class FooterTrafficLightWidget(CarTrafficLightWidget):
    def init_colors(self):
        self.config(width=47, height=87, bg='black')
        self.colors[Color.RED] = self.create_oval(5, 5, 45, 45, fill=Color.RED)
        self.colors[Color.GREEN] = self.create_oval(5, 45, 45, 85, fill=Color.GREEN)
