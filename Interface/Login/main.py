# from PyQt6 import QtCore, QtGui, QtWidgets
# from PyQt6.uic import loadUi
# from PyQt6.QtWidgets import *
# import sys



# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import db
# from firebase_admin import storage
# from firebase_admin import auth,exceptions

# cred = credentials.Certificate("ServiceAccountKey.json")

# firebase_admin.initialize_app(cred, {"databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     
#                                      "storageBucket":"faceregconition-80c55.appspot.com"})


# #cửa sổ login
# class Login_w(QMainWindow):
#     def __init__(self):
#         super(Login_w,self).__init__()
#         uic.loadUi('login-ui.ui',self)
            
# #cửa sổ changePass
# class changePass_w(QMainWindow):
#     def __init__(self):
#         super(Login_w,self).__init__()
#         uic.loadUi('changePass.ui',self)


# app=QApplication(sys.argv)
# widget=QtWidgets.QStackedWidget()

# Login_f=Login_w()
# changePass_f=changePass_w()
# widget.addWidget(Login_f)
# widget.addWidget(changePass_f)
# widget.setCurrentIndex(0)
# widget.setFixedHeight(600)
# widget.setFixedWidth(853)
# widget.show()
# app.exec()

def loginFuntion(self):
        user = self.leUser.text()
        password = self.lePassword.text()

        if len(user)==0 or len(password)==0:
            self.error.setText()


