from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from package.ui.initial_setup_start_ui import Ui_initialSetupStartWidget
from package.ui.initial_setup_set_password_ui import Ui_initialSetupSetPasswordWidget
from package.ui.initial_setup_control_setting_ui import Ui_initialSetupControlSettingWidget

class InitialSetupUI(QStackedWidget):


    def __init__(self):
        super().__init__()
        self.resize(800, 480)
        self.stack1_start = QWidget()
        self.stack2_set_password = QWidget()
        self.stack3_control_setting = QWidget()

        self.stack1StartUI()
        self.stack2SetPasswordUI()
        self.stack3ControlSettingUI()

        self.addWidget(self.stack1_start)
        self.addWidget(self.stack2_set_password)
        self.addWidget(self.stack3_control_setting)

        self.setCurrentIndex(0)

    def stack1StartUI(self):
        ui = Ui_initialSetupStartWidget()
        ui.setupUi(self.stack1_start)

    def stack2SetPasswordUI(self):
        ui = Ui_initialSetupSetPasswordWidget()
        ui.setupUi(self.stack2_set_password)

    def stack3ControlSettingUI(self):
        ui = Ui_initialSetupControlSettingWidget()
        ui.setupUi(self.stack3_control_setting)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = InitialSetupUI()
    ui.show()
    sys.exit(app.exec_())