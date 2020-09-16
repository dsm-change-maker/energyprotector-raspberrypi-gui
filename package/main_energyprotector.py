from PyQt5.QtWidgets import *
from package.ui.main_energyprotector_ui import Ui_MainWindow
from package.widgets.page_control_energy import PageControlEnergy
from package.widgets.page_rank_log import PageRankLog

class MainEnergyProtectorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setup_ui()
        self.set_signals()

    def setup_ui(self):
        self.ui.setupUi(self)
        self.page_control_energy = PageControlEnergy()
        self.page_control_energy1 = PageControlEnergy()
        self.page_rank_log = PageRankLog()
        self.page_control_energy2 = PageControlEnergy()
        self.ui.pagesWidget.insertWidget(0,self.page_control_energy)
        self.ui.pagesWidget.insertWidget(1,self.page_rank_log)
        self.ui.pagesWidget.insertWidget(2,self.page_control_energy1)
        self.ui.pagesWidget.insertWidget(3,self.page_control_energy2)
        self.ui.pagesWidget.setCurrentIndex(0)

    def set_signals(self):
        self.ui.go_control_energy_button.clicked.connect(self.go_control_energy_page)
        self.ui.go_rank_log_button.clicked.connect(self.go_rank_log_page)
        self.ui.go_usage_graph_button.clicked.connect(self.go_usage_graph_page)
        self.ui.go_setting_button.clicked.connect(self.go_setting_page)

    def go_control_energy_page(self):
        self.ui.pagesWidget.setCurrentIndex(0)

    def go_rank_log_page(self):
        self.ui.pagesWidget.setCurrentIndex(1)

    def go_usage_graph_page(self):
        self.ui.pagesWidget.setCurrentIndex(2)

    def go_setting_page(self):
        self.ui.pagesWidget.setCurrentIndex(3)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainEnergyProtectorWindow = MainEnergyProtectorUI()
    mainEnergyProtectorWindow.show()
    sys.exit(app.exec_())