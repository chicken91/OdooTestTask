import json

from task3.model.Color import Color


class TrafficLight:

    def __init__(self):
        self.carColor = Color.RED
        self.footerColor = Color.GREEN

    def show_info(self, index):
        print(str(index + 1) + ". TrafficLight car color: " + self.carColor + ", footer color: " + self.footerColor)

    def to_json(self):
        return str(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)).replace("\n", "").replace(
            " ", "")
