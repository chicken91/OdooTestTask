import threading

from task3.model.TrafficLight import TrafficLight


class TrafficLightController:

    def __init__(self):
        self.nightMode = False
        self.traffic_lights = list()
        self.timer = None
        self.timer_callback = None
        self.traffic_lights.append(TrafficLight())
        self.init_timer()

    def set_timer_callback(self, timer_callback):
        self.timer_callback = timer_callback

    def add_traffic_light(self):
        self.traffic_lights.append(TrafficLight())

    def remove_traffic_light(self, index):
        del self.traffic_lights[index]

    def init_timer(self):
        self.timer = threading.Timer(3, self.change_traffic_lights_state)
        self.timer.setDaemon(True)
        self.timer.start()

    def change_traffic_lights_state(self):
        for traffic_light in self.traffic_lights:
            car_color = traffic_light.carColor
            traffic_light.carColor = traffic_light.footerColor
            traffic_light.footerColor = car_color

        if self.timer_callback is not None:
            self.timer_callback()

        self.init_timer()

    def show_info(self):
        for index, traffic_light in enumerate(self.traffic_lights):
            traffic_light.show_info(index)

    def send_info(self):
        json_file = "{nightMode: " + str(self.nightMode) + ", trafficLights: ["
        for traffic_light in self.traffic_lights:
            json_file += traffic_light.to_json() + ","
        json_file = json_file[:-1]

        json_file += "]}"
        print(json_file)
