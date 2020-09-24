from PyQt5.QtWidgets import *
from package.ui.initial_setup_ui import Ui_initialSetupWidget
from package.device_setting import DeviceSetting
from package.utils import set_control_setting_style
from package.utils import finish_set_password


class InitialSetupUI(QStackedWidget):
    def __init__(self, device_setting: DeviceSetting):
        super().__init__()
        self.page = 0
        self.password = ""
        self.re_password = ""
        self.password_wrong = False
        self.device_setting = device_setting
        self.ui = Ui_initialSetupWidget()

        self.init_device_setting()
        self.setup_ui()
        self.set_signals()
        self.setCurrentIndex(self.page)

    def init(self):
        self.page = 0
        self.password = ""
        self.re_password = ""
        self.password_wrong = False
        self.init_device_setting()
        self.ui.id_read_only.setText("디바이스 그룹&아이디 : '" + self.device_setting.group + "'  & '" + self.device_setting.id + "'")
        set_control_setting_style(self.ui.auto_control_button, self.device_setting.auto_control)
        set_control_setting_style(self.ui.remote_control_button, self.device_setting.remote_control)

    def init_device_setting(self):
        self.device_setting.get_id()
        self.device_setting.get_group()
        self.device_setting.password = ""
        self.device_setting.auto_control = True
        self.device_setting.remote_control = True

    def setup_ui(self):
        self.ui.setupUi(self)
        self.ui.id_read_only.setText("디바이스 아이디 : " + self.device_setting.id)
        set_control_setting_style(self.ui.auto_control_button, self.device_setting.auto_control)
        set_control_setting_style(self.ui.remote_control_button, self.device_setting.remote_control)
        self.ui.notice_wrong_label.setText("")
        self.ui.notice_wrong_label_2.setText("")

    def set_signals(self):
        # page_start
        self.ui.start_button.clicked.connect(self.next_page)
        # page_set_password
        self.ui.password_setting_button.clicked.connect(self.finish_page_set_password)
        self.ui.password_edit.textChanged.connect(self.set_password)
        self.ui.password_re_edit.textChanged.connect(self.set_re_password)
        # page_control_setting
        self.ui.initial_setting_finish_button.clicked.connect(self.finish_initial_setting)
        self.ui.auto_control_button.clicked.connect(self.toggle_auto_control)
        self.ui.remote_control_button.clicked.connect(self.toggle_remote_control)

    def finish_initial_setting(self):
        self.device_setting.write()
        self.next_page()

    def finish_page_set_password(self):
        if len(self.password) == 0 and len(self.re_password) > 0:
            self.ui.notice_wrong_label.setText("!")
            self.ui.notice_wrong_label_2.setText("")
            self.ui.password_edit.setText("")
            self.ui.password_re_edit.setText("")
            self.ui.password_setting_button.setText("비밀번호를 입력해주세요")
            return
        if finish_set_password(self, self.ui.password_setting_button):
            self.device_setting.password = self.password
            self.next_page()

    def set_password(self):
        if self.password_wrong:
            self.ui.password_setting_button.setText("비밀번호 설정")
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        self.password = self.ui.password_edit.text()

    def set_re_password(self):
        if self.password_wrong:
            self.ui.password_setting_button.setText("비밀번호 설정")
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        self.re_password = self.ui.password_re_edit.text()

    def toggle_auto_control(self):
        self.device_setting.auto_control = not self.device_setting.auto_control
        set_control_setting_style(self.ui.auto_control_button, self.device_setting.auto_control)

    def toggle_remote_control(self):
        self.device_setting.remote_control = not self.device_setting.remote_control
        set_control_setting_style(self.ui.remote_control_button, self.device_setting.remote_control)

    def next_page(self):
        self.page += 1
        if self.page > 2:
            self.page = 0
        self.setCurrentIndex(self.page)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    device_setting = DeviceSetting()
    initialSetupWidget = InitialSetupUI(device_setting)
    initialSetupWidget.show()
    sys.exit(app.exec_())
