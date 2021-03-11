# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'directoryDialog_v001.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Directory_Dialog(object):
    def setupUi(self, Directory_Dialog):
        if not Directory_Dialog.objectName():
            Directory_Dialog.setObjectName(u"Directory_Dialog")
        Directory_Dialog.setWindowModality(Qt.WindowModal)
        Directory_Dialog.resize(476, 159)
        self.directory_lineEdit = QLineEdit(Directory_Dialog)
        self.directory_lineEdit.setObjectName(u"directory_lineEdit")
        self.directory_lineEdit.setGeometry(QRect(120, 40, 340, 30))
        font = QFont()
        font.setPointSize(12)
        self.directory_lineEdit.setFont(font)
        self.directory_lineEdit.setAlignment(Qt.AlignCenter)
        self.directory_label = QLabel(Directory_Dialog)
        self.directory_label.setObjectName(u"directory_label")
        self.directory_label.setGeometry(QRect(20, 38, 91, 31))
        font1 = QFont()
        font1.setPointSize(16)
        self.directory_label.setFont(font1)
        self.ok_buttonBox = QDialogButtonBox(Directory_Dialog)
        self.ok_buttonBox.setObjectName(u"ok_buttonBox")
        self.ok_buttonBox.setGeometry(QRect(170, 110, 156, 23))
        self.ok_buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.retranslateUi(Directory_Dialog)

        QMetaObject.connectSlotsByName(Directory_Dialog)
    # setupUi

    def retranslateUi(self, Directory_Dialog):
        Directory_Dialog.setWindowTitle(QCoreApplication.translate("Directory_Dialog", u"Dialog", None))
        self.directory_lineEdit.setPlaceholderText(QCoreApplication.translate("Directory_Dialog", u"Enter Root Directory", None))
        self.directory_label.setText(QCoreApplication.translate("Directory_Dialog", u"Directory:", None))
    # retranslateUi

