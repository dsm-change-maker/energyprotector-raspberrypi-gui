from PyQt5.QtWidgets import *
from package.control_energy_button import ControlEnergyButton
from package.ui.page_control_energy_ui import Ui_controlEnergyPage


class PageControlEnergy(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_controlEnergyPage()
        self.setup_ui()

    def setup_ui(self):
        self.ui.setupUi(self)
        self.add_control_buttons()

    def add_control_buttons(self):
        switch_count = 3
        plug_count = 3

        for n in range(switch_count):
            item = QListWidgetItem(self.ui.switchListWidget)
            control_button = ControlEnergyButton()
            control_button.set_text("스위치" + str(n))

            print("TEST" + str(control_button.sizeHint()))
            item.setSizeHint(control_button.sizeHint())
            self.ui.switchListWidget.setItemWidget(item, control_button)
            self.ui.switchListWidget.addItem(item)

        for n in range(plug_count):
            item = QListWidgetItem(self.ui.plugListWidget)
            control_button = ControlEnergyButton()
            control_button.set_text("플러그" + str(n))

            item.setSizeHint(control_button.sizeHint())
            self.ui.plugListWidget.setItemWidget(item, control_button)
            self.ui.plugListWidget.addItem(item)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    pageControlEnergy = PageControlEnergy()
    pageControlEnergy.show()
    sys.exit(app.exec_())
