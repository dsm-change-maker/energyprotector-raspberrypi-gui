from PyQt5.QtWidgets import *
from package.ui.page_setting_ui import Ui_pageSetting
from package.device_setting import DeviceSetting
from package.utils import set_control_setting_style
from package.utils import finish_set_password


class PageSetting(QWidget):
    def __init__(self, device_setting: DeviceSetting):
        super().__init__()
        self.device_setting = device_setting
        self.device_setting.load_conf()
        self.password = ""
        self.re_password = ""
        self.password_wrong = False
        self.exist_message = False
        self.auto_control = self.device_setting.auto_control
        self.remote_control = self.device_setting.remote_control

        self.ui = Ui_pageSetting()
        self.setup_ui()
        self.set_signals()

    def initial(self):
        self.device_setting.load_conf()
        self.password = ""
        self.re_password = ""
        self.password_wrong = False
        self.exist_message = False
        self.auto_control = self.device_setting.auto_control
        self.remote_control = self.device_setting.remote_control
        self.ui.change_setting_button.setText("설정 변경하기")
        self.ui.id_read_only.setText("ID & PW : '" + self.device_setting.id + "' & '" + self.device_setting.password+"'")

    def setup_ui(self):
        self.ui.setupUi(self)
        self.ui.id_read_only.setText("ID & PW : '" + self.device_setting.id + "' & '" + self.device_setting.password+"'")
        self.ui.notice_wrong_label.setText("")
        self.ui.notice_wrong_label_2.setText("")
        self.ui.change_setting_button.setText("설정 변경하기")
        set_control_setting_style(self.ui.auto_control_button, self.device_setting.auto_control)
        set_control_setting_style(self.ui.remote_control_button, self.device_setting.remote_control)

    def set_signals(self):
        self.ui.auto_control_button.clicked.connect(self.toggle_auto_control)
        self.ui.remote_control_button.clicked.connect(self.toggle_remote_control)

        self.ui.password_edit.textChanged.connect(self.set_password)
        self.ui.password_re_edit.textChanged.connect(self.set_re_password)
        self.ui.change_setting_button.clicked.connect(self.change_setting)

    def change_setting(self):
        is_pw = False
        password_is_change = False
        remote_control_is_change = False
        auto_control_is_change = False

        if self.remote_control is not self.device_setting.remote_control:
            self.device_setting.remote_control = self.remote_control
            remote_control_is_change = True
        if self.auto_control is not self.device_setting.auto_control:
            self.device_setting.auto_control = self.auto_control
            auto_control_is_change = True

        if len(self.password) > 0:
            is_pw = True
            if finish_set_password(self, self.ui.change_setting_button):
                if self.password is not self.device_setting.password:
                    self.device_setting.password = self.password
                    password_is_change = True
            else:
                self.exist_message = True
        else:
            if len(self.re_password) > 0:
                self.ui.password_re_edit.setText("")
            else:
                self.ui.notice_wrong_label.setText("")
                self.ui.notice_wrong_label_2.setText("")

        if password_is_change and not remote_control_is_change and not auto_control_is_change:
            self.ui.change_setting_button.setText("비밀번호가 변경되었습니다.")
            self.exist_message = True
        elif remote_control_is_change and not password_is_change and not auto_control_is_change:
            self.ui.change_setting_button.setText("원격 제어 설정이 변경되었습니다.")
            self.exist_message = True
        elif auto_control_is_change and not password_is_change and not remote_control_is_change:
            self.ui.change_setting_button.setText("자동 OFF 설정이 변경되었습니다.")
            self.exist_message = True
        elif remote_control_is_change and auto_control_is_change and not password_is_change:
            self.ui.change_setting_button.setText("원격 제어/자동 OFF 설정이 변경되었습니다.")
            self.exist_message = True
        elif password_is_change and remote_control_is_change and not auto_control_is_change:
            self.ui.change_setting_button.setText("원격제어 설정/비밀번호가 변경되었습니다.")
            self.exist_message = True
        elif password_is_change and auto_control_is_change and not remote_control_is_change:
            self.ui.change_setting_button.setText("자동 OFF 설정/비밀번호가 변경되었습니다.")
            self.exist_message = True
        elif password_is_change and auto_control_is_change and remote_control_is_change:
            self.ui.change_setting_button.setText("비밀번호/원격 제어/자동 OFF 설정이 변경되었습니다.")
            self.exist_message = True
        else:
            if not is_pw:
                self.ui.change_setting_button.setText("설정이 변경되지 않았습니다.")
                self.exist_message = True
        self.password = ""
        self.re_password = ""
        self.ui.id_read_only.setText("ID & PW : '" + self.device_setting.id + "' & '" + self.device_setting.password+"'")
        self.device_setting.write()

    def set_password(self):
        if self.password_wrong or self.exist_message:
            self.ui.change_setting_button.setText("설정 변경하기")
            self.exist_message = False
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        self.password = self.ui.password_edit.text()

    def set_re_password(self):
        if self.password_wrong or self.exist_message:
            self.ui.change_setting_button.setText("설정 변경하기")
            self.exist_message = False
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        self.re_password = self.ui.password_re_edit.text()

    def toggle_auto_control(self):
        self.auto_control = not self.auto_control
        if self.exist_message:
            self.exist_message = False
            self.ui.change_setting_button.setText("설정 변경하기")
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        set_control_setting_style(self.ui.auto_control_button, self.auto_control)

    def toggle_remote_control(self):
        self.remote_control = not self.remote_control
        if self.exist_message:
            self.exist_message = False
            self.ui.change_setting_button.setText("설정 변경하기")
            self.ui.notice_wrong_label.setText("")
            self.ui.notice_wrong_label_2.setText("")
        set_control_setting_style(self.ui.remote_control_button, self.remote_control)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    device_setting = DeviceSetting()
    pageSetting = PageSetting(device_setting)
    pageSetting.show()
    sys.exit(app.exec_())
