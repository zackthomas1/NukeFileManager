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
        self.showCode_lineEdit = QLineEdit(Form)
        self.showCode_lineEdit.setObjectName(u"showCode_lineEdit")
        self.showCode_lineEdit.setGeometry(QRect(170, 190, 340, 30))
        font = QFont()
        font.setPointSize(16)
        self.showCode_lineEdit.setFont(font)
        self.showCode_label = QLabel(Form)
        self.showCode_label.setObjectName(u"showCode_label")
        self.showCode_label.setGeometry(QRect(30, 180, 131, 51))
        self.showCode_label.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 340, 180, 30))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.showCode_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Show Code", None))
        self.showCode_label.setText(QCoreApplication.translate("Form", u"Show Code: ", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Create Show Project Structure", None))
    # retranslateUi

