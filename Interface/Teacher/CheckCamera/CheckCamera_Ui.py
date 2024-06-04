from PyQt6 import QtCore, QtGui, QtWidgets



class Ui_CheckCamera(object):
    def setupUi(self, CheckCamera):
        CheckCamera.setObjectName("CheckCamera")
        CheckCamera.resize(1272, 680)
        CheckCamera.setStyleSheet("#CheckCamera{\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"#Header {\n"
"    background-color: rgb(165, 213, 255);\n"
"}\n"
"\n"
"#Header #Logo{\n"
"    image: url(:/Pic/logo.png);\n"
"    border: none;\n"
"}\n"
"\n"
"#Header #NameSW{\n"
"    font-family: \"Robotol\", sans-serif;\n"
"    font-size: 25px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#result_frame {\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid black;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"\n"
"#btn_frame {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"#btn_frame QPushButton{\n"
"    background-color: #a5d5ff;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#btn_frame QPushButton:hover{\n"
"    background-color: rgb(3, 105, 161); /* Màu nền mới khi hover */\n"
"    border-color: rgb(65, 173, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(parent=CheckCamera)
        self.centralwidget.setObjectName("centralwidget")
        self.Header = QtWidgets.QFrame(parent=self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(0, 0, 1281, 71))
        self.Header.setStyleSheet("")
        self.Header.setObjectName("Header")
        self.NameSW = QtWidgets.QLabel(parent=self.Header)
        self.NameSW.setGeometry(QtCore.QRect(30, 20, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Robotol")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.NameSW.setFont(font)
        self.NameSW.setStyleSheet("")
        self.NameSW.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.NameSW.setObjectName("NameSW")
        self.label_class = QtWidgets.QLabel(parent=self.Header)
        self.label_class.setGeometry(QtCore.QRect(680, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Robotol")
        font.setBold(True)
        font.setWeight(75)
        self.label_class.setFont(font)
        self.label_class.setStyleSheet("")
        self.label_class.setText("")
        self.label_class.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_class.setObjectName("label_class")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 70, 1281, 631))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.btn_frame = QtWidgets.QFrame(parent=self.widget)
        self.btn_frame.setGeometry(QtCore.QRect(30, 20, 1211, 550))
        self.btn_frame.setStyleSheet("")
        self.btn_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.btn_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.btn_frame.setObjectName("btn_frame")
        self.showcam_btn = QtWidgets.QPushButton(parent=self.btn_frame)
        self.showcam_btn.setGeometry(QtCore.QRect(40, 20, 111, 41))
        self.showcam_btn.setStyleSheet("")
        self.showcam_btn.setObjectName("showcam_btn")
        self.line = QtWidgets.QLabel(parent=self.btn_frame)
        self.line.setGeometry(QtCore.QRect(0, 80, 1211, 1))  # Đặt vị trí và kích thước của đường thẳng
        self.line.setStyleSheet("background-color: black;")  # Đặt màu nền của đường thẳng

        CheckCamera.setCentralWidget(self.centralwidget)

        self.retranslateUi(CheckCamera)
        QtCore.QMetaObject.connectSlotsByName(CheckCamera)
        # StudentManagement.resizeEvent = self.on_window_resized

    def retranslateUi(self, CheckCamera):
        _translate = QtCore.QCoreApplication.translate
        CheckCamera.setWindowTitle(_translate("CheckCamera", "MainWindow"))
        self.NameSW.setText(_translate("CheckCamera", "STUDENT CAMERA"))
        self.showcam_btn.setText(_translate("CheckCamera", "Show Camera"))

        self.showcam_btn.clicked.connect(self.showcam)
        
    def showcam(self):
        print(1)
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CheckCamera = QtWidgets.QMainWindow()
    ui = Ui_CheckCamera()
    ui.setupUi(CheckCamera)
    CheckCamera.show()
    sys.exit(app.exec())