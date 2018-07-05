from task3.model.TrafficLight import TrafficLight


class TrafficLightController:
    nightMode = False
    traffic_lights = list()
    timer = None

    def __init__(self):
        self.traffic_lights.append(TrafficLight())
        self.traffic_lights.append(TrafficLight())
        self.traffic_lights.append(TrafficLight())

    def add_traffic_light(self):
        self.traffic_lights.append(TrafficLight())

    def remove_traffic_light(self, index):
        del self.traffic_lights[index]

    def show_info(self):
        for traffic_light in self.traffic_lights:
            traffic_light.show_info()
