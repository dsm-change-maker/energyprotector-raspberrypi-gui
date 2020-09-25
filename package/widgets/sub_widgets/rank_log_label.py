# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.ui.rank_log_label_ui import Ui_rankLogBox


class RankLogLabel(QWidget):
    def __init__(self, text):
        super().__init__()
        self.ui = Ui_rankLogBox()
        self.setup_ui()
        self.set_text(text)

    def setup_ui(self):
        self.ui.setupUi(self)

    def set_text(self, text):
        self.ui.label.setText(text)
