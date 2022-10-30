from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 1000)
        MainWindow.setStyleSheet("background-color: rgb(248, 245, 223)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 20, 960, 960))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred,
                                           QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_picture_tomat = QtWidgets.QLabel(self.frame)
        self.label_picture_tomat.setGeometry(QtCore.QRect(200, 160, 531, 611))
        self.label_picture_tomat.setText("")
        self.label_picture_tomat.setPixmap(QtGui.QPixmap(".//files//tomato.png"))
        self.label_picture_tomat.setScaledContents(True)
        self.label_picture_tomat.setObjectName("label_picture_tomat")
        self.layoutWidget = QtWidgets.QWidget(self.frame)
        self.layoutWidget.setGeometry(QtCore.QRect(130, 870, 721, 54))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.start_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.start_button.setFont(font)
        self.start_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.start_button.setMouseTracking(True)
        self.start_button.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.start_button.setCheckable(False)
        self.start_button.setObjectName("start_button")
        self.horizontalLayout.addWidget(self.start_button)
        self.labe_hackenl = QtWidgets.QLabel(self.layoutWidget)
        self.labe_hackenl.setMouseTracking(False)
        self.labe_hackenl.setAutoFillBackground(False)
        self.labe_hackenl.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.labe_hackenl.setObjectName("labe_hackenl")
        self.horizontalLayout.addWidget(self.labe_hackenl)
        self.reset_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.reset_button.setFont(font)
        self.reset_button.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.reset_button.setMouseTracking(True)
        self.reset_button.setStyleSheet("\n""background-color: rgb(255, 255, 255);")
        self.reset_button.setCheckable(False)
        self.reset_button.setObjectName("reset_button")
        self.horizontalLayout.addWidget(self.reset_button)
