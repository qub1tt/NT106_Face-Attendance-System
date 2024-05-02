from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QScrollArea, QVBoxLayout


class Ui_StudentManagement(object):
    def setupUi(self, StudentManagement):
        StudentManagement.setObjectName("StudentManagement")
        StudentManagement.resize(1272, 680)
        StudentManagement.setStyleSheet("#StudentManagement{\n"
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
        self.centralwidget = QtWidgets.QWidget(parent=StudentManagement)
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
        self.class_btn = QtWidgets.QPushButton(parent=self.btn_frame)
        self.class_btn.setGeometry(QtCore.QRect(40, 20, 111, 41))
        self.class_btn.setStyleSheet("")
        self.class_btn.setObjectName("class_btn")
        self.line = QtWidgets.QLabel(parent=self.btn_frame)
        self.line.setGeometry(QtCore.QRect(0, 80, 1211, 1))
        self.line.setStyleSheet("background-color: black;") 
        
        
        # Thêm sau phần khởi tạo của btn_frame
        self.scrollArea = QScrollArea(self.btn_frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 90, 1211, 460))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget() 
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea.setStyleSheet("background-color: white; border: 1px solid black;")

        # Tạo layout cho QScrollArea
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)

        # Thêm các QWidget vào QScrollArea
        for _ in range(5):  # Thêm 5 hàng
            hbox = QtWidgets.QHBoxLayout()  # Sử dụng QHBoxLayout để xếp các QWidget theo hàng ngang
            hbox.setSpacing(0)
            for _ in range(3):  # Mỗi hàng có 3 QWidget
                widget = QtWidgets.QWidget()
                widget.setFixedWidth(385)  # Đặt chiều rộng tối thiểu là 400px
                widget.setFixedHeight(230) 
                widget.setStyleSheet("border: 1px solid black; border-radius: 10px; margin-top: 10px;")  # Thêm border
                hbox.addWidget(widget)
            self.verticalLayout.addLayout(hbox)

        # Đặt kích thước của QScrollArea nếu nội dung vượt quá kích thước btn_frame
        self.scrollArea.setMinimumSize(1211, 460)

        StudentManagement.setCentralWidget(self.centralwidget)

        self.retranslateUi(StudentManagement)
        QtCore.QMetaObject.connectSlotsByName(StudentManagement)
        # StudentManagement.resizeEvent = self.on_window_resized

    def retranslateUi(self, StudentManagement):
        _translate = QtCore.QCoreApplication.translate
        StudentManagement.setWindowTitle(_translate("StudentManagement", "MainWindow"))
        self.NameSW.setText(_translate("StudentManagement", "STUDENT CAMERA"))
        self.class_btn.setText(_translate("StudentManagement", "Show Camera"))

    #     self.class_btn.clicked.connect(self.show_cam)
        
    # def show_cam(self):
        # Create an instance of Ui_TestMainWindow
        # test_ui = Ui_StudentManagement()
        # test_ui2 = Ui_Attendance()
        # # Create a QMainWindow to hold the UI
        # test_window = QMainWindow()
        # test_window2 = QMainWindow()
        # # Setup the UI inside the QMainWindow
        # test_ui.setupUi(test_window)
        # test_ui2.setupUi(test_window2)
        # # Add the QMainWindow to the QStackWidget
        # self.main_content.insertWidget(1, test_window)
        # self.main_content.insertWidget(2, test_window2)  
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentManagement = QtWidgets.QMainWindow()
    ui = Ui_StudentManagement()
    ui.setupUi(StudentManagement)
    StudentManagement.show()
    sys.exit(app.exec())