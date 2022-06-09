# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PyQt5 import QtWidgets, uic

force_units = ['N', 'KN', 'MN']
force_unit_values = [1,10**3, 10**6]
stress_units  = ['Pa', 'KPa', 'Mpa', 'GPa']
stress_units_values = [1,10**3,10**6,10**9]
length_units  = ['m', 'mm', 'cm']
length_units_values = [1, 10**-3, 10**-2] 
distribution_profile = ['rectangular', 'triangle/trapezoidal']
direction = ['upwards', 'downwards']

class MainWindow(QtWidgets.QWidget):
    def __init__(self,parent_widget):
        super(MainWindow, self).__init__()

        self.parent_widget = parent_widget 
        uic.loadUi("load_input.ui",self.parent_widget)
        self.parent_widget.layout().addWidget(self)

        """ my many attempts at loading the widget into the parent"""
        # ui_path = os.path.join(os.path.dirname(__file__), "load_input.ui")
        # self.form = uic.loadUi(ui_path,parent_widget)
        # uic.loadUi("load_input.ui",self)
        # parent_widget.layout().addWidget(self)

        self.quantity_unit.addItems(force_units)
        self.distribution_combo.addItems(distribution_profile)
        self.direction_input.addItems(direction)
        self.location_unit.addItems(length_units)
        self.min_unit.addItems(force_units)
        self.max_unit.addItems(force_units)
        self.min_location_unit.addItems(length_units)
        self.max_location_unit.addItems(length_units)
    
    def setPage(self,mode):
        """Mode = 0 for load and 1 for supports"""
        if mode == 0:
            self.input_page.setCurrentIndex(0)
        elif mode == 1:
            self.input_page.setCurrentIndex(1)    

# app = QtWidgets.QApplication(sys.argv)
# window = MainWindow()
# app.exec_()