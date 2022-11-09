from PyQt6 import QtWidgets, QtGui
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
import winsound
import datetime

from UI import Ui_MainWindow

class Tomate(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Tomate")                           # windows Title

        self.hacken = ""
        self.ui.labe_hackenl.setText(self.hacken)               # hacken ✔
        self.ui.labe_hackenl.setStyleSheet("background-color: rgb(0, 0, 0); color: #AAFF00; font-size: 55px; "
                                           "font-weight: bold;")
        self.worked_time = 0                                    # how many times worked
        self.pause_time = False      # pause or not

        # color waiting or pause
        self.ui.label_color_left.setStyleSheet("background-color: rgb(255, 170, 170);")
        self.ui.label_color_right.setStyleSheet("background-color: rgb(255, 170, 170);")
        self.ui.label_Work_Rest.setStyleSheet("background-color: rgb(255, 170, 170);")
        self.ui.label_Work_Rest.setText("Waiting...")
        ###################################################################################

        # how many minutes #################################################
        self.timer_3 = QTimer()
        self.timer_3.setInterval(5000)
        self.timer_3.timeout.connect(self.worked_intervals)
        self.timer_3.start()
        ###################################################################################

        # data and time ########################
        self.timer_2 = QTimer()
        self.timer_2.setInterval(1000)
        self.timer_2.timeout.connect(self.date)
        self.timer_2.start()
        ###################################################################################