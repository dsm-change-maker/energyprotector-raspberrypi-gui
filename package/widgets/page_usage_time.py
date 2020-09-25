# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.ui.page_usage_time_ui import Ui_pageUsageTime
from package.widgets.sub_widgets.usage_time_graph import UsageTimeGraph


class PageUsageTime(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_pageUsageTime()
        self.setup_ui()

    def setup_ui(self):
        self.ui.setupUi(self)
        self.ui.verticalLayout.addWidget(UsageTimeGraph())


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    pageUsageTime = PageUsageTime()
    pageUsageTime.show()
    sys.exit(app.exec_())
