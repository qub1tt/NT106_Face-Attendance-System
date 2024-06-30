# Form implementation generated from reading ui file 'changepassword.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import firebase_init

import bcrypt
import os
import re



from firebase_admin import db

class Ui_ChangePass(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 498)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-3, 0, 800, 500))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(380, 0, 421, 501))
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
        self.lbl_image.setGeometry(QtCore.QRect(-50, 0, 491, 491))
        self.lbl_image.setStyleSheet("")
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap("Interface/Png/Image/changepassword.png"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setWordWrap(False)
        self.lbl_image.setObjectName("lbl_image")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(450, 30, 281, 41))
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
        self.leUser = QtWidgets.QLineEdit(parent=self.widget)
        self.leUser.setGeometry(QtCore.QRect(480, 170, 261, 50))
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
        self.btnLogin.setGeometry(QtCore.QRect(440, 416, 301, 51))
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
        self.label_4.setGeometry(QtCore.QRect(450, 180, 31, 31))
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_4.setPixmap(QtGui.QPixmap("Interface/Png/Icon/user_icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(440, 170, 311, 51))
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
        self.lePassword.setGeometry(QtCore.QRect(480, 240, 261, 50))
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
        self.label_7.setGeometry(QtCore.QRect(440, 240, 311, 51))
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
        self.label_5.setGeometry(QtCore.QRect(450, 250, 31, 31))
        self.label_5.setStyleSheet("")
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_5.setPixmap(QtGui.QPixmap("Interface/Png/Icon/password_icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.lbleror = QtWidgets.QLabel(parent=self.widget)
        self.lbleror.setGeometry(QtCore.QRect(50, 336, 291, 20))
        self.lbleror.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 12px;\n"
"background-color: transparent;\n"
"font-weight: bold;")
        self.lbleror.setText("")
        self.lbleror.setObjectName("lbleror")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(440, 310, 311, 51))
        self.label_8.setStyleSheet("background-color:rgba(0,0,0,0);\n"
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
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.lePassword_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.lePassword_2.setGeometry(QtCore.QRect(480, 310, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma,sans-serif")
        font.setPointSize(-1)
        self.lePassword_2.setFont(font)
        self.lePassword_2.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"border:none;\n"
"border-radius: 10px;\n"
"color:rgba(0,0,0,240);\n"
"background-color: transparent;\n"
"font-family: \"Tahoma\", sans-serif;\n"
"font-size: 18px;\n"
"padding: 10px; ")
        self.lePassword_2.setFrame(True)
        self.lePassword_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lePassword_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lePassword_2.setObjectName("lePassword_2")
        self.label_9 = QtWidgets.QLabel(parent=self.widget)
        self.label_9.setGeometry(QtCore.QRect(450, 320, 31, 31))
        self.label_9.setStyleSheet("")
        self.label_9.setLineWidth(1)
        self.label_9.setText("")
        self.label_9.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_9.setPixmap(QtGui.QPixmap("Interface/Png/Icon/reset-password-icon.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(550, 80, 81, 71))
        self.label_10.setStyleSheet("")
        self.label_10.setLineWidth(1)
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_10.setPixmap(QtGui.QPixmap("Interface/Png/Icon/lock_icon.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.lbl_error = QtWidgets.QLabel(parent=self.widget)
        self.lbl_error.setGeometry(QtCore.QRect(450, 370, 291, 31))
        self.lbl_error.setText("")
        self.lbl_error.setObjectName("lbl_error")
        self.lbl_backimg.raise_()
        self.label.raise_()
        self.lbl_image.raise_()
        self.label_2.raise_()
        self.btnLogin.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.leUser.raise_()
        self.label_7.raise_()
        self.lePassword.raise_()
        self.label_5.raise_()
        self.lbleror.raise_()
        self.label_8.raise_()
        self.lePassword_2.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.lbl_error.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "CHANGE PASSWORD"))
        self.leUser.setPlaceholderText(_translate("MainWindow", "Enter your Username"))
        self.btnLogin.setText(_translate("MainWindow", "Change"))
        self.lePassword.setPlaceholderText(_translate("MainWindow", "Enter your Old Password"))
        self.lePassword_2.setPlaceholderText(_translate("MainWindow", "Enter your New Password"))

        self.btnLogin.clicked.connect(self.change_password_function)
    def change_password_function(self):
        # Lấy dữ liệu từ giao diện người dùng
        username = self.leUser.text()
        old_password = self.lePassword.text()
        new_password = self.lePassword_2.text()
        # kiểm tra còn ô nào trống không
        if len(username) == 0 or len(old_password) == 0 or len(new_password) == 0:
            self.lbl_error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.lbl_error.setText("Please input all fields")
            return
        

        # Kiểm tra username để xác định loại người dùng và user_id
        user_type, user_id = self.check_username_exists(username)
        if not user_type:
            print("Username does not exist in database!")
            self.lbl_error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.lbl_error.setText("Username does not exist!")
            return

        # Lấy mật khẩu cũ từ database
        ref = db.reference(f'{user_type}/{user_id}')
        stored_password = ref.child("Password").get().encode('utf-8')

        # Kiểm tra mật khẩu cũ
        if not bcrypt.checkpw(old_password.encode('utf-8'), stored_password):
            print("Old password is incorrect!")
            self.lbl_error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.lbl_error.setText("Old password is incorrect!")
            return

        # Cập nhật mật khẩu mới
        self.update_password(user_type, user_id, new_password)

    def check_username_exists(self, username):
        # Kiểm tra username trong nhánh Students
        ref_students = db.reference('Students/')
        students = ref_students.get()
        if username in students:
            return 'Students', username
        
        # Kiểm tra username trong nhánh Admin
        ref_admin = db.reference('Admin/')
        admin = ref_admin.get()
        if admin.get('Username') == username:
            return 'Admin', 'Admin'
        
        return None, None
    def update_password(self,user_type, user_id, new_password):
        try:
                # Kiểm tra mật khẩu mạnh
                if not self.is_strong_password(new_password):
                        print("Password is not strong enough!")
                        self.lbl_error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                        self.lbl_error.setText("Password is not strong enough!")
                        return

                hashed_new = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
                ref = db.reference(f'{user_type}/{user_id}')
                ref.update({"Password": hashed_new.decode()})
                print("Password updated successfully!")
                self.lbl_error.setStyleSheet("color:rgb(0, 255, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                self.lbl_error.setText("Password updated successfully!")

        except Exception as e:
                print("Error updating password:", e)
                self.lbl_error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
                self.lbl_error.setText("Error updating password:", e)

    def is_strong_password(self, password):
        if len(password) < 8:
                return False
        if not re.search(r"[A-Z]", password):
                return False
        if not re.search(r"[a-z]", password):
                return False
        if not re.search(r"[0-9]", password):
                return False
        if not re.search(r"[\W_]", password):  # \W là viết tắt của non-word character, _ là ký tự underscore
                return False
        return True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ChangePass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
