from task3.model.Color import Color


class TrafficLight:
    carColor = Color.RED
    footerColor = Color.RED

    def __init__(self):
        pass

    def show_info(self):
        print("Car color: " + str(self.carColor) + "footer color: " + str(self.footerColor))
