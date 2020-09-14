import re
import bcrypt
from pathlib import Path


def get_project_root() -> Path:
    """Returns project root folder."""
    return Path(__file__).parent.parent


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


def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def check_password(hashed_password, password):
    bcrypt.checkpw(password.encode('utf-8'), hashed_password)


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
