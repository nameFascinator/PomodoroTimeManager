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
        self.setWindowTitle("Tomate")  # windows Title

        self.hacken = ""
        self.ui.labe_hackenl.setText(self.hacken)  # hacken ✔
        self.ui.labe_hackenl.setStyleSheet("background-color: rgb(0, 0, 0); color: #AAFF00; font-size: 55px; "
                                           "font-weight: bold;")
        self.worked_time = 0  # how many times worked
        self.pause_time = False  # pause or not

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

        # Timer 0 0 0
        self.milliseconds = 0
        self.seconds = 0
        self.minutes = 0
        ###################################################################################

        self.counting = False

        # button ##########################################################################
        self.ui.start_button.clicked.connect(self.start_timer)  # button start
        self.ui.pause_button.clicked.connect(self.pause_timer)  # button pause count
        self.ui.reset_button.clicked.connect(self.refresh)  # refresh count
        ###################################################################################

        # user input ######################################################################
        self.input_work_interval = int(25)
        self.input_small_pause_interval = int(5)
        self.input_big_pause_interval = int(30)
        ###################################################################################
        self.copy_old_time_difference = 0
        self.was_paused = False

    def worked_intervals(self):  # pause or work
        try:
            self.input_work_interval = int(self.ui.lineEdit_input_work_interval.text())
        except:
            pass

        try:
            self.input_small_pause_interval = int(self.ui.lineEdit_input_small_pause_interval.text())
        except:
            pass

        try:
            self.input_big_pause_interval = int(self.ui.lineEd_input_big_pause_interval.text())
        except:
            pass

        if self.pause_time == False:
            if self.worked_time < 4:
                if self.minutes == self.input_work_interval:
                    self.hacken = self.hacken + " ✔"
                    self.ui.labe_hackenl.setText(self.hacken)
                    self.worked_time = self.worked_time + 1
                    self.pause_time = True
                    self.ui.labe_hackenl.setText(self.hacken)
                    self.ui.label_color_left.setStyleSheet("background-color: rgb(240, 182, 34);")
                    self.ui.label_color_right.setStyleSheet("background-color: rgb(240, 182, 34);")
                    self.ui.label_Work_Rest.setStyleSheet("background-color: rgb(240, 182, 34);")
                    self.ui.label_Work_Rest.setText("Relax!!!")

                    self.counting = False
                    self.milliseconds = 0
                    self.seconds = 0
                    self.minutes = 0
                    self.ui.label_timer.setText(f" 0{self.minutes}:0{self.seconds}:0{self.milliseconds}")
                    self.counting = True
                    if self.worked_time < 4:
                        self.start_timer_position = datetime.datetime.now() + datetime.timedelta(
                            minutes=self.input_small_pause_interval)
                        winsound.PlaySound(".//files//Alert and Small Pause.wav", winsound.SND_ASYNC)
                    else:
                        self.start_timer_position = datetime.datetime.now() + datetime.timedelta(
                            minutes=self.input_big_pause_interval)
                        winsound.PlaySound(".//files//Alert and Big Pause.wav", winsound.SND_ASYNC)

        elif self.pause_time == True:
            if self.worked_time < 4:
                if self.minutes == self.input_small_pause_interval:
                    self.start_timer_position = datetime.datetime.now() + datetime.timedelta(
                        minutes=self.input_work_interval)
                    self.pause_time = False
                    self.ui.label_color_left.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.ui.label_color_right.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.ui.label_Work_Rest.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.ui.label_Work_Rest.setText("Work!!!")
                    self.counting = False
                    self.milliseconds = 0
                    self.seconds = 0
                    self.minutes = 0
                    self.ui.label_timer.setText(f" 0{self.minutes}:0{self.seconds}:0{self.milliseconds}")
                    self.counting = True
            elif self.worked_time == 4:
                if self.minutes == self.input_big_pause_interval:
                    self.start_timer_position = datetime.datetime.now() + datetime.timedelta(
                        minutes=self.input_work_interval)
                    self.worked_time = 0
                    self.milliseconds = 0
                    self.seconds = 0
                    self.minutes = 0
                    self.hacken = ""
                    self.pause_time = False
                    self.counting = False

                    self.ui.labe_hackenl.setText(self.hacken)  # refresh ✔
                    self.ui.labe_hackenl.setStyleSheet(
                        "background-color: rgb(0, 0, 0); color: #AAFF00; font-size: 55px; font-weight: bold;")

                    self.ui.label_color_left.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.ui.label_color_right.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.ui.label_Work_Rest.setStyleSheet("background-color: rgb(0, 170, 0);")
                    self.ui.label_Work_Rest.setText("Work!!!")

                    self.ui.label_timer.setText(f" 0{self.minutes}:0{self.seconds}:0{self.milliseconds}")
                    self.counting = True
