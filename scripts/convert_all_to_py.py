import os

if __name__ == '__main__':
    print("--Convert .qrc files to py--")
    os.system("python ./scripts/convert_qrc_to_py.py . .")
    print("--Convert .ui files to py--")
    os.system("python ./scripts/convert_ui_to_py.py designer package/ui")