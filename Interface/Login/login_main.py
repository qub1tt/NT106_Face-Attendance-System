import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from login_ui import Ui_Login
from changePass import Ui_ChangePass
from forgotPass import Ui_ForgotPass

from forgotPass import OTPSender




import firebase_init


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Application')
        self.setGeometry(100, 100, 800, 500)

        # Create central widget and set it as the central widget
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Create a layout for the central widget
        main_layout = QtWidgets.QVBoxLayout(central_widget)
        
        # Create the stacked widget and add it to the main layout
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        main_layout.addWidget(self.stacked_widget)
        
        # Create the pages and add them to the stacked widget
        self.forgot_pass_page = QtWidgets.QMainWindow()
        self.login_page = QtWidgets.QMainWindow()
        self.change_pass_page = QtWidgets.QMainWindow()
        
        self.forgot_pass_ui = Ui_ForgotPass()
        self.forgot_pass_ui.setupUi(self.forgot_pass_page)

        self.login_ui = Ui_Login()
        self.login_ui.setupUi(self.login_page)
        
        self.change_pass_ui = Ui_ChangePass()
        self.change_pass_ui.setupUi(self.change_pass_page)
        
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.change_pass_page)
        self.stacked_widget.addWidget(self.forgot_pass_page)

        
        # Create btnLogin button and ensure it is always on top
        self.btnLogin = QtWidgets.QPushButton(self)
        self.btnLogin.setFixedSize(60, 40)
        self.btnLogin.setIcon(QtGui.QIcon("Anh/back.png"))
        self.btnLogin.setIconSize(QtCore.QSize(30, 30))
        self.btnLogin.move(10, 10)
        self.btnLogin.clicked.connect(self.show_login)
        
        # Ensure the button is always on top
        self.btnLogin.raise_()

        # Connect button to show the change password page
        self.login_ui.pushButton.clicked.connect(self.show_change_pass)

        self.login_ui.btnForgotPassword.clicked.connect(self.show_forgot_pass)

        self.show_login()
    
    def show_login(self, event=None):
        self.stacked_widget.setCurrentWidget(self.login_page)
    
    def show_change_pass(self, event=None):
        self.stacked_widget.setCurrentWidget(self.change_pass_page)
    def show_forgot_pass(self, event=None):
        self.stacked_widget.setCurrentWidget(self.forgot_pass_page)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
