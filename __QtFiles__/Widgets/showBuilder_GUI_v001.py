# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShowBuilder_GUI_v001.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 800)
        self.EnterShowChode_lineEdit = QLineEdit(Form)
        self.EnterShowChode_lineEdit.setObjectName(u"EnterShowChode_lineEdit")
        self.EnterShowChode_lineEdit.setGeometry(QRect(140, 200, 340, 30))
        font = QFont()
        font.setPointSize(16)
        self.EnterShowChode_lineEdit.setFont(font)
        self.showCode_label = QLabel(Form)
        self.showCode_label.setObjectName(u"showCode_label")
        self.showCode_label.setGeometry(QRect(20, 205, 111, 20))
        self.showCode_label.setFont(font)
        self.CreateShow_pushButton = QPushButton(Form)
        self.CreateShow_pushButton.setObjectName(u"CreateShow_pushButton")
        self.CreateShow_pushButton.setGeometry(QRect(190, 250, 230, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.CreateShow_pushButton.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.EnterShowChode_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Show Code", None))
        self.showCode_label.setText(QCoreApplication.translate("Form", u"Show Code: ", None))
        self.CreateShow_pushButton.setText(QCoreApplication.translate("Form", u"Create Show Project Structure", None))
    # retranslateUi

