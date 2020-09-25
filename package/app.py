# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.mainwindow import MainWindow

QApplication.setApplicationName('에너지 지킴이')
QApplication.setApplicationVersion('0.1')


def run():
    import sys
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    return app.exec_()
