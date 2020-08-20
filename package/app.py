from PyQt5.QtWidgets import *
from package.mainwindow import MainWindow

QApplication.setApplicationName('에너지 지킴이')
QApplication.setApplicationVersion('0.1')

def run():
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    return app.exec_()
