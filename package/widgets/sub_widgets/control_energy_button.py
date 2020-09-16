from PyQt5.QtWidgets import *
from package.ui.energy_control_button_ui import Ui_controlButtonBox


class ControlEnergyButton(QWidget):
    def __init__(self):
        super().__init__()
        self.state = False
        self.ui = Ui_controlButtonBox()
        self.setup_ui()
        self.set_signals()
        self.toggle_state()

    def setup_ui(self):
        self.ui.setupUi(self)


    def set_signals(self):
        self.ui.button_push.clicked.connect(self.toggle_state)

    def set_text(self, text):
        self.ui.button_text_label.setText(text)

    def toggle_state(self):
        if self.state:
            self.ui.button_push.setText("ON")
            self.ui.button_push.setStyleSheet("border:none;\n"
                                           "background-color: rgb(48, 216, 136);\n"
                                           "color: white;\n"
                                           "border-top-right-radius: 15%;\n"
                                           "border-bottom-right-radius: 15%;")
            self.state = False
        else:
            self.ui.button_push.setText("OFF")
            self.ui.button_push.setStyleSheet("border:none;\n"
                                           "background-color: rgb(242, 160, 160);\n"
                                           "color: white;\n"
                                           "border-top-right-radius: 15%;\n"
                                           "border-bottom-right-radius: 15%;")
            self.state = True
