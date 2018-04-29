#!/url/bin/python3
# -*- coding:utf-8 -*-

import queue
import re
import sys

import requests
from bs4 import BeautifulSoup as bs
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidgetItemIterator

from getDatas import (get_kanasakuhinn, get_kanasakusya, get_sakuhinnCa,
                      get_sakusyaCa)
from textState import TextState
from Ui_AozoraReader import Ui_MainWindow

t_url = queue.Queue(1)  # 获取文章用的url
t_text = queue.Queue(1)  # 该显示的文章


def get_work(url):
    # 获取文章
    q = 'card' + url.split('card')[-1]
    reg_work_homepage = requests.get(url)
    soup_work_homepage = bs(reg_work_homepage.content.decode("utf-8"), 'lxml')
    links = soup_work_homepage.findAll(
        name='a', attrs={"href": re.compile(r'^./files/')})[-1]['href']
    link = url.replace(q, '') + links[2:]
    return link


class readTextThread(QtCore.QThread):
    # 多开进程处理文章读取，先要把网址获取了才能新建此进程
    trigger = QtCore.pyqtSignal()

    def __int__(self):
        super(readTextThread, self).__init__()

    def run(self):
        try:
            url = get_work(t_url.get())
            reg = requests.get(url)
            reg.encoding = "Shift_JIS"
            t_text.put(reg.text)
        except Exception as e:
            t_text.put("读取错误：" + str(e))
        finally:
            self.trigger.emit()


class Aozora(QMainWindow):
    def __init__(self, parent=None):

        super(Aozora, self).__init__(parent)
        self.initUI = Ui_MainWindow()
        self.initUI.setupUi(self)
        #self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        item_0 = self.initUI.item_0
        D = get_sakusyaCa()
        _translate = QtCore.QCoreApplication.translate
        for i, o in zip(D, range(len(D))):
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            self.initUI.treeWidget.topLevelItem(0).child(o).setText(
                0, _translate("MainWindow", D[o]))
            B = get_kanasakusya(D[o])
            for j, k in zip(B, range(len(B))):
                item_2 = QtWidgets.QTreeWidgetItem(item_1)
                self.initUI.treeWidget.topLevelItem(0).child(o).child(
                    k).setText(0, _translate("MainWindow", B[k][2]))
        item_0 = QtWidgets.QTreeWidgetItem(self.initUI.treeWidget)

        C = get_sakuhinnCa()
        for i, o in zip(C, range(len(C))):
            item_1 = QtWidgets.QTreeWidgetItem(item_0)
            self.initUI.treeWidget.topLevelItem(1).child(o).setText(
                0, _translate("MainWindow", C[o]))
            A = get_kanasakuhinn(C[o])
            for j, k in zip(A, range(len(A))):
                item_2 = QtWidgets.QTreeWidgetItem(item_1)
                self.initUI.treeWidget.topLevelItem(1).child(o).child(
                    k).setText(0, _translate("MainWindow", A[k][2]))
                if self.initUI.treeWidget.topLevelItem(1).child(o).child(
                        k).isSelected():
                    print(".....................")
        self.initUI.treeWidget.topLevelItem(0).setText(0,
                                                       _translate(
                                                           "MainWindow",
                                                           "作者序（不想写了）"))
        self.initUI.treeWidget.topLevelItem(1).setText(0,
                                                       _translate(
                                                           "MainWindow",
                                                           "作品序"))

        self.initUI.button_mainPage.clicked.connect(self.main_page)
        self.initUI.button_seek.clicked.connect(self.search)
        self.initUI.button_read.clicked.connect(self.l_view_tri)
        self.initUI.button_lastPage.clicked.connect(self.last_page)
        self.initUI.button_nextPage.clicked.connect(self.next_page)
        self.wenzhang = t_text
        self.T = readTextThread()  # 初始化显示第一篇文章
        self.textstate = TextState()
        self.init_text()

    def init_text(self):
        # 处理文章显示，它将获取网址，新建进程，成功后显示文章
        t_url.put(self.textstate.get_url())
        self.T = readTextThread()
        self.T.trigger.connect(self.show_wenzhang)
        self.T.start()

    def show_wenzhang(self):
        content = self.wenzhang.get()
        self.initUI.label_view.setText(content)

    def main_page(self):
        self.textstate.set_now(1)
        self.init_text()

    def next_page(self):
        self.textstate.next_text()
        self.init_text()

    def last_page(self):
        self.textstate.last_text()
        self.init_text()

    def l_view_tri(self):
        # 列表的点击函数，传入作品名字，传入self.textstate
        # self.textstate.get_l_item(tri)
        tri = self.item_selected()
        if tri is not None:
            self.textstate.get_l_item(tri)
            self.init_text()

    def search(self):
        pass
    
    def item_selected(self):
        item = QTreeWidgetItemIterator(self.initUI.treeWidget)
        # 该类的value()即为QTreeWidgetItem
        while item.value():
            # print(item.value())
            v = item.value()
            if v.isSelected() is True:
                # print(item.value().text(0))
                return item.value().text(0)
            item += 1


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Aozora()
    ex.show()
    sys.exit(app.exec_())
"""あいうえおかきくけこさしすせそたちつてとなにぬねのはひふへほまみむめもやゆよらりるれろわをん"""
