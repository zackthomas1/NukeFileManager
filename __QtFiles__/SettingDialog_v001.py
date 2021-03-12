# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SettingDialog_v001.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Settings_Dialog(object):
    def setupUi(self, Settings_Dialog):
        if not Settings_Dialog.objectName():
            Settings_Dialog.setObjectName(u"Settings_Dialog")
        Settings_Dialog.setWindowModality(Qt.WindowModal)
        Settings_Dialog.resize(480, 150)
        self.directory_lineEdit = QLineEdit(Settings_Dialog)
        self.directory_lineEdit.setObjectName(u"directory_lineEdit")
        self.directory_lineEdit.setGeometry(QRect(120, 40, 340, 30))
        font = QFont()
        font.setPointSize(12)
        self.directory_lineEdit.setFont(font)
        self.directory_lineEdit.setAlignment(Qt.AlignCenter)
        self.directory_label = QLabel(Settings_Dialog)
        self.directory_label.setObjectName(u"directory_label")
        self.directory_label.setGeometry(QRect(20, 30, 90, 51))
        self.directory_label.setFont(font)
        self.ok_buttonBox = QDialogButtonBox(Settings_Dialog)
        self.ok_buttonBox.setObjectName(u"ok_buttonBox")
        self.ok_buttonBox.setGeometry(QRect(170, 110, 156, 23))
        self.ok_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Settings_Dialog)

        QMetaObject.connectSlotsByName(Settings_Dialog)
    # setupUi

    def retranslateUi(self, Settings_Dialog):
        Settings_Dialog.setWindowTitle(QCoreApplication.translate("Settings_Dialog", u"Settings Dialog", None))
        self.directory_lineEdit.setPlaceholderText(QCoreApplication.translate("Settings_Dialog", u"Enter Root Directory", None))
        self.directory_label.setText(QCoreApplication.translate("Settings_Dialog", u"Root \n"
"Directory:", None))
    # retranslateUi

