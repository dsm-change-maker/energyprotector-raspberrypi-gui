from PyQt5.QtWidgets import *
from package.ui.main_energyprotector_ui import Ui_MainWindow
from package.page_control_energy import PageControlEnergy

class MainEnergyProtectorUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.setup_ui()

    def setup_ui(self):
        self.ui.setupUi(self)

        self.page_control_energy = PageControlEnergy()

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