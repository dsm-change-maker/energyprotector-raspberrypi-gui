import os
from pathlib import Path

def get_project_root():
    """Returns project root folder."""
    return str(Path(__file__).parent.parent)

if __name__ == '__main__':
    print("--Convert .qrc files to py--")
    os.system("python " + get_project_root() + "/scripts/convert_qrc_to_py.py .. ..")
    print("--Convert .ui files to py--")
    os.system("python " + get_project_root() + "/scripts/convert_ui_to_py.py ../designer ../package/ui")