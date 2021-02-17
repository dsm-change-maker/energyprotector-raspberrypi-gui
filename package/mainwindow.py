# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.initial_setup import InitialSetupUI
from package.main_energyprotector import MainEnergyProtectorUI
from package.error_load_setting import ErrorLoadSettingUi
from package.device_setting import DeviceSetting
from package.server import Server
from package.server import get_token
from package.service.api import Apis
from package.database import DataBase
from package.utils import get_project_root
from package.utils import request_failed
from package.widgets.page_usage_time import usagelog_update


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.server = Server()
        self.device_setting = DeviceSetting()
        self.apis = Apis(self.server, self.device_setting)

        self.initial_setup_ui = InitialSetupUI(self.device_setting, self.server, self.apis)
        self.main_energy_protector_ui = MainEnergyProtectorUI(self.device_setting, self.server, self.apis)
        self.error_load_setting_ui = ErrorLoadSettingUi()

        self.setup_ui()
        self.set_signals()

        res = self.device_setting.register(self.server)
        if res is not None:
            if get_token(self.server, self.apis) is None:
                request_failed('GET_TOKEN')
        else:
            request_failed('DEVICE_SETTING.REGISTER')

        if not self.device_setting.load_conf():
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
        self.store_usage_time()
        self.main_energy_protector_ui.init()
        self.initial_setup_ui.hide()
        self.error_load_setting_ui.hide()
        self.main_energy_protector_ui.show()

    def store_usage_time(self):
        res = self.apis.usage.get(day=True, day_n=5)
        if res[0]:
            usagelog_update(res[2]['day'])


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
