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
        Settings_Dialog.resize(491, 216)
        self.rootDirectory_lineEdit = QLineEdit(Settings_Dialog)
        self.rootDirectory_lineEdit.setObjectName(u"rootDirectory_lineEdit")
        self.rootDirectory_lineEdit.setGeometry(QRect(140, 40, 340, 30))
        font = QFont()
        font.setPointSize(12)
        self.rootDirectory_lineEdit.setFont(font)
        self.rootDirectory_lineEdit.setAlignment(Qt.AlignCenter)
        self.rootDirectory_label = QLabel(Settings_Dialog)
        self.rootDirectory_label.setObjectName(u"rootDirectory_label")
        self.rootDirectory_label.setGeometry(QRect(20, 30, 111, 51))
        self.rootDirectory_label.setFont(font)
        self.ok_buttonBox = QDialogButtonBox(Settings_Dialog)
        self.ok_buttonBox.setObjectName(u"ok_buttonBox")
        self.ok_buttonBox.setGeometry(QRect(180, 170, 156, 23))
        self.ok_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.NukeExe_lineEdit = QLineEdit(Settings_Dialog)
        self.NukeExe_lineEdit.setObjectName(u"NukeExe_lineEdit")
        self.NukeExe_lineEdit.setGeometry(QRect(140, 90, 340, 30))
        self.NukeExe_lineEdit.setFont(font)
        self.NukeExe_lineEdit.setAlignment(Qt.AlignCenter)
        self.NukeExe_label = QLabel(Settings_Dialog)
        self.NukeExe_label.setObjectName(u"NukeExe_label")
        self.NukeExe_label.setGeometry(QRect(20, 80, 111, 51))
        self.NukeExe_label.setFont(font)

        self.retranslateUi(Settings_Dialog)

        QMetaObject.connectSlotsByName(Settings_Dialog)
    # setupUi

    def retranslateUi(self, Settings_Dialog):
        Settings_Dialog.setWindowTitle(QCoreApplication.translate("Settings_Dialog", u"Settings Dialog", None))
        self.rootDirectory_lineEdit.setPlaceholderText(QCoreApplication.translate("Settings_Dialog", u"Enter Root Directory", None))
        self.rootDirectory_label.setText(QCoreApplication.translate("Settings_Dialog", u"Root Directory:", None))
        self.NukeExe_lineEdit.setPlaceholderText(QCoreApplication.translate("Settings_Dialog", u"Enter Path to Nuke Executable", None))
        self.NukeExe_label.setText(QCoreApplication.translate("Settings_Dialog", u"Nuke Exe Path:", None))
    # retranslateUi

