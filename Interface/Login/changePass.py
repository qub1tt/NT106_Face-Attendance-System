# Form implementation generated from reading ui file 'changePass.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
import bcrypt

import subprocess
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("ServiceAccountKey.json")

firebase_admin.initialize_app(cred, {"databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     
                                     "storageBucket":"faceregconition-80c55.appspot.com"})

ref = db.reference("Admin")
passw = ref.child("Password").get().encode("utf-8")

def update_password(new_password):
        try:
                hashed_new = bcrypt.hashpw(new_password.encode('utf-8'),bcrypt.gensalt())
                ref.update({"Password": hashed_new.decode()})
                print("Password updated successfully!")

        except Exception as e:
                print("Error updating password:", e)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(429, 547)
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
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:black;\n"
"")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.leUser = QtWidgets.QLineEdit(parent=self.widget)
        self.leUser.setGeometry(QtCore.QRect(70, 100, 310, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.leUser.setFont(font)
        self.leUser.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.leUser.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.leUser.setObjectName("leUser")
        self.btnLogin = QtWidgets.QPushButton(parent=self.widget)
        self.btnLogin.setGeometry(QtCore.QRect(20, 380, 360, 60))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
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
        self.label_4 = QtWidgets.QLabel(parent=self.widget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 50, 50))
        self.label_4.setStyleSheet("background-color:rgb(76,198,198)")
        self.label_4.setLineWidth(1)
        self.label_4.setText("")
        self.label_4.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_4.setPixmap(QtGui.QPixmap("Interface/Png/Icon/user.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_6 = QtWidgets.QLabel(parent=self.widget)
        self.label_6.setGeometry(QtCore.QRect(20, 100, 360, 50))
        self.label_6.setStyleSheet("background-color:white;\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.lePassword = QtWidgets.QLineEdit(parent=self.widget)
        self.lePassword.setGeometry(QtCore.QRect(70, 190, 310, 50))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.lePassword.setFont(font)
        self.lePassword.setStyleSheet("background-color:rgba(255,255,255,255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46,82,101,200);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;")
        self.lePassword.setFrame(True)
        self.lePassword.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.lePassword.setObjectName("lePassword")
        self.label_7 = QtWidgets.QLabel(parent=self.widget)
        self.label_7.setGeometry(QtCore.QRect(20, 190, 360, 50))
        self.label_7.setStyleSheet("background-color:white;\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(parent=self.widget)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 50, 50))
        self.label_5.setStyleSheet("background-color:rgb(76,198,198)")
        self.label_5.setLineWidth(1)
        self.label_5.setText("")
        self.label_5.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_5.setPixmap(QtGui.QPixmap("Interface/Png/Icon/password.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_8 = QtWidgets.QLabel(parent=self.widget)
        self.label_8.setGeometry(QtCore.QRect(20, 270, 360, 50))
        self.label_8.setStyleSheet("background-color:white;")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.label_10 = QtWidgets.QLabel(parent=self.widget)
        self.label_10.setGeometry(QtCore.QRect(20, 280, 50, 50))
        self.label_10.setStyleSheet("background-color:rgb(76,198,198)")
        self.label_10.setLineWidth(1)
        self.label_10.setText("")
        self.label_10.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.label_10.setPixmap(QtGui.QPixmap("Interface/Png/Icon/changepassword2.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setWordWrap(False)
        self.label_10.setOpenExternalLinks(False)
        self.label_10.setObjectName("label_10")
        self.leUser_2 = QtWidgets.QLineEdit(parent=self.widget)
        self.leUser_2.setGeometry(QtCore.QRect(70, 280, 310, 50))
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
        self.label_6.raise_()
        self.label_4.raise_()
        self.leUser.raise_()
        self.label_7.raise_()
        self.lePassword.raise_()
        self.label_5.raise_()
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
        self.leUser.setPlaceholderText(_translate("MainWindow", "Username or Email"))
        self.btnLogin.setText(_translate("MainWindow", "Change Password"))
        self.lePassword.setPlaceholderText(_translate("MainWindow", "Enter your Old-Password"))
        self.leUser_2.setPlaceholderText(_translate("MainWindow", "Enter your New-Password"))


        self.btnLogin.clicked.connect(self.change_password_function)

    def change_password_function(self):
        # Lấy mật khẩu mới từ giao diện
        old_password = self.lePassword.text()
        new_password = self.leUser_2.text()

        old_pass = old_password.encode("utf-8")
        
        result = bcrypt.checkpw(old_pass, passw) 

        if result:
                # Gọi hàm update_password để cập nhật mật khẩu trong cơ sở dữ liệu Firebase
                update_password(new_password)
        else:
             print("Mat khau cu khong dung!")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
