# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.mainwindow import MainWindow
from package.socket_client import SocketClientRaspberryThread

QApplication.setApplicationName('에너지 지킴이')
QApplication.setApplicationVersion('0.1')

raspberry_id = 'BTY2_7caa0e2f'
raspberry_group = 'DSMHS_7cbf72b9'
SERVER_HOST = '3.35.25.172'
SERVER_PORT = 58495


def run():
    import sys

    socket_client_thread = SocketClientRaspberryThread(raspberry_id, raspberry_group, SERVER_HOST, SERVER_PORT,
                                                       debug=False)
    socket_client_thread.start()

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    return app.exec_()
