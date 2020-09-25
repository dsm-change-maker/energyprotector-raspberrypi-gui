from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal
from package.ui.error_load_setting_ui import Ui_errorLoadSetting


class ErrorLoadSettingUi(QWidget):
    go_initial = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_errorLoadSetting()
        self.setup_ui()

    def setup_ui(self):
        self.ui.setupUi(self)

    def set_signals(self):
        self.ui.button.clicked.connect(self.clicked)

    def clicked(self):
        self.go_initial.emit()