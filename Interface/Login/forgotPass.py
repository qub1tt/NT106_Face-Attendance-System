from PyQt6 import QtCore, QtGui, QtWidgets
from confirmOTP import Ui_OTP
from newpass import Ui_ChangePass

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import os
import bcrypt
import re
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


import firebase_init

class OTPSender:
    def __init__(self):
        self.email_address = "duyhoangnguyen1711@gmail.com"  # Thay đổi thành địa chỉ email của bạn
        self.email_password = "mlyy pxzo mbwf ansb"  # Thay đổi thành mật khẩu email của bạn

    def generate_otp(self):
        otp = ''.join(random.choices('0123456789', k=6))  # Tạo mã OTP 6 chữ số ngẫu nhiên
        return otp

    def send_otp_email(self, receiver_email, otp):
        # Load HTML template
        with open(r'Interface\Login\template.html', 'r', encoding='utf-8') as file:
            html_template = file.read()

        # Replace placeholder with actual OTP
        html_content = html_template.replace('{{ otp }}', otp)

        msg = MIMEMultipart()
        msg['From'] = self.email_address
        msg['To'] = receiver_email
        msg['Subject'] = "OTP for Password Reset"

        # Attach HTML content
        msg.attach(MIMEText(html_content, 'html'))

        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                server.starttls()
                server.login(self.email_address, self.email_password)
                server.send_message(msg)
            print("OTP email sent successfully!")
        except Exception as e:
            print(f"Error sending OTP email: {e}")


class Ui_ForgotPass(object):
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
        self.lbl_image.setGeometry(QtCore.QRect(290, 40, 611, 431))
        self.lbl_image.setStyleSheet("")
        self.lbl_image.setText("")
        self.lbl_image.setPixmap(QtGui.QPixmap("Interface/Png/Image/forgotpassword.png"))
        self.lbl_image.setScaledContents(True)
        self.lbl_image.setObjectName("lbl_image")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(70, 30, 250, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 22px;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.leUser = QtWidgets.QLineEdit(parent=self.widget)
        self.leUser.setGeometry(QtCore.QRect(80, 310, 261, 50))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
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
        self.btnLogin.setGeometry(QtCore.QRect(40, 390, 301, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
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
        self.label_4.setGeometry(QtCore.QRect(50, 320, 31, 31))
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_4.setPixmap(QtGui.QPixmap("Interface/Png/Icon/user_icon.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 310, 311, 51))
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
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(140, 90, 91, 91))
        self.label_5.setStyleSheet("")
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_5.setPixmap(QtGui.QPixmap("Interface/Png/Icon/email_icon.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_3 = QtWidgets.QLabel(parent=self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 190, 311, 51))
        self.label_3.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(30, 220, 311, 51))
        self.label_7.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 14px;\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.label_Error = QtWidgets.QLabel(parent=self.widget)
        self.label_Error.setGeometry(QtCore.QRect(50, 260, 291, 41))
        self.label_Error.setStyleSheet("color:rgb(255, 0, 0);\n"
"font-size: 18px;\n"
"font-weight: bold;")
        self.label_Error.setText("")
        self.label_Error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_Error.setObjectName("label_Error")
        self.lbl_backimg.raise_()
        self.label.raise_()
        self.lbl_image.raise_()
        self.label_2.raise_()
        self.btnLogin.raise_()
        self.label_6.raise_()
        self.label_4.raise_()
        self.leUser.raise_()
        self.label_5.raise_()
        self.label_3.raise_()
        self.label_7.raise_()
        self.label_Error.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "FORGOT PASSWORD ?"))
        self.leUser.setPlaceholderText(_translate("MainWindow", "Enter your Email"))
        self.btnLogin.setText(_translate("MainWindow", "Send to"))
        self.label_3.setText(_translate("MainWindow", "Please enter your email address to "))
        self.label_7.setText(_translate("MainWindow", "receive a verification code"))

        self.btnLogin.clicked.connect(self.sendOTP)

    def sendOTP(self):
        
        email_address = self.leUser.text()  # Địa chỉ email của người dùng
        user_type, user_id = self.check_email_exists(email_address)
        if len(email_address) == 0 :
            self.label_Error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                            "font-size: 18px;\n"
                                            "font-weight: bold;")
            self.label_Error.setText("Please input all fields")
            return
        if not user_type:
            print("Email does not exist in database")
            self.label_Error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                            "font-size: 18px;\n"
                                            "font-weight: bold;")
            self.label_Error.setText("Email does not exist")
            return

        # Chỉ khởi tạo và hiển thị cửa sổ OTP nếu email tồn tại
        self.otp_window = Ui_OTP()
        self.otp_window.setupUi(MainWindow)
        MainWindow.show()

        otp_sender = OTPSender()
        otp = otp_sender.generate_otp()
        otp_sender.send_otp_email(email_address, otp)
        print("OTP email sent successfully!")
        self.label_Error.setStyleSheet("color:rgb(0, 255, 0);\n"
                                        "font-size: 18px;\n"
                                        "font-weight: bold;")
        self.label_Error.setText("OTP email sent successfully!")
        self.otp_window.btnLogin.clicked.connect(lambda: self.confirmOTP(MainWindow, otp, user_type, user_id))

    def confirmOTP(self, MainWindow, generated_otp, user_type, user_id):
        # Lấy mã OTP từ QLineEdit
        entered_otp = self.otp_window.leUser.text()

        # So sánh mã OTP nhập vào với mã OTP được tạo ra
        if entered_otp == generated_otp:  # Thay `generated_otp` bằng mã OTP đã được tạo ra
            print("OTP verified successfully!")
            self.otp_window.label_Error.setStyleSheet("color:rgb(0, 255, 0);\n"
                                                    "font-size: 18px;\n"
                                                    "font-weight: bold;")
            self.otp_window.label_Error.setText("OTP verified successfully!")
            self.show_newpass_window(user_type, user_id)
        else:
            print("OTP does not match. Please try again.")
            self.otp_window.label_Error.setStyleSheet("color:rgb(255, 0, 0);\n"
                                                    "font-size: 18px;\n"
                                                    "font-weight: bold;")
            self.otp_window.label_Error.setText("OTP does not match. Please try again.")

    def show_newpass_window(self, user_type, user_id):
        # Hiển thị cửa sổ newpass
        self.newpass_window = Ui_ChangePass()
        self.newpass_window.setupUi(MainWindow)
        MainWindow.show()
        self.newpass_window.btnLogin.clicked.connect(lambda: self.change_password_function(user_type, user_id))

    def change_password_function(self, user_type, user_id):
        new_password = self.newpass_window.lePassword.text()
        confirm_password = self.newpass_window.lePassword_2.text()

        # Kiểm tra mật khẩu mạnh
        if not self.is_strong_password(new_password):
            print("Password is not strong enough!")
            self.newpass_window.label_Error.setStyleSheet("color:rgb(255, 0, 0);"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.newpass_window.label_Error.setText("Password is not strong enough!")
            return

        if new_password != confirm_password:
            print("Passwords do not match!")
            self.newpass_window.label_Error.setStyleSheet("color:rgb(255, 0, 0);"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.newpass_window.label_Error.setText("Passwords do not match!")
            return

        try:
            hashed_new = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
            # Cập nhật mật khẩu vào cơ sở dữ liệu
            self.update_password(user_type, user_id, hashed_new.decode())
            print("Password updated successfully!")
            self.newpass_window.label_Error.setStyleSheet("color:rgb(0, 255, 0);\n"
                                                        "font-size: 18px;\n"
                                                        "font-weight: bold;")
            self.newpass_window.label_Error.setText("Password updated successfully!")
        except Exception as e:
            self.newpass_window.label_Error.setText("Error")
            print("Error: ",e)
            
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

    def check_email_exists(self, email):
        # Kiểm tra email trong database Firebase
        ref_students = db.reference('Students/')
        students = ref_students.get()
        for student_id, student in students.items():
            if student.get('Email') == email:
                return 'Students', student_id
        
        ref_admin = db.reference('Admin/')
        admin = ref_admin.get()
        if admin.get('Email') == email:
            return 'Admin', 'Admin'
        
        return None, None

    def update_password(self, user_type, user_id, hashed_password):
        # Cập nhật mật khẩu trong database Firebase
        if user_type == 'Students':
            ref = db.reference(f'Students/{user_id}')
        elif user_type == 'Admin':
            ref = db.reference('Admin/')

        ref.update({"Password": hashed_password})


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ForgotPass()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
