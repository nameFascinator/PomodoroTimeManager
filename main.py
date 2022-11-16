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

    def date(self):
        today = datetime.datetime.now()  # time now
        form = today.strftime("%d.%m.%Y // %H:%M:%S")  # EU time format
        self.ui.label_date_now.setText(f"Today is: {form}")  # show data and time

    def start_timer(self):  # начинамем отсчет
        self.pause_time = False
        if self.was_paused == False:
            self.start_timer_position = datetime.datetime.now() + datetime.timedelta(minutes=self.input_work_interval,
                                                                                     seconds=0)
        else:
            self.start_timer_position = datetime.datetime.now() + datetime.timedelta(minutes=self.input_work_interval,
                                                                                     seconds=-self.copy_old_time_difference)

        self.time_difference = (self.input_work_interval * 60) - (
                self.start_timer_position - datetime.datetime.now()).total_seconds()
        self.ui.label_Work_Rest.setText("Work")
        self.ui.label_color_left.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.ui.label_color_right.setStyleSheet("background-color: rgb(0, 170, 0);")
        self.ui.label_Work_Rest.setStyleSheet("background-color: rgb(0, 170, 0);")

        self.counting = True  # start count True

        if self.counting == True:
            self.timer = QTimer()  # create object QTimer
            self.timer.setInterval(10)  # Set the interval with which the program will call the recurring timer
            # function responsible for counting the timer.
            self.timer.timeout.connect(self.recurring_timer)
            self.timer.start()  # start Qtimer object
        else:
            self.timer.stop()  # stop Qtimer object if counting False

        self.was_paused = False

    def pause_timer(self):  # stop counting, put on stop
        self.was_paused = True
        self.copy_old_time_difference = int(self.minutes * 60) + int(self.seconds)

        if self.counting == False:
            pass
        else:
            self.ui.label_color_left.setStyleSheet("background-color: rgb(255, 170, 170);")
            self.ui.label_color_right.setStyleSheet("background-color: rgb(255, 170, 170);")
            self.ui.label_Work_Rest.setStyleSheet("background-color: rgb(255, 170, 170);")
            self.ui.label_Work_Rest.setText("Waiting...")
            self.timer.stop()

    def recurring_timer(self):  # start_time
        if self.minutes == 0 and self.seconds == 0 and self.milliseconds == 0 and self.pause_time == False and self.worked_time < 4:
            winsound.PlaySound(".//files//Alert and Work.wav", winsound.SND_ASYNC)

        self.minutes = str(int(self.time_difference / 60))
        self.seconds = str(int(self.time_difference % 60))
        self.milliseconds = str(
            int((round(self.time_difference % 60, 4) - int(round(self.time_difference % 60, 4))) * 100))

        if len(self.milliseconds) == 1:
            self.milliseconds = "0" + self.milliseconds

        if len(self.seconds) == 1:
            self.seconds = "0" + self.seconds

        if len(self.minutes) == 1:
            self.minutes = "0" + self.minutes

        self.ui.label_timer.setText(f" {self.minutes}:{self.seconds}:{self.milliseconds}")

        if self.milliseconds[0] == "0":
            self.milliseconds = int(self.milliseconds[1])
        else:
            self.milliseconds = int(self.milliseconds)

        if self.seconds[0] == "0":
            self.seconds = int(self.seconds[1])
        else:
            self.seconds = int(self.seconds)

        if self.minutes[0] == "0":
            self.minutes = int(self.minutes[1])
        else:
            self.minutes = int(self.minutes)

        self.minutes = int(self.time_difference / 60)
        self.seconds = int(self.time_difference % 60)
        self.milliseconds = int((round(self.time_difference % 60, 4) - int(round(self.time_difference % 60, 4))) * 100)

        if self.pause_time == False and self.worked_time < 4:
            self.time_difference = (self.input_work_interval * 60) - (
                        self.start_timer_position - datetime.datetime.now()).total_seconds()
            self.convert_to_procent = (self.minutes * 60 + self.seconds) / (int(self.input_work_interval) * 60 / 100)
            self.ui.progressBar.setProperty("value", self.convert_to_procent)

        if self.pause_time == True and self.worked_time < 4:
            self.time_difference = (self.input_small_pause_interval * 60) - (
                        self.start_timer_position - datetime.datetime.now()).total_seconds()
            self.convert_to_procent = (self.minutes * 60 + self.seconds) / (self.input_small_pause_interval * 60 / 100)
            self.ui.progressBar.setProperty("value", self.convert_to_procent)

        if self.pause_time == True and self.worked_time == 4:
            self.time_difference = (self.input_big_pause_interval * 60) - (
                        self.start_timer_position - datetime.datetime.now()).total_seconds()
            self.convert_to_procent = (self.minutes * 60 + self.seconds) / (self.input_big_pause_interval * 60 / 100)
            self.ui.progressBar.setProperty("value", self.convert_to_procent)
