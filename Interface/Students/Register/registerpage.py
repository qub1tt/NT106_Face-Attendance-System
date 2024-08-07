# Form implementation generated from reading ui file 'registerpage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QListWidget, QPushButton, QVBoxLayout, QMessageBox, QApplication, QWidget, QLabel, QFileDialog, QListWidgetItem, QDialog, QDialogButtonBox
from PyQt6.QtGui import QIcon
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 758)
        MainWindow.setWindowIcon(QIcon("Interface/Png/Icon/face-id.png"))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        qr = MainWindow.frameGeometry()
        cp = QtGui.QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        MainWindow.move(qr.topLeft())
        self.widget.setGeometry(QtCore.QRect(0, 0, 930, 761))
        self.widget.setStyleSheet("background-color: rgb(165,213,255);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(20, 20, 891, 721))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                    "border-radius: 20px;")
        self.widget_3.setObjectName("widget_3")
        self.txtEmail = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtEmail.setGeometry(QtCore.QRect(40, 500, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtEmail.setFont(font)
        self.txtEmail.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                    "border: 2px solid rgb(122, 122, 122);\n"
                                    "border-radius: 10px;\n"
                                    "color:rgba(0,0,0,240);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "font-family: \"Tahoma\", sans-serif;\n"
                                    "font-size: 18px;\n"
                                    "padding: 10px; ")
        self.txtEmail.setText("")
        self.txtEmail.setObjectName("txtEmail")
        self.txtFaculty = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtFaculty.setGeometry(QtCore.QRect(470, 300, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtFaculty.setFont(font)
        self.txtFaculty.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                      "border: 2px solid rgb(122, 122, 122);\n"
                                      "border-radius: 10px;\n"
                                      "color:rgba(0,0,0,240);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "font-family: \"Tahoma\", sans-serif;\n"
                                      "font-size: 18px;\n"
                                      "padding: 10px; ")
        self.txtFaculty.setText("")
        self.txtFaculty.setObjectName("txtFaculty")
        self.txtName = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtName.setGeometry(QtCore.QRect(40, 400, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtName.setFont(font)
        self.txtName.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                   "border: 2px solid rgb(122, 122, 122);\n"
                                   "border-radius: 10px;\n"
                                   "color:rgba(0,0,0,240);\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "font-family: \"Tahoma\", sans-serif;\n"
                                   "font-size: 18px;\n"
                                   "padding: 10px; ")
        self.txtName.setText("")
        self.txtName.setObjectName("txtName")
        self.txtMajor = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtMajor.setGeometry(QtCore.QRect(470, 400, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtMajor.setFont(font)
        self.txtMajor.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                    "border: 2px solid rgb(122, 122, 122);\n"
                                    "border-radius: 10px;\n"
                                    "color:rgba(0,0,0,240);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "font-family: \"Tahoma\", sans-serif;\n"
                                    "font-size: 18px;\n"
                                    "padding: 10px; ")
        self.txtMajor.setText("")
        self.txtMajor.setObjectName("txtMajor")
        self.txtStuID = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtStuID.setGeometry(QtCore.QRect(40, 300, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtStuID.setFont(font)
        self.txtStuID.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                    "border: 2px solid rgb(122, 122, 122);\n"
                                    "border-radius: 10px;\n"
                                    "color:rgba(0,0,0,240);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "font-family: \"Tahoma\", sans-serif;\n"
                                    "font-size: 18px;\n"
                                    "padding: 10px; ")
        self.txtStuID.setText("")
        self.txtStuID.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.txtStuID.setObjectName("txtStuID")
        self.lblUpAvatar = QtWidgets.QLabel(parent=self.widget_3)
        self.lblUpAvatar.setGeometry(QtCore.QRect(110, 190, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.lblUpAvatar.setFont(font)
        self.lblUpAvatar.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                       "font-size: 25px;\n"
                                       "font-weight: bold;\n"
                                       "background-color: transparent;")
        self.lblUpAvatar.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblUpAvatar.setObjectName("lblUpAvatar")
        self.widget_2 = QtWidgets.QWidget(parent=self.widget_3)
        self.widget_2.setGeometry(QtCore.QRect(150, 30, 171, 161))
        self.widget_2.setStyleSheet(
                                    "background-color: transparent;")
        self.widget_2.setObjectName("widget_2")
        self.btnUpAvatar = QtWidgets.QPushButton(parent=self.widget_2)
        self.btnUpAvatar.setGeometry(QtCore.QRect(0, 0, 171, 161))
        font = QtGui.QFont()
        font.setFamily("Social Media Circled")
        font.setPointSize(15)
        self.btnUpAvatar.setFont(font)
        self.btnUpAvatar.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/Png/Icon/UploadAvatar.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnUpAvatar.setIcon(icon)
        self.btnUpAvatar.setIconSize(QtCore.QSize(150, 150))
        self.btnUpAvatar.setObjectName("btnUpAvatar")
        self.txtYear = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtYear.setGeometry(QtCore.QRect(470, 500, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtYear.setFont(font)
        self.txtYear.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                   "border: 2px solid rgb(122, 122, 122);\n"
                                   "border-radius: 10px;\n"
                                   "color:rgba(0,0,0,240);\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "font-family: \"Tahoma\", sans-serif;\n"
                                   "font-size: 18px;\n"
                                   "padding: 10px; ")
        self.txtYear.setText("")
        self.txtYear.setObjectName("txtYear")
        self.btnRegister = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnRegister.setGeometry(QtCore.QRect(679, 640, 171, 60))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setStyleSheet("""
    QPushButton {
        background-color: rgb(0, 119, 182);
        border-radius: 20px;
        font-size: 20px;
        color: rgb(255, 255, 255);
        font-family: "Tahoma", sans-serif;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));
    }
    QPushButton:pressed {
        padding-left: 5px;
        padding-top: 5px;
        background-color: rgba(150, 123, 111, 255);
    }
""")
        self.btnRegister.setObjectName("btnRegister")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_14.setGeometry(QtCore.QRect(460, 30, 401, 201))
        self.label_14.setText("")
        self.label_14.setPixmap(QtGui.QPixmap("Interface/Png/Image/register.png"))
        self.label_14.setScaledContents(True)
        self.label_14.setObjectName("label_14")
        self.labelStuID = QtWidgets.QLabel(parent=self.widget_3)
        self.labelStuID.setGeometry(QtCore.QRect(40, 270, 111, 16))
        self.labelStuID.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                      "font-size: 18px;\n"
                                      "font-weight: bold;\n"
                                      "background-color: transparent;")
        self.labelStuID.setObjectName("labelStuID")
        self.labelName = QtWidgets.QLabel(parent=self.widget_3)
        self.labelName.setGeometry(QtCore.QRect(40, 370, 111, 16))
        self.labelName.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;\n"
                                     "background-color: transparent;")
        self.labelName.setObjectName("labelName")
        self.labelEmail = QtWidgets.QLabel(parent=self.widget_3)
        self.labelEmail.setGeometry(QtCore.QRect(40, 470, 111, 16))
        self.labelEmail.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                      "font-size: 18px;\n"
                                      "font-weight: bold;\n"
                                      "background-color: transparent;")
        self.labelEmail.setObjectName("labelEmail")
        self.labelFaculty = QtWidgets.QLabel(parent=self.widget_3)
        self.labelFaculty.setGeometry(QtCore.QRect(470, 270, 111, 16))
        self.labelFaculty.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                        "font-size: 18px;\n"
                                        "font-weight: bold;\n"
                                        "background-color: transparent;")
        self.labelFaculty.setObjectName("labelFaculty")
        self.labelMajor = QtWidgets.QLabel(parent=self.widget_3)
        self.labelMajor.setGeometry(QtCore.QRect(470, 370, 111, 16))
        self.labelMajor.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                      "font-size: 18px;\n"
                                      "font-weight: bold;\n"
                                      "background-color: transparent;")
        self.labelMajor.setObjectName("labelMajor")
        self.labelYear = QtWidgets.QLabel(parent=self.widget_3)
        self.labelYear.setGeometry(QtCore.QRect(470, 470, 111, 16))
        self.labelYear.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;\n"
                                     "background-color: transparent;")
        self.labelYear.setObjectName("labelYear")
        self.labelClass = QtWidgets.QLabel(parent=self.widget_3)
        self.labelClass.setGeometry(QtCore.QRect(40, 570, 111, 16))
        self.labelClass.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                      "font-size: 18px;\n"
                                      "font-weight: bold;\n"
                                      "background-color: transparent;")
        self.labelClass.setObjectName("labelClass")

        # Thêm QPushButton để mở dialog chọn lớp
        self.btnSelectClasses = QPushButton("", parent=self.widget_3)
        self.btnSelectClasses.setGeometry(QtCore.QRect(40, 600, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.btnSelectClasses.setFont(font)
        self.btnSelectClasses.setObjectName("btnSelectClasses")
        self.btnSelectClasses.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                     "font-size: 18px;\n"
                                     "font-weight: bold;\n"
                                     "background-color: transparent;")
        # QLineEdit để hiển thị các lớp đã chọn, đặt cùng vị trí với btnSelectClasses
        self.txtClass = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtClass.setGeometry(QtCore.QRect(40, 600, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtClass.setFont(font)
        self.txtClass.setStyleSheet("background-color:rgba(0,0,0,0);\n"
        "border: 2px solid rgb(122, 122, 122);\n"
        "border-radius: 10px;\n"
        "color:rgba(0,0,0,240);\n"
        "background-color: rgb(255, 255, 255);\n"
        "font-family: \"Tahoma\", sans-serif;\n"
        "font-size: 18px;\n"
        "padding: 10px; ")
        self.txtClass.setText("")
        self.txtClass.setObjectName("txtClass")

        # Đảm bảo btnSelectClasses nằm trên txtClass
        self.btnSelectClasses.raise_()

        self.labelError = QtWidgets.QLabel(parent=self.widget_3)
        self.labelError.setGeometry(QtCore.QRect(460, 570, 411, 61))
        self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "font-family: \"Tahoma\", sans-serif;\n"
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n"
                                      "qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n")
        self.labelError.setText("")
        self.labelError.setObjectName("labelError")
        self.btnBack = QPushButton("", parent=self.widget_3)
        self.btnBack.setGeometry(QtCore.QRect(40, 600, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.btnBack.setFont(font)
        self.btnBack.setFixedSize(60, 40)
        self.btnBack.setIcon(QtGui.QIcon("Interface/Png/Icon/back.png"))
        self.btnBack.setIconSize(QtCore.QSize(30, 30))
        self.btnBack.move(20, 20)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Thiết lập thứ tự tab
        MainWindow.setTabOrder(self.btnRegister, self.txtStuID)
        MainWindow.setTabOrder(self.txtStuID, self.txtName)
        MainWindow.setTabOrder(self.txtName, self.txtEmail)
        MainWindow.setTabOrder(self.txtEmail, self.btnSelectClasses)
        MainWindow.setTabOrder(self.btnSelectClasses, self.txtFaculty)
        MainWindow.setTabOrder(self.txtFaculty, self.txtMajor)
        MainWindow.setTabOrder(self.txtMajor, self.txtYear)
        MainWindow.setTabOrder(self.txtYear, self.btnRegister)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Register"))
        self.btnRegister.setText(_translate("MainWindow", "Register"))
        self.labelStuID.setText(_translate("MainWindow", "Student ID:"))
        self.labelName.setText(_translate("MainWindow", "Name:"))
        self.labelEmail.setText(_translate("MainWindow", "Email:"))
        self.labelFaculty.setText(_translate("MainWindow", "Faculty:"))
        self.labelMajor.setText(_translate("MainWindow", "Major:"))
        self.labelYear.setText(_translate("MainWindow", "Year:"))
        self.labelClass.setText(_translate("MainWindow", "Class:"))
        self.txtEmail.setPlaceholderText(_translate("MainWindow", "Enter your Email"))
        self.txtFaculty.setPlaceholderText(_translate("MainWindow", "Enter your Faculty"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "Enter your Name"))
        self.txtMajor.setPlaceholderText(_translate("MainWindow", "Enter your Major"))
        self.txtStuID.setPlaceholderText(_translate("MainWindow", "Enter your Student ID"))
        self.lblUpAvatar.setText(_translate("MainWindow", "Upload your avatar"))
        self.txtYear.setPlaceholderText(_translate("MainWindow", "Enter your Year"))
        self.txtClass.setPlaceholderText(_translate("MainWindow", "Enter your Class")) 

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
