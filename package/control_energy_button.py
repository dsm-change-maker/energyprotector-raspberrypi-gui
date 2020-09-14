from PyQt5.QtWidgets import *
from package.ui.energy_control_button_ui import Ui_controlButtonBox

class ControlEnergyButton(QWidget):
    def __init__(self):
        super().__init__()
        self.state = False
        self.ui = Ui_controlButtonBox()
        self.setup_ui()

    def setup_ui(self):
        control_button_box = QWidget()
        self.ui.setupUi(control_button_box)
        layout = QBoxLayout(QBoxLayout.TopToBottom)
        layout.addWidget(control_button_box)
        layout.setSizeConstraint(QBoxLayout.SetFixedSize)
        self.setLayout(layout)


    def set_text(self, text):
        self.ui.button_text_label.setText(text)

    def toggle_state(self):
        if not self.state:
            self.ui.button_push.setText("ON")
            self.button_push.setStyleSheet("border:none;\n"
                                           "background-color: rgb(242, 160, 160);\n"
                                           "color: white;\n"
                                           "border-top-right-radius: 15%;\n"
                                           "border-bottom-right-radius: 15%;")
        else:
            self.ui.button_push.setText("OFF")
            self.button_push.setStyleSheet("border:none;\n"
                                           "background-color: rgb(48, 216, 136);\n"
                                           "color: white;\n"
                                           "border-top-right-radius: 15%;\n"
                                           "border-bottom-right-radius: 15%;")
        self.state = not self.state

