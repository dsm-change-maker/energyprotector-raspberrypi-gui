# -*- coding: utf-8 -*-

from pyecharts.charts import Bar
from pyecharts import options as opts
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import *
from package.ui.page_usage_time_ui import Ui_pageUsageTime
from package.utils import get_project_root
from package.utils import request_failed


class PageUsageTime(QWidget):
    def __init__(self, apis):
        super().__init__()
        self.apis = apis
        self.ui = Ui_pageUsageTime()
        self.day_times = [80, 90, 100, 110, 120]
        self.month_times = [100, 200, 300, 400, 500]
        self.year_times = [400, 500, 600, 700, 800]
        self.init_data()
        self.setup_ui()

    def initial(self):
        res = self.apis.usage.get(year=True, year_n=5, month=True, month_n=5, day=True, day_n=5)
        if res[0]:
            self.day_times = list(map(lambda _, time: int(time), res[2]['day']))
            self.month_times = list(map(lambda _, time: int(time), res[2]['month']))
            self.year_times = list(map(lambda _, time: int(time), res[2]['year']))
            self.init_data()
            self.my_html.load(QUrl('file:///' + get_project_root() + '/conf/usage_time.html'))
        else:
            request_failed('USAGE.GET')
            self.my_html.load(QUrl('file:///' + get_project_root() + '/conf/usage_time_request_failed.html'))

    def init_data(self):
        op = opts.InitOpts(width="500px", height="331px")
        bar = (
            Bar(init_opts=op)
                .add_xaxis(["-4", "-3", "-2", "-1", "0"])
                .add_yaxis("day", self.day_times)
                .add_yaxis("month", self.month_times)
                .add_yaxis("year", self.year_times)
        )
        bar.render(path=get_project_root()+'/conf/usage_time.html')

    def setup_ui(self):
        self.ui.setupUi(self)
        self.my_html = QWebEngineView()
        self.my_html.load(QUrl('file:///' + get_project_root() + '/conf/usage_time.html'))
        self.ui.verticalLayout.addWidget(self.my_html)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    pageUsageTime = PageUsageTime()
    pageUsageTime.show()

    sys.exit(app.exec())
