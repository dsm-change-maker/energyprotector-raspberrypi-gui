from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from package.ui.initial_setup_ui import Ui_initialSetupWidget
from package.device_setting import DeviceSetting

class InitialSetupUI(QStackedWidget):
    def __init__(self, device_setting):
        super().__init__()
        self.page = 0
        self.device_setting = device_setting

        self.init_device_setting()
        self.setup_ui()
        self.set_signals()
        self.setCurrentIndex(self.page)

    def init_device_setting(self):
        print("INIT")
        self.device_setting.new_id()

    def setup_ui(self):
        ui = Ui_initialSetupWidget()
        ui.setupUi(self)
        self.ui = ui
        self.set_device_id()

    def set_signals(self):
        # page_start
        self.ui.startButton.clicked.connect(self.next_page)
        # page_set_password
        self.ui.settingButton.clicked.connect(self.next_page)
        # page_control_setting
        self.ui.settingFinishButton.clicked.connect(self.next_page)

    def set_device_id(self):
        self.ui.idEditReadOnly.setText("디바이스 아이디 : " + self.device_setting.id)

    def next_page(self):
        self.page += 1
        if self.page > 2:
            self.page = 0
        self.setCurrentIndex(self.page)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    device_setting = DeviceSetting()
    initialSetupWidget = InitialSetupUI(device_setting)
    print(device_setting.id)
    initialSetupWidget.show()
    sys.exit(app.exec_())
