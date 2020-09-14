from package.utils import password_validation
from PyQt5.QtWidgets import *
from package.ui.initial_setup_ui import Ui_initialSetupWidget
from package.device_setting import DeviceSetting


class InitialSetupUI(QStackedWidget):
    def __init__(self, device_setting:DeviceSetting):
        super().__init__()
        self.page = 0
        self.re_password = ""
        self.password_wrong = False
        self.device_setting = device_setting
        self.ui = Ui_initialSetupWidget()

        self.init_device_setting()
        self.setup_ui()
        self.set_signals()
        self.setCurrentIndex(self.page)

    def init_device_setting(self):
        self.device_setting.get_id()
        self.device_setting.auto_control = False
        self.device_setting.remote_control = True

    def setup_ui(self):
        self.ui.setupUi(self)
        self.ui.id_read_only.setText("디바이스 아이디 : " + self.device_setting.id)
        self.set_page_control_setting_style(self.ui.auto_control_button, self.device_setting.auto_control)
        self.set_page_control_setting_style(self.ui.remote_control_button, self.device_setting.remote_control)
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
        self.device_setting.print()
        self.next_page()

    def finish_page_set_password(self):
        pw_res = password_validation(self.device_setting.password)
        if not pw_res[0]:
            self.ui.password_edit.setText("")
            self.ui.password_re_edit.setText("")
            self.ui.password_setting_button.setText(pw_res[1])
            self.ui.notice_wrong_label.setText("!")
            self.ui.notice_wrong_label_2.setText("!")
            self.password_wrong = True
            return

        if len(self.re_password) is 0:
            self.ui.password_re_edit.setText("")
            self.ui.password_setting_button.setText("'비밀번호 확인'을 입력해주세요")
            self.ui.notice_wrong_label_2.setText("!")
            self.password_wrong = True
            return

        if self.device_setting.password == self.re_password:
            temp_password = self.ui.password_edit.text()
            self.ui.password_edit.setText("")
            self.ui.password_re_edit.setText("")
            self.device_setting.set_password(temp_password)
            self.next_page()
        else:
            self.ui.password_re_edit.setText("")
            self.ui.password_setting_button.setText("재입력한 비밀번호가 잘못되었습니다")
            self.ui.notice_wrong_label_2.setText("!")
            self.password_wrong = True

    def set_password(self):
        if self.password_wrong:
            self.ui.password_setting_button.setText("비밀번호 설정")
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        self.device_setting.set_password(self.ui.password_edit.text())

    def set_re_password(self):
        if self.password_wrong:
            self.ui.password_setting_button.setText("비밀번호 설정")
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        self.re_password = self.ui.password_re_edit.text()

    def set_page_control_setting_style(self, button, state):
        if state:
            button.setText("ON")
            button.setStyleSheet("border:none;\n"
                                 "background-color: rgb(48, 216, 136);\n"
                                 "color: white;\n"
                                 "border-top-right-radius: 8%;\n"
                                 "border-bottom-right-radius: 8%;")
        else:
            button.setText("OFF")
            button.setStyleSheet("border:none;\n"
                                 "background-color: rgb(242, 160, 160);\n"
                                 "color: white;\n"
                                 "border-top-right-radius: 8%;\n"
                                 "border-bottom-right-radius: 8%;")

    def toggle_auto_control(self):
        if self.device_setting.auto_control:
            self.device_setting.auto_control = False
        else:
            self.device_setting.auto_control = True

        self.set_page_control_setting_style(self.ui.auto_control_button, self.device_setting.auto_control)

    def toggle_remote_control(self):
        if self.device_setting.remote_control:
            self.device_setting.remote_control = False
        else:
            self.device_setting.remote_control = True

        self.set_page_control_setting_style(self.ui.remote_control_button, self.device_setting.remote_control)

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
