# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_login(QtWidgets.QDialog):
    def setupUi(self, login):
        super().__init__()
        login.setObjectName("login")
        login.resize(400, 600)
        login.setMinimumSize(QtCore.QSize(400, 600))
        login.setMaximumSize(QtCore.QSize(400, 600))
        self.login_Label = QtWidgets.QLabel(login)
        self.login_Label.setGeometry(QtCore.QRect(40, 90, 320, 80))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(32)
        font.setBold(False)
        font.setWeight(50)
        self.login_Label.setFont(font)
        self.login_Label.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login_Label.setObjectName("login_Label")
        self.register_pushButton = QtWidgets.QPushButton(login)
        self.register_pushButton.setGeometry(QtCore.QRect(90, 230, 211, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.register_pushButton.setFont(font)
        self.register_pushButton.setObjectName("register_pushButton")
        self.verification_pushButton = QtWidgets.QPushButton(login)
        self.verification_pushButton.setGeometry(QtCore.QRect(90, 370, 211, 81))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(24)
        self.verification_pushButton.setFont(font)
        self.verification_pushButton.setObjectName("verification_pushButton")

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "Voiceprint Recognition"))
        login.setWhatsThis(_translate("login", "<html><head/><body><p>声纹识别系统</p></body></html>"))
        self.login_Label.setText(_translate("login", "声纹识别系统"))
        self.register_pushButton.setText(_translate("login", "用户注册"))
        self.verification_pushButton.setText(_translate("login", "身份验证"))
