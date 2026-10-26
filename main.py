#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from main_window import Ui_Form


class Win(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()

        self.setupUi(self)

        self.setWindowTitle("工作表检查器_V1.0")

        self.resize(1600, 1000)

        self.init_ui()



    def init_ui(self):

        self.btn_start.clicked.connect(self.func_start)

        self.te_input1.setPlaceholderText("请输入导出的工作表名称")
        self.te_input2.setPlaceholderText("请输入用于检查的工作表名称")

    def func_start(self):

        print(self.te_input1.toPlainText())
        print(self.te_input2.toPlainText())

        origin_names = self.te_input1.toPlainText().split("\n")
        check_names = self.te_input2.toPlainText().split("\n")

        self.check_names(origin_names, check_names)

    def check_names(self, origin_names, check_names):

        res = []
        for cname in check_names:
            if cname not in origin_names:
                res.append(cname)

        if res:
            print("res:\t", res)
            self.te_output.clear()
            self.te_output.appendPlainText(f"没有找到的：\n{'\n'.join(res)}")
        else:
            self.te_output.clear()
            QMessageBox.information(self, "提示", "正确")







if __name__ == '__main__':

    app = QApplication(sys.argv)

    win = Win()
    win.show()

    sys.exit(app.exec_())