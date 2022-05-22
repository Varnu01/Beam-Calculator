# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PyQt5 import QtWidgets, uic
import math 
from math import pi
import input_window 

loads = ['Concentrated load', 'Torque', 'Distributed Load']
supports = ['Pin', 'Roller', 'Fixed']
force_units = ['N', 'KN', 'MN']
force_unit_values = [1,10**3, 10**6]
stress_units  = ['Pa', 'KPa', 'Mpa', 'GPa']
stress_units_values = [1,10**3,10**6,10**9]
beam_cross_section = ['Rectangle', 'Round', 'Round Hollow', 'I-beam', 'Custom']
length_units  = ['m', 'mm', 'cm']
length_units_values = [1, 10**-3, 10**-2] 

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("mainwindow.ui",self)
        self.show()
        self.supportwindow = input_window.MainWindow(self.<parentwindow>,self)
        
        self.E_unit_.addItems(stress_units)
        self.length_unit_.addItems(length_units)
        self.support_combo.addItems(supports)
        self.load_combo.addItems(loads)

        self.d1_unit.addItems(length_units)
        self.d2_unit.addItems(length_units)
        self.d3_unit.addItems(length_units)
        self.d4_unit.addItems(length_units)

        self.cross_section_combo.addItems(beam_cross_section)
        self.cross_section_combo.currentIndexChanged.connect(self.beam_dimensions_ui)


    def beam_dimensions_ui(self):
        if self.cross_section_combo.currentIndex() == 0:
            self.d1_label.setText('Height')
            self.d2_label.setText('Breadth')

            self.d2_label.setVisible(True)
            self.d2.setVisible(True)
            self.d2_unit.setVisible(True)

            self.d3_label.setVisible(False)
            self.d3.setVisible(False)
            self.d3_unit.setVisible(False)

            self.d4_label.setVisible(False)
            self.d4.setVisible(False)
            self.d4_unit.setVisible(False)
            
        
        elif self.cross_section_combo.currentIndex() == 1:
            self.d1_label.setText('Diameter')

            self.d2_label.setVisible(False)
            self.d2.setVisible(False)
            self.d2_unit.setVisible(False)

            self.d3_label.setVisible(False)
            self.d3.setVisible(False)
            self.d3_unit.setVisible(False)

            self.d4_label.setVisible(False)
            self.d4.setVisible(False)
            self.d4_unit.setVisible(False)

        elif self.cross_section_combo.currentIndex() == 2:
            self.d1_label.setText('Outside Diameter')
            self.d2_label.setText('Inside Diameter')
            
            self.d2_label.setVisible(True)
            self.d2.setVisible(True)
            self.d2_unit.setVisible(True)
            
            self.d3_label.setVisible(False)
            self.d3.setVisible(False)
            self.d3_unit.setVisible(False)

            self.d4_label.setVisible(False)
            self.d4.setVisible(False)
            self.d4_unit.setVisible(False)

        elif self.cross_section_combo.currentIndex() == 3:
            self.d1_label.setText('Web Height')
            self.d2_label.setText('Flange Height')
            self.d3_label.setText('Web Width')
            self.d4_label.setText('Flange Width')

            self.d2_label.setVisible(True)
            self.d2.setVisible(True)
            self.d2_unit.setVisible(True)
            
            self.d3_label.setVisible(True)
            self.d3.setVisible(True)
            self.d3_unit.setVisible(True)

            self.d4_label.setVisible(True)
            self.d4.setVisible(True)
            self.d4_unit.setVisible(True)
        
        elif self.cross_section_combo.currentIndex() == 4:
            self.d1_label.setText('Moment of Inertia (mm^4)')
            self.d1_unit.setVisible(False)

            self.d2_label.setVisible(False)
            self.d2.setVisible(False)
            self.d2_unit.setVisible(False)

            self.d3_label.setVisible(False)
            self.d3.setVisible(False)
            self.d3_unit.setVisible(False)

            self.d4_label.setVisible(False)
            self.d4.setVisible(False)
            self.d4_unit.setVisible(False)

            

    def process_inputs(self):
        self.E_unit = stress_units_values[self.E_unit_.currentIndex()]
        self.E = (self.E_unit) * float(self.E_in.text())

        self.length_unit = length_units_values[self.length_unit_.currentIndex()]
        self.beam_length = self.length_unit * float(self.beam_length_in.text())

        if self.cross_section_combo.currentIndex() == 0:
            self.d1_unit_ = length_units_values[self.d1_unit.currentIndex()]
            self.d2_unit_ = length_units_values[self.d2_unit.currentIndex()]
            self.d1 = self.d1_unit_ * float(self.d1.text())
            self.d2 = self.d1_unit_ * float(self.d2.text())
            self.inertia = (self.d1*(self.d2**3)/12)

        elif self.cross_section_combo.currentIndex() == 1:
            self.d1_unit_ = length_units_values[self.d1_unit.currentIndex()]
            self.d1 = self.d1_unit_ *  float(self.d1.text())
            self.inertia = (pi*(self.d1**4))/64

        elif self.cross_section_combo.currentIndex() == 2:
            self.d1_unit_ = length_units_values[self.d1_unit.currentIndex()]
            self.d2_unit_ = length_units_values[self.d2_unit.currentIndex()]
            self.d1 = self.d1_unit_ * float(self.d1.text())
            self.d2 = self.d2_unit_ * float(self.d2.text())
            self.inertia = (pi/64) * (self.d1**4 - self.d2**4)

        elif self.cross_section_combo.currentIndex() == 3:
            self.d1_unit_ = length_units_values[self.d1_unit.currentIndex()]
            self.d2_unit_ = length_units_values[self.d2_unit.currentIndex()]
            self.d3_unit_ = length_units_values[self.d3_unit.currentIndex()]
            self.d4_unit_ = length_units_values[self.d4_unit.currentIndex()]
            self.d1 = self.d1_unit_ * float(self.d1.text())
            self.d2 = self.d2_unit_ * float(self.d2.text())
            self.d3 = self.d3_unit_ * float(self.d3.text())
            self.d4 = self.d4_unit_ * float(self.d4.text())
            
            # Ixx = H3b/12 + 2[h3B/12 + hB(H+h)2/4]
            self.inertia = (((self.d1**3)*self.d3)/12) + 2*((((self.d2**3)*self.d4)/12)+ ((self.d2*self.d4)*((self.d1+self.d2)**2)/4))
            # self.d1_label.setText('Web Height')
            # self.d2_label.setText('Flange Height')
            # self.d3_label.setText('Web Width')
            # self.d4_label.setText('Flange Width')

app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
app.exec_()
        
    


