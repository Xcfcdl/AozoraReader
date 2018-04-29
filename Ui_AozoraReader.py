# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'E:\Codes\python\GUI\PyQt\AozoraReader\AozoraReader.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from getDatas import get_sakuhinnCa, get_sakusyaCa, get_kanasakuhinn, get_kanasakusya


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(878, 545)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(True)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMaximumSize(QtCore.QSize(60, 60))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("A-OTF TakaHand Std H")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("A-OTF TakaHand Std H")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem = QtWidgets.QSpacerItem(458, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.Mini_button_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Mini_button_2.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap(":/min/sources/menu.png"), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.Mini_button_2.setIcon(icon)
        self.Mini_button_2.setObjectName("Mini_button_2")
        self.horizontalLayout_5.addWidget(self.Mini_button_2)
        self.Mini_button = QtWidgets.QPushButton(self.centralwidget)
        self.Mini_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(
            QtGui.QPixmap(":/min/sources/mini.jpg"), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.Mini_button.setIcon(icon1)
        self.Mini_button.setObjectName("Mini_button")
        self.horizontalLayout_5.addWidget(self.Mini_button)
        self.max_button = QtWidgets.QPushButton(self.centralwidget)
        self.max_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(
            QtGui.QPixmap(
                ":/min/sources/641811830ab31eca1fb5d5f18fab69ab.png"),
            QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.max_button.setIcon(icon2)
        self.max_button.setObjectName("max_button")
        self.horizontalLayout_5.addWidget(self.max_button)
        self.quit_button = QtWidgets.QPushButton(self.centralwidget)
        self.quit_button.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(
            QtGui.QPixmap(":/min/sources/quit.png"), QtGui.QIcon.Normal,
            QtGui.QIcon.Off)
        self.quit_button.setIcon(icon3)
        self.quit_button.setObjectName("quit_button")
        self.horizontalLayout_5.addWidget(self.quit_button)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.treeWidget = QtWidgets.QTreeWidget(self.centralwidget)
        self.treeWidget.setMaximumSize(QtCore.QSize(200, 16777215))
        self.treeWidget.setObjectName("treeWidget")
        """列表"""
        self.item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        self.horizontalLayout_3.addWidget(self.treeWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_view = QtWidgets.QTextBrowser(self.centralwidget)
        self.label_view.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_view.setObjectName("label_view")
        self.verticalLayout.addWidget(self.label_view)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.button_read = QtWidgets.QPushButton(self.centralwidget)
        self.button_read.setObjectName("button_read")
        self.horizontalLayout_2.addWidget(self.button_read)
        self.edit_seek = QtWidgets.QTextEdit(self.centralwidget)
        self.edit_seek.setMaximumSize(QtCore.QSize(161, 25))
        self.edit_seek.setObjectName("edit_seek")
        self.horizontalLayout_2.addWidget(self.edit_seek)
        self.button_seek = QtWidgets.QPushButton(self.centralwidget)
        self.button_seek.setObjectName("button_seek")
        self.horizontalLayout_2.addWidget(self.button_seek)
        spacerItem1 = QtWidgets.QSpacerItem(146, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.button_mainPage = QtWidgets.QPushButton(self.centralwidget)
        self.button_mainPage.setObjectName("button_mainPage")
        self.horizontalLayout.addWidget(self.button_mainPage)
        self.button_lastPage = QtWidgets.QPushButton(self.centralwidget)
        self.button_lastPage.setObjectName("button_lastPage")
        self.horizontalLayout.addWidget(self.button_lastPage)
        self.button_nextPage = QtWidgets.QPushButton(self.centralwidget)
        self.button_nextPage.setStyleSheet("")
        self.button_nextPage.setObjectName("button_nextPage")
        self.horizontalLayout.addWidget(self.button_nextPage)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_7.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.f = True
        self.retranslateUi(MainWindow)
        self.Mini_button.clicked.connect(MainWindow.showMinimized)
        self.max_button.clicked.connect(self.F)
        self.quit_button.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def F(self):
        if self.f:
            self.MainWindow.showFullScreen()
            self.f = not self.f
        else:
            self.MainWindow.showNormal()
            self.f = not self.f

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setStatusTip(_translate("MainWindow", "就绪"))
        self.label_2.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p><img src=\":/logo/sources/logo2.png\"/></p></body></html>"
            ))
        self.label.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\">青空文庫読取り</p></body></html>"
            ))
        self.label_3.setText(
            _translate(
                "MainWindow",
                "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">AOZORABUNNKO</span></p></body></html>"
            ))
        self.treeWidget.setWhatsThis(
            _translate("MainWindow",
                       "<html><head/><body><p>ｗっくぇ</p></body></html>"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "排序"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.setSortingEnabled(__sortingEnabled)
        self.button_read.setText(_translate("MainWindow", "读取"))
        self.button_seek.setText(_translate("MainWindow", "搜索（不想写了）"))
        self.button_mainPage.setText(_translate("MainWindow", "主页"))
        self.button_lastPage.setText(_translate("MainWindow", "上一页"))
        self.button_nextPage.setText(_translate("MainWindow", "下一页"))


import soucers_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
