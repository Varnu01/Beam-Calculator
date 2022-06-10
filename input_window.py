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
        uic.loadUi("load_input.ui",self)
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
        self.support_location_unit.addItems(length_units)

    def setPage(self,mode):
        """Mode = 0 for load and 1 for supports"""
        if mode == 0:
            self.input_page.setCurrentIndex(0)
        elif mode == 1:
            self.input_page.setCurrentIndex(1)
    
    def inputConfig(self,type):
        """ set how the input page should look based on the input type """
        if type != 0:
            self.distribution_combo.setVisible(False)
            self.min_input.setVisible(False)
            self.max_input.setVisible(False)
            self.min_unit.setVisible(False)
            self.max_unit.setVisible(False)
            self.min_label.setVisible(False)
            self.max_label.setVisible(False)
            self.max_location_input.setVisible(False)
            self.min_location_input.setVisible(False)
            self.max_location_unit.setVisible(False)
            self.min_location_unit.setVisible(False)
            self.max_location_label.setVisible(False)
            self.min_location_label.setVisible(False)

            self.location_input.setVisible(True)
            self.location_unit.setVisible(True)
            self.location_label.setVisible(True)

        elif type == 0:
            self.distribution_combo.setVisible(True)
            self.min_input.setVisible(True)
            self.max_input.setVisible(True)
            self.min_unit.setVisible(True)
            self.max_unit.setVisible(True)
            self.min_label.setVisible(True)
            self.max_label.setVisible(True)
            
            self.max_location_input.setVisible(True)
            self.min_location_input.setVisible(True)
            self.max_location_unit.setVisible(True)
            self.min_location_unit.setVisible(True)
            self.max_location_label.setVisible(True)
            self.min_location_label.setVisible(True)

            self.location_input.setVisible(False)
            self.location_unit.setVisible(False)
            self.location_label.setVisible(False)
    
    def process_input(self,mode, mode_config):
        """Mode = 0 for load and 1 for supports, Mode_config = 0 for dist load, 1 for rest"""
        if mode == 0:
            self.quantity = float(self.quantity_input.text()) 
            self.quant_unit = force_unit_values[self.quantity_unit.currentIndex()]
            if mode_config == 0:
                self.dist_profile = distribution_profile[self.distribution_combo.currentIndex()]
                # self.min = <>
                # self.max = <>
                # self.min_unit 
            


    

    
        

# app = QtWidgets.QApplication(sys.argv)
# window = MainWindow()
# app.exec_()