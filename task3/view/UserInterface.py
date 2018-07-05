import tkinter
from functools import partial

from task3.model.TrafficLightType import TrafficLightType
from task3.view.CarTrafficLightWidget import CarTrafficLightWidget
from task3.view.FooterTrafficLightWidget import FooterTrafficLightWidget


class UserInterface:

    def __init__(self, traffic_light_controller):
        self.traffic_light_widgets = {TrafficLightType.CAR: [], TrafficLightType.FOOTER: []}
        self.currentRow = 1
        self.traffic_light_controller = traffic_light_controller
        self.traffic_light_controller.set_timer_callback(self.update_traffic_lights_state)
        self.ui = tkinter.Tk()
        add_button = tkinter.Button(text='Add', name='add_control_widget')
        add_button.grid(row=self.currentRow, column=1, columnspan=1, rowspan=1)
        add_button.bind("<Button-1>", self.on_add_click)
        add_button = tkinter.Button(text='Info', name='info_control_widget')
        add_button.grid(row=self.currentRow, column=2, columnspan=1, rowspan=1)
        add_button = tkinter.Button(text='Send', name='send_control_widget')
        add_button.grid(row=self.currentRow, column=3, columnspan=1, rowspan=1)
        self.currentRow += 1

        self.update_ui()

        self.ui.mainloop()
        pass

    def on_add_click(self, event):
        self.traffic_light_controller.add_traffic_light()
        self.update_ui()

    def on_info_click(self, event):
        pass

    def on_send_click(self, event):
        pass

    def on_remove_click(self, index, event):
        self.traffic_light_controller.remove_traffic_light(index)
        self.update_ui()

    def update_ui(self):
        for child in self.ui.winfo_children():
            if child.winfo_name().find('control_widget') == -1:
                child.destroy()
        self.currentRow = 2

        self.traffic_light_widgets[TrafficLightType.CAR].clear()
        self.traffic_light_widgets[TrafficLightType.FOOTER].clear()

        for traffic_light in self.traffic_light_controller.traffic_lights:
            self.create_traffic_light()
        self.update_traffic_lights_state()

    def update_traffic_lights_state(self):
        for index, traffic_light_data in enumerate(self.traffic_light_controller.traffic_lights):
            self.traffic_light_widgets[TrafficLightType.CAR][index].set_color(traffic_light_data.carColor)
            self.traffic_light_widgets[TrafficLightType.FOOTER][index].set_color(traffic_light_data.footerColor)

    def create_traffic_light(self):
        auto_traffic_light = CarTrafficLightWidget()
        auto_traffic_light.grid(row=self.currentRow, column=1, columnspan=1, rowspan=1)
        self.traffic_light_widgets[TrafficLightType.CAR].append(auto_traffic_light)

        footer_traffic_light = FooterTrafficLightWidget()
        footer_traffic_light.grid(row=self.currentRow, column=2, columnspan=1, rowspan=1)
        self.traffic_light_widgets[TrafficLightType.FOOTER].append(footer_traffic_light)

        traffic_light_index = len(self.traffic_light_widgets[TrafficLightType.FOOTER]) - 1
        add_button = tkinter.Button(text='Remove', state="normal", name='btn_' + str(traffic_light_index))
        add_button.grid(row=self.currentRow, column=3, columnspan=1, rowspan=1)
        add_button.bind("<Button-1>", partial(self.on_remove_click, traffic_light_index))

        self.currentRow += 1
        pass
