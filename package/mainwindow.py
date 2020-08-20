from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()
        self.setupUI()

    def setupUI(self):

        self.resize(800, 480)