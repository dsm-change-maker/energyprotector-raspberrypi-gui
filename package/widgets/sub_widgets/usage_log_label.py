# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.ui.usage_log_label_ui import Ui_usageLogBox


class UsageLogLabel(QWidget):
    def __init__(self, text):
        super().__init__()
        self.ui = Ui_usageLogBox()
        self.setup_ui()
        self.set_text(text)

    def setup_ui(self):
        self.ui.setupUi(self)

    def set_text(self, text):
        self.ui.label.setText(text)
