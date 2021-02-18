# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from package.ui.page_usage_log_ui import Ui_pageUsageLog
from package.widgets.sub_widgets.usage_log_label import UsageLogLabel
from package.utils import get_project_root
from package.database import DataBase

def usagelog_update(day_usage_times):
    db = DataBase(get_project_root() + '/conf/energy_protector')
    db.execute('CREATE TABLE IF NOT EXISTS usage_log (date TEXT, usage_time INT)')
    for time in day_usage_times:
        count = db.execute('SELECT COUNT(*) FROM usage_log WHERE date = ?',
                                (time[0],))[0][0]
        if count is 0:
            db.execute('INSERT INTO usage_log (date, usage_time) values (?, ?)',(time[0], time[1], ))
        else:
            db.execute('UPDATE usage_log SET usage_time=? WHERE date = ?', (time[1], time[0],))

class PageUsageLog(QWidget):
    def __init__(self, apis):
        super().__init__()
        self.apis = apis
        self.ui = Ui_pageUsageLog()
        self.setup_ui()

        self.usage_logs = []
        self.get_log()

        self.ui.tableWidget.setRowCount(len(self.usage_logs))
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setFocusPolicy(Qt.NoFocus)
        for n in range(len(self.usage_logs)):
            self.ui.tableWidget.setCellWidget(n, 0, UsageLogLabel(self.usage_logs[n]))

    def get_log(self):
        db = DataBase(get_project_root() + '/conf/energy_protector')
        db.execute('CREATE TABLE IF NOT EXISTS usage_log (date TEXT primary key, usage_time INT)')

        day_res = self.apis.usage.get(day=True, day_n=5)
        if day_res[0]:
            usagelog_update(day_res[2]['day'])

        log_count = db.execute('SELECT COUNT(*) FROM usage_log')[0][0]
        if log_count > 0:
            self.usage_logs = []
            data_list = db.execute('SELECT * FROM usage_log')
            for data in data_list:
                temp_str = data[0] + " : "
                hour = data[1] // 3600
                minute = (data[1] % 3600) // 60
                temp_str += str(hour) + "시간 " + str(minute) + "분"
                self.usage_logs.append(temp_str)
        else:
            self.usage_logs.append('사용 기록이 존재하지 않습니다.')
            self.usage_logs.append('사용 기록은 1일을 기준으로 기록됩니다.')

    def setup_ui(self):
        self.ui.setupUi(self)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    pageUsageLog = PageUsageLog()
    pageUsageLog.show()
    sys.exit(app.exec_())
