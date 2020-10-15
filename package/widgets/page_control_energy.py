# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.ui.page_control_energy_ui import Ui_pageControlEnergy
from package.widgets.sub_widgets.control_energy_button import ControlEnergyButton
from package.server import Server
from package.device_setting import DeviceSetting
from package.service.api import Apis


class PageControlEnergy(QWidget):
    def __init__(self, device_setting: DeviceSetting, server: Server, apis: Apis):
        super().__init__()
        self.server = server
        self.device_setting = device_setting
        self.apis = apis

        self.switch_count = len(self.device_setting.switch_devices)
        self.plug_count = len(self.device_setting.plug_devices)
        self.switch_buttons = []
        self.plug_buttons = []
        self.ui = Ui_pageControlEnergy()
        self.setup_ui()

    def setup_ui(self):
        self.ui.setupUi(self)
        self.add_control_buttons()

    def add_control_buttons(self):
        switch_unit_count = 0
        plug_unit_count = 0
        for n in range(self.switch_count):
            temp_device = self.device_setting.switch_devices[n]
            for n_unit in range(len(temp_device.units)):
                self.switch_buttons.append(
                    ControlEnergyButton(temp_device.id, temp_device.d_type, n_unit, self.apis, self.server, init_state=temp_device.units[n_unit]))
                self.switch_buttons[switch_unit_count].set_text("스위치" + str(switch_unit_count + 1))
                self.ui.gridLayout.addWidget(self.switch_buttons[switch_unit_count], switch_unit_count, 0)
                switch_unit_count += 1

        for n in range(self.plug_count):
            temp_device = self.device_setting.plug_devices[n]
            for n_unit in range(len(temp_device.units)):
                self.plug_buttons.append(
                    ControlEnergyButton(temp_device.id, temp_device.d_type, n_unit, self.apis, self.server, init_state=temp_device.units[n_unit]))
                self.plug_buttons[plug_unit_count].set_text("플러그" + str(plug_unit_count + 1))
                self.ui.gridLayout.addWidget(self.plug_buttons[plug_unit_count], plug_unit_count, 1)
                plug_unit_count += 1

    def initial(self):
        switch_unit_count = 0
        plug_unit_count = 0
        for switch_device in self.device_setting.switch_devices:
            switch_device.load()
            for n_unit in range(len(switch_device.units)):
                self.switch_buttons[switch_unit_count].set_state(switch_device.units[n_unit])
                switch_unit_count += 1
        for plug_device in self.device_setting.plug_devices:
            plug_device.load()
            for n_unit in range(len(plug_device.units)):
                self.plug_buttons[plug_unit_count].set_state(plug_device.units[n_unit])
                plug_unit_count += 1



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)

    server = Server()
    device_setting = DeviceSetting()
    apis = Apis(server, device_setting)

    pageControlEnergy = PageControlEnergy(device_setting, server, apis)
    pageControlEnergy.show()
    sys.exit(app.exec_())
