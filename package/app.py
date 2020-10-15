# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import *
from package.mainwindow import MainWindow
from package.socket_client import SocketClientRaspberryThread

QApplication.setApplicationName('에너지 지킴이')
QApplication.setApplicationVersion('0.1')

raspberry_id = 'rasp_id_1'
raspberry_group = 'rasp_group_1'
SERVER_HOST = '192.168.43.15'
SERVER_PORT = 7770


def run():
    import sys

    socket_client_thread = SocketClientRaspberryThread(raspberry_id, raspberry_group, SERVER_HOST, SERVER_PORT, debug=False)
    socket_client_thread.start()

    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    return app.exec_()
