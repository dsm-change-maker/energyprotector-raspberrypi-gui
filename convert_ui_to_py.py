import os


if __name__ == "__main__":
	os.system("pyrcc5 .\\resources.qrc > .\\package\\ui\\resources_rc.py")
	os.system("pyuic5 -x .\\designer\\initial_setup_start.ui -o .\\package\\ui\\initial_setup_start_ui.py")
	os.system("pyuic5 -x .\\designer\\initial_setup_set_password.ui -o .\\package\\ui\\initial_setup_set_password_ui.py")
	os.system("pyuic5 -x .\\designer\\initial_setup_control_setting.ui -o .\\package\\ui\\initial_setup_control_setting_ui.py")