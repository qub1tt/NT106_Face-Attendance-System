# Form implementation generated from reading ui file '.\test.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_ChangePass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 486)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 10, 401, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, -80, 400, 581))
        self.label.setStyleSheet("background-color:rgb(165,213,255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 20, 340, 39))
        font = QtGui.QFont()
        font.setFamily("Imprint MT Shadow")
        font.setPointSize(20)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:black;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.btnLogin = QtWidgets.QPushButton(parent=self.widget)
        self.btnLogin.setGeometry(QtCore.QRect(30, 280, 360, 60))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("QPushButton#btnLogin{\n"
"    background-color:qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1,y2:0.477, stop:0 rgba(11,131,120,219), stop:1 rgba(85,98,112,226));\n"
"   color:rgba(255,255,255,210);\n"
"border-radius:10px;\n"
"}    \n"
"QPushButton#btnLogin:hover{\n"
"    background-color:qlineargradient(spread:pad,x1:0, y1:0.505682, x2:1,y2:0.477, stop:0 rgba(150,123,111,219), stop:1 rgba(85,81,84,226));\n"
"  \n"
"}    \n"
"\n"
"QPushButton#btnLogin:pressed{\n"
"    padding-left:5px;\n"
"padding-top:5px;\n"
"background-color:rgba(150,123,111,255);\n"
"\n"
"}    \n"
"\n"
"")
        self.btnLogin.setObjectName("btnLogin")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(20, 270, 360, 50))
        self.label_8.setStyleSheet("background-color:white;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(30, 130, 50, 50))
        self.label_10.setStyleSheet("background-color:rgb(76,198,198)")
        self.label_10.setLineWidth(1)
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_10.setPixmap(QtGui.QPixmap("Interface\Png\Icon\changepassword2.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(False)
        self.label_10.setOpenExternalLinks(False)
        self.label_10.setObjectName("label_10")
        self.leUser_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.leUser_2.setGeometry(QtCore.QRect(80, 130, 310, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leUser_2.setFont(font)
        self.leUser_2.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.leUser_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.leUser_2.setObjectName("leUser_2")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(20, 280, 360, 50))
        self.label_9.setStyleSheet("background-color:white;\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.label_9.raise_()
        self.label_8.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.btnLogin.raise_()
        self.label_10.raise_()
        self.leUser_2.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Change Your Password"))
        self.btnLogin.setText(_translate("MainWindow", "Change Password"))
        self.leUser_2.setPlaceholderText(_translate("MainWindow", "Enter your New-Password"))


