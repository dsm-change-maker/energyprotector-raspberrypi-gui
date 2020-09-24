import re
from pathlib import Path
from PyQt5.QtWidgets import QPushButton


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


def process_res(response):
    data = response.json()
    if str(response.status_code)[0] == '4':
        return [False, response.status_code, data.message]
    return [True, response.status_code, data.data]


def file_read_one(file_name):
    f = open(file_name, "r")
    res = f.readline()
    f.close()
    return res


def password_validation(password) -> [bool, str]:
    if len(password) is 0:
        return [False, "비밀번호를 입력해주세요"]

    if 0 < len(password) < 10:
        return [False, "비밀번호 길이가 10보다 작습니다."]

    if re.search(r'\s', password):
        return [False, "공백이 포함되어 있습니다."]

    if not re.search(r'\d', password) or not re.search(r'\D', password):
        return [False, "문자 + 숫자으로 만들어주세요."]

    return [True, "비밀번호 설정"]


def set_control_setting_style(button: QPushButton, state: bool):
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


def finish_set_password(object, password_button) -> bool:
    pw_res = password_validation(object.password)
    if not pw_res[0]:
        object.ui.password_edit.setText("")
        object.ui.password_re_edit.setText("")
        object.password = ""
        object.re_password = ""
        object.ui.notice_wrong_label.setText("!")
        object.ui.notice_wrong_label_2.setText("!")
        object.password_wrong = True
        password_button.setText(pw_res[1])
        return False

    if len(object.password) > 0 and len(object.re_password) is 0:
        object.ui.password_re_edit.setText("")
        object.re_password = ""
        object.ui.notice_wrong_label.setText("")
        object.ui.notice_wrong_label_2.setText("!")
        object.password_wrong = True
        password_button.setText("'비밀번호 확인'을 입력해주세요")
        return False

    if object.password == object.re_password:
        temp_password = object.ui.password_edit.text()
        object.ui.password_edit.setText("")
        object.ui.password_re_edit.setText("")
        object.password = ""
        object.re_password = ""
        object.password = temp_password
        return True
    else:
        object.ui.password_re_edit.setText("")
        object.re_password = ""
        object.ui.notice_wrong_label_2.setText("!")
        object.password_wrong = True
        password_button.setText("재입력한 비밀번호가 잘못되었습니다")
    return False


if __name__ == "__main__":
    print("-get_project_root() test-")
    print(get_project_root())
    print("\n-password_validation() test-")
    print(password_validation("hello world"))  # False
    print(password_validation("good evening baby 1001"))  # False
    print(password_validation("helloWorldGoodEveningGOOD"))  # False
    print(password_validation("123458390803802380829080234"))  # False
    print(password_validation("hell"))  # False
    print(password_validation("helloWorldBaby1234"))  # True
