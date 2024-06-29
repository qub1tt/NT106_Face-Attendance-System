# Form implementation generated from reading ui file 'login-ui.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
from PyQt6 import QtCore, QtGui, QtWidgets
import bcrypt
import os




from firebase_admin import db

import firebase_init




ref_admin = db.reference("Admin")
admin_password_hash = ref_admin.child("Password").get().encode("utf-8")

ref_students = db.reference("Students")


class Ui_Login(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 498)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-3, 0, 800, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(-40, 0, 421, 501))
        self.label.setStyleSheet("background-color:rgb(248, 248, 248);\n"
"border-radius: 20px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.lbl_backimg = QtWidgets.QLabel(parent=self.widget)
        self.lbl_backimg.setGeometry(QtCore.QRect(-1, 0, 791, 500))
        self.lbl_backimg.setStyleSheet("background-color:rgb(165,213,255);")
        self.lbl_backimg.setText("")
        self.lbl_backimg.setObjectName("lbl_backimg")
        self.lbl_image = QtWidgets.QLabel(parent=self.widget)
        self.lbl_image.setGeometry(QtCore.QRect(310, 70, 531, 371))
        self.lbl_image.setStyleSheet("")
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap("Anh/login.png"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(60, 50, 250, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 25px;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(20, 110, 341, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 15px;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.leUser = QtWidgets.QLineEdit(parent=self.widget)
        self.leUser.setGeometry(QtCore.QRect(80, 180, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma,sans-serif")
        font.setPointSize(-1)
        self.leUser.setFont(font)
        self.leUser.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"background-color: transparent;\n"
"color:rgba(0,0,0,240);\n"
"font-family: \"Tahoma\", sans-serif;\n"
"font-size: 18px;\n"
"padding: 10px; ")
        self.leUser.setText("")
        self.leUser.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.leUser.setObjectName("leUser")
        self.btnLogin = QtWidgets.QPushButton(parent=self.widget)
        self.btnLogin.setGeometry(QtCore.QRect(40, 410, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("QPushButton#btnLogin{\n"
"        background-color: rgb(0, 119, 182);\n"
"border-radius: 20px;\n"
"font-size:22px;\n"
"color:rgb(255, 255, 255);\n"
"font-family: \"Tahoma\", sans-serif;\n"
"font-size: 22px;\n"
"font-weight:bold;\n"
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
"")
        self.btnLogin.setObjectName("btnLogin")
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 190, 31, 31))
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_4.setPixmap(QtGui.QPixmap("Anh/user_icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 180, 311, 51))
        self.label_6.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border: 2px solid rgb(122, 122, 122);\n"
"border-radius: 10px;\n"
"color:rgba(0,0,0,240);\n"
"background-color: rgb(255, 255, 255);\n"
"font-family: \"Tahoma\", sans-serif;\n"
"font-size: 18px;\n"
"padding: 10px; ")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lePassword = QtWidgets.QLineEdit(parent=self.widget)
        self.lePassword.setGeometry(QtCore.QRect(80, 260, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma,sans-serif")
        font.setPointSize(-1)
        self.lePassword.setFont(font)
        self.lePassword.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"color:rgba(0,0,0,240);\n"
"background-color: transparent;\n"
"font-family: \"Tahoma\", sans-serif;\n"
"font-size: 18px;\n"
"padding: 10px; ")
        self.lePassword.setFrame(True)
        self.lePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lePassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lePassword.setObjectName("lePassword")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(40, 260, 311, 51))
        self.label_7.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border: 2px solid rgb(122, 122, 122);\n"
"border-radius: 10px;\n"
"color:rgba(0,0,0,240);\n"
"background-color: rgb(255, 255, 255);\n"
"font-family: \"Tahoma\", sans-serif;\n"
"font-size: 18px;\n"
"padding: 10px; \n"
"background-color:white;\n"
"\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(50, 270, 31, 31))
        self.label_5.setStyleSheet("")
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_5.setPixmap(QtGui.QPixmap("Anh/password_icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.btnForgotPassword = QtWidgets.QPushButton(parent=self.widget)
        self.btnForgotPassword.setGeometry(QtCore.QRect(220, 370, 131, 23))
        self.btnForgotPassword.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 12px;\n"
"background-color: transparent;\n"
"font-weight: bold;\n"
"font-style: italic;")
        self.btnForgotPassword.setObjectName("btnForgotPassword")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget)
        self.pushButton.setGeometry(QtCore.QRect(40, 370, 131, 23))
        self.pushButton.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 12px;\n"
"background-color: transparent;\n"
"font-weight: bold;\n"
"font-style: italic;")
        self.pushButton.setObjectName("pushButton")
        self.lbleror = QtWidgets.QLabel(parent=self.widget)
        self.lbleror.setGeometry(QtCore.QRect(50, 336, 291, 20))
        self.lbleror.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 12px;\n"
"background-color: transparent;\n"
"font-weight: bold;")
        self.lbleror.setText("")
        self.lbleror.setObjectName("lbleror")
        self.lbl_backimg.raise_()
        self.label.raise_()
        self.lbl_image.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btnLogin.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.leUser.raise_()
        self.label_7.raise_()
        self.lePassword.raise_()
        self.label_5.raise_()
        self.btnForgotPassword.raise_()
        self.pushButton.raise_()
        self.lbleror.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
# dấu mật khẩu
    def togglePasswordVisibility(self):
        if self.lePassword.echoMode() == QtWidgets.QLineEdit.EchoMode.Normal:
                self.lePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        else:
                self.lePassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "WELCOME"))
        self.label_3.setText(_translate("MainWindow", "Welcome to Face Attendance System"))
        self.leUser.setPlaceholderText(_translate("MainWindow", "Enter your Username"))
        self.btnLogin.setText(_translate("MainWindow", "Sign in"))
        self.lePassword.setPlaceholderText(_translate("MainWindow", "Enter your Password"))
        self.btnForgotPassword.setText(_translate("MainWindow", "Forgot password ?"))
        self.pushButton.setText(_translate("MainWindow", "Change password ?"))
       
        self.btnLogin.clicked.connect(self.loginFunction)

    def loginFunction(self):
        user = self.leUser.text()
        password = self.lePassword.text()

        hashed_password = password.encode("utf-8")
        if len(user) == 0 or len(password) == 0:
            self.lbleror.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.lbleror.setText("Please input all fields")
            return
        
        self.lbleror.setText("")

        # Kiểm tra tài khoản Admin
        try:
            if user == ref_admin.child("Username").get():
                result = bcrypt.checkpw(hashed_password, admin_password_hash)
                if result:
                    print("Admin login successful!")
                    self.lbleror.setStyleSheet("color:rgb(0, 255, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                    self.lbleror.setText("Admin login successful!")
                    os.environ['USER_ID'] = user
                    # Thực hiện các hành động sau khi đăng nhập thành công (Admin)
                    subprocess.Popen(["python", r"Interface/Teacher/Dashboard/Dashboard_main.py"])
                    return
                else:
                    self.lbleror.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                    self.lbleror.setText("Incorrect password!")
                    return
        except Exception as e:
            print(e)

        # Kiểm tra tài khoản Student
        try:
            student_ref = ref_students.child(user)
            student_data = student_ref.get()
            if student_data:
                student_password_hash = student_data["Password"].encode("utf-8")
                result = bcrypt.checkpw(hashed_password, student_password_hash)
                if result:
                    self.lbleror.setStyleSheet("color:rgb(0, 255, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                    print("Student login successful!")
                    os.environ['USER_ID'] = user
                    # Thực hiện các hành động sau khi đăng nhập thành công (Student)
                    subprocess.Popen(["python", r"Interface/Students/Home/homepage.py"])
                    return
                else:
                    self.lbleror.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                    self.lbleror.setText("Incorrect password!")
                    return
            else:
                self.lbleror.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                self.lbleror.setText("User not found!")
        except Exception as e:
            print(e)
            self.lbleror.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.lbleror.setText("User not found!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
