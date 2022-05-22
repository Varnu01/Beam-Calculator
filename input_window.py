# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PyQt5 import QtWidgets, uic

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self,parent_widget):
        super(MainWindow, self).__init__()
        uic.loadUi("load_input.ui",self)
        self.parent_widget = parent_widget
        self.parent_widget.layout().addWidget(self)
        self.show()

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()