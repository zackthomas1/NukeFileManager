# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ShotBuilder_GUI_v001.ui'
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
        self.EnterShotChode_lineEdit = QLineEdit(Form)
        self.EnterShotChode_lineEdit.setObjectName(u"EnterShotChode_lineEdit")
        self.EnterShotChode_lineEdit.setGeometry(QRect(140, 200, 340, 30))
        font = QFont()
        font.setPointSize(16)
        self.EnterShotChode_lineEdit.setFont(font)
        self.shotCode_label = QLabel(Form)
        self.shotCode_label.setObjectName(u"shotCode_label")
        self.shotCode_label.setGeometry(QRect(30, 205, 101, 21))
        self.shotCode_label.setFont(font)
        self.CreateShot_pushButton = QPushButton(Form)
        self.CreateShot_pushButton.setObjectName(u"CreateShot_pushButton")
        self.CreateShot_pushButton.setGeometry(QRect(190, 250, 180, 30))
        font1 = QFont()
        font1.setPointSize(12)
        self.CreateShot_pushButton.setFont(font1)
        self.selectedShow_label = QLabel(Form)
        self.selectedShow_label.setObjectName(u"selectedShow_label")
        self.selectedShow_label.setGeometry(QRect(30, 140, 450, 30))
        self.selectedShow_label.setFont(font)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.EnterShotChode_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Shot Code", None))
        self.shotCode_label.setText(QCoreApplication.translate("Form", u"Shot Code:", None))
        self.CreateShot_pushButton.setText(QCoreApplication.translate("Form", u"Create Shot Folder", None))
        self.selectedShow_label.setText(QCoreApplication.translate("Form", u"Currently Selected Show: None", None))
    # retranslateUi

