# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\designer\initial_setup_control_setting.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_initialSetupControlSettingWidget(object):
    def setupUi(self, initialSetupControlSettingWidget):
        initialSetupControlSettingWidget.setObjectName("initialSetupControlSettingWidget")
        initialSetupControlSettingWidget.resize(800, 468)
        initialSetupControlSettingWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.settingTextLabel = QtWidgets.QLabel(initialSetupControlSettingWidget)
        self.settingTextLabel.setGeometry(QtCore.QRect(170, 50, 460, 91))
        self.settingTextLabel.setStyleSheet("#settingTextLabel {\n"
"font: 25pt \"나눔바른펜\";\n"
"\n"
"}")
        self.settingTextLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.settingTextLabel.setObjectName("settingTextLabel")
        self.setting1Label = QtWidgets.QLabel(initialSetupControlSettingWidget)
        self.setting1Label.setGeometry(QtCore.QRect(170, 160, 460, 41))
        font = QtGui.QFont()
        font.setFamily("나눔바른펜")
        font.setPointSize(14)
        self.setting1Label.setFont(font)
        self.setting1Label.setStyleSheet("#setting1Label {\n"
"border: 1px solid #ddd;\n"
"}")
        self.setting1Label.setAlignment(QtCore.Qt.AlignCenter)
        self.setting1Label.setObjectName("setting1Label")
        self.setting2Label = QtWidgets.QLabel(initialSetupControlSettingWidget)
        self.setting2Label.setGeometry(QtCore.QRect(170, 220, 460, 41))
        font = QtGui.QFont()
        font.setFamily("나눔바른펜")
        font.setPointSize(14)
        self.setting2Label.setFont(font)
        self.setting2Label.setStyleSheet("#setting2Label {\n"
"border: 1px solid #ddd;\n"
"}")
        self.setting2Label.setAlignment(QtCore.Qt.AlignCenter)
        self.setting2Label.setObjectName("setting2Label")
        self.settingFinishButton = QtWidgets.QPushButton(initialSetupControlSettingWidget)
        self.settingFinishButton.setGeometry(QtCore.QRect(170, 280, 460, 41))
        font = QtGui.QFont()
        font.setFamily("나눔바른펜")
        font.setPointSize(14)
        self.settingFinishButton.setFont(font)
        self.settingFinishButton.setStyleSheet("#settingFinishButton {\n"
"background-color:rgb(242, 160, 160);\n"
"color: white;\n"
"border: none;\n"
"}")
        self.settingFinishButton.setObjectName("settingFinishButton")
        self.setting1ToggleButton = QtWidgets.QPushButton(initialSetupControlSettingWidget)
        self.setting1ToggleButton.setGeometry(QtCore.QRect(520, 160, 111, 41))
        font = QtGui.QFont()
        font.setFamily("나눔바른펜")
        font.setPointSize(12)
        self.setting1ToggleButton.setFont(font)
        self.setting1ToggleButton.setStyleSheet("#setting1ToggleButton {\n"
"border:none;\n"
"    background-color: rgb(48, 216, 136);\n"
"color: white;\n"
"}")
        self.setting1ToggleButton.setObjectName("setting1ToggleButton")
        self.setting2ToggleButton = QtWidgets.QPushButton(initialSetupControlSettingWidget)
        self.setting2ToggleButton.setGeometry(QtCore.QRect(520, 220, 111, 41))
        font = QtGui.QFont()
        font.setFamily("나눔바른펜")
        font.setPointSize(12)
        self.setting2ToggleButton.setFont(font)
        self.setting2ToggleButton.setStyleSheet("#setting2ToggleButton {\n"
"border:none;\n"
"background-color: rgb(242, 160, 160);\n"
"color: white;\n"
"}")
        self.setting2ToggleButton.setObjectName("setting2ToggleButton")

        self.retranslateUi(initialSetupControlSettingWidget)
        QtCore.QMetaObject.connectSlotsByName(initialSetupControlSettingWidget)

    def retranslateUi(self, initialSetupControlSettingWidget):
        _translate = QtCore.QCoreApplication.translate
        initialSetupControlSettingWidget.setWindowTitle(_translate("initialSetupControlSettingWidget", "Form"))
        self.settingTextLabel.setText(_translate("initialSetupControlSettingWidget", "에너지 지킴이 설정 - 2"))
        self.setting1Label.setText(_translate("initialSetupControlSettingWidget", "사람이 없을 때 자동 OFF"))
        self.setting2Label.setText(_translate("initialSetupControlSettingWidget", "웹/앱을 통한 원격 제어"))
        self.settingFinishButton.setText(_translate("initialSetupControlSettingWidget", "DSM 에너지 지킴이 시작하기"))
        self.setting1ToggleButton.setText(_translate("initialSetupControlSettingWidget", "ON"))
        self.setting2ToggleButton.setText(_translate("initialSetupControlSettingWidget", "OFF"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    initialSetupControlSettingWidget = QtWidgets.QWidget()
    ui = Ui_initialSetupControlSettingWidget()
    ui.setupUi(initialSetupControlSettingWidget)
    initialSetupControlSettingWidget.show()
    sys.exit(app.exec_())
