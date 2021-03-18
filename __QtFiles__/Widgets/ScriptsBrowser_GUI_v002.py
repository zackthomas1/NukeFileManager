# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ScriptsBrowser_GUI_v002.ui'
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
        Form.resize(550, 799)
        self.scriptBrowser_widget = QWidget(Form)
        self.scriptBrowser_widget.setObjectName(u"scriptBrowser_widget")
        self.scriptBrowser_widget.setGeometry(QRect(0, 0, 550, 800))
        self.scriptBrowser_widget.setCursor(QCursor(Qt.ArrowCursor))
        self.shotCode_comboBox = QComboBox(self.scriptBrowser_widget)
        self.shotCode_comboBox.setObjectName(u"shotCode_comboBox")
        self.shotCode_comboBox.setGeometry(QRect(140, 410, 340, 30))
        font = QFont()
        font.setPointSize(12)
        self.shotCode_comboBox.setFont(font)
        self.showCode_comboBox = QComboBox(self.scriptBrowser_widget)
        self.showCode_comboBox.setObjectName(u"showCode_comboBox")
        self.showCode_comboBox.setGeometry(QRect(140, 370, 340, 30))
        self.showCode_comboBox.setFont(font)
        self.launchNukeIndie_pushButton = QPushButton(self.scriptBrowser_widget)
        self.launchNukeIndie_pushButton.setObjectName(u"launchNukeIndie_pushButton")
        self.launchNukeIndie_pushButton.setGeometry(QRect(200, 640, 200, 40))
        font1 = QFont()
        font1.setPointSize(16)
        self.launchNukeIndie_pushButton.setFont(font1)
        self.scripts_listView = QListView(self.scriptBrowser_widget)
        self.scripts_listView.setObjectName(u"scripts_listView")
        self.scripts_listView.setGeometry(QRect(15, 10, 520, 340))
        self.scripts_listView.setFont(font)
        self.scripts_listView.setTextElideMode(Qt.ElideMiddle)
        self.scripts_listView.setMovement(QListView.Free)
        self.show_label = QLabel(self.scriptBrowser_widget)
        self.show_label.setObjectName(u"show_label")
        self.show_label.setGeometry(QRect(60, 370, 58, 25))
        self.show_label.setFont(font1)
        self.shot_label = QLabel(self.scriptBrowser_widget)
        self.shot_label.setObjectName(u"shot_label")
        self.shot_label.setGeometry(QRect(70, 410, 51, 25))
        self.shot_label.setFont(font1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(accessibility)
        self.scriptBrowser_widget.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.launchNukeIndie_pushButton.setText(QCoreApplication.translate("Form", u"Launch Nuke Indie", None))
        self.show_label.setText(QCoreApplication.translate("Form", u"Show:", None))
        self.shot_label.setText(QCoreApplication.translate("Form", u"Shot: ", None))
    # retranslateUi

