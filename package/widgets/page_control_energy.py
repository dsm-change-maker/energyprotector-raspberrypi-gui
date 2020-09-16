from PyQt5.QtWidgets import *
from package.ui.page_control_energy_ui import Ui_pageControlEnergy
from package.widgets.sub_widgets.control_energy_button import ControlEnergyButton


class PageControlEnergy(QWidget):
    def __init__(self):
        super().__init__()
        self.switch_count = 3
        self.plug_count = 4
        self.switch_buttons = []
        self.plug_buttons = []
        self.ui = Ui_pageControlEnergy()
        self.setup_ui()

    def setup_ui(self):
        self.ui.setupUi(self)
        self.add_control_buttons()

    def add_control_buttons(self):
        for n in range(self.switch_count):
            self.switch_buttons.append(ControlEnergyButton())
            self.switch_buttons[n].set_text("스위치" + str(n+1))
            self.ui.gridLayout.addWidget(self.switch_buttons[n], n, 0)

        for n in range(self.plug_count):
            self.plug_buttons.append(ControlEnergyButton())
            self.plug_buttons[n].set_text("플러그" + str(n+1))
            self.ui.gridLayout.addWidget(self.plug_buttons[n], n, 1)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    pageControlEnergy = PageControlEnergy()
    pageControlEnergy.show()
    sys.exit(app.exec_())
