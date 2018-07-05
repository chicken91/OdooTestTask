from task3.model.Color import Color


class TrafficLight:

    def __init__(self):
        self.carColor = Color.RED
        self.footerColor = Color.GREEN
        pass

    def show_info(self):
        print("Car color: " + str(self.carColor) + "footer color: " + str(self.footerColor))
