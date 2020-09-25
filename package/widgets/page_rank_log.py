# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from package.ui.page_rank_log_ui import Ui_pageRankLog
from package.widgets.sub_widgets.rank_log_label import RankLogLabel

class PageRankLog(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_pageRankLog()
        self.setup_ui()

        self.log_count = 100
        self.rank_log = []
        self.ui.tableWidget.setRowCount(self.log_count)
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setFocusPolicy(Qt.NoFocus)
        for n in range(self.log_count):
            self.ui.tableWidget.setCellWidget(n, 0, RankLogLabel("2020년 0월 0위 : 000시간"))

    def setup_ui(self):
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    pageRankLog = PageRankLog()
    pageRankLog.show()
    sys.exit(app.exec_())
