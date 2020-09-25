# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.device_setting import DeviceSetting
from package.initial_setup import InitialSetupUI
from package.main_energyprotector import MainEnergyProtectorUI
from package.error_load_setting import ErrorLoadSettingUi
from package.server import Server


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.server = Server()
        self.device_setting = DeviceSetting()
        self.initial_setup_ui = InitialSetupUI(self.device_setting, self.server)
        self.main_energy_protector_ui = MainEnergyProtectorUI(self.device_setting, self.server)
        self.error_load_setting_ui = ErrorLoadSettingUi()
        self.setup_ui()
        self.set_signals()

        temp_device_setting = DeviceSetting()
        if not temp_device_setting.load_conf():
            self.show_initial_setting()
        else:
            self.show_main_energy_protector()

    def setup_ui(self):
        self.resize(800, 480)
        self.setStyleSheet("background-color:white")
        lay = QVBoxLayout()
        lay.addWidget(self.initial_setup_ui)
        lay.addWidget(self.main_energy_protector_ui)
        widget = QWidget()
        widget.setLayout(lay)
        self.setCentralWidget(widget)

    def set_signals(self):
        self.initial_setup_ui.ui.initial_setting_finish_button.clicked.connect(self.show_main_energy_protector)
        self.main_energy_protector_ui.ui.pagesWidget.widget(3).go_initial.connect(self.show_initial_setting)
        self.error_load_setting_ui.go_initial.connect(self.show_initial_setting)

    def show_initial_setting(self):
        self.initial_setup_ui.init()
        self.main_energy_protector_ui.hide()
        self.error_load_setting_ui.hide()
        self.initial_setup_ui.show()

    def show_main_energy_protector(self):
        self.main_energy_protector_ui.init()
        self.initial_setup_ui.hide()
        self.error_load_setting_ui.hide()
        self.main_energy_protector_ui.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
