# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.ui.energy_control_button_ui import Ui_controlButtonBox
from package.service.api import Apis
from package.server import Server
from package.utils import request_failed
from package.utils import get_project_root
from package.device_setting import Device


class ControlEnergyButton(QWidget):
    def __init__(self, device_id, device_type, unit_index, apis: Apis, server: Server, init_state=False):
        super().__init__()
        self.apis = apis
        self.server = server
        self.device_id = device_id
        self.device_type = device_type
        self.unit_index = unit_index

        self.state = init_state
        self.ui = Ui_controlButtonBox()
        self.setup_ui()
        self.set_signals()

    def setup_ui(self):
        self.ui.setupUi(self)
        self.set_style()

    def set_signals(self):
        self.ui.button_push.clicked.connect(self.toggle_state)

    def set_text(self, text):
        self.ui.button_text_label.setText(text)

    def set_state(self, state):
        self.state = state
        self.set_style()

    def set_style(self):
        if self.state:
            self.ui.button_push.setText("ON")
            self.ui.button_push.setStyleSheet("border:none;\n"
                                              "background-color: rgb(48, 216, 136);\n"
                                              "color: white;\n"
                                              "border-top-right-radius: 15%;\n"
                                              "border-bottom-right-radius: 15%;")
        else:
            self.ui.button_push.setText("OFF")
            self.ui.button_push.setStyleSheet("border:none;\n"
                                              "background-color: rgb(242, 160, 160);\n"
                                              "color: white;\n"
                                              "border-top-right-radius: 15%;\n"
                                              "border-bottom-right-radius: 15%;")
        self.ui.button_push.repaint()

    def toggle_state(self):
        self.state = not self.state
        res = self.apis.device.control(self.device_id, self.device_type, self.state, self.unit_index,
                                       self.server.token.access)
        print(res)
        if res[0] is False:
            self.state = not self.state
            request_failed('DEVICE.CONTROL')
            self.ui.button_push.setText('ERR')
            self.ui.button_push.setStyleSheet("border:none;\n"
                                              "background-color: rgb(255, 110, 112);\n"
                                              "color: white;\n"
                                              "border-top-right-radius: 15%;\n"
                                              "border-bottom-right-radius: 15%;")
            return

        self.set_style()


if __name__ == "__main__":
    import sys
    from package.device_setting import DeviceSetting

    app = QApplication(sys.argv)

    server = Server()
    device_setting = DeviceSetting()
    apis = Apis(server, device_setting)

    button = ControlEnergyButton('device_id', 'device_type', 0, apis, server)
    button.show()
    sys.exit(app.exec_())
