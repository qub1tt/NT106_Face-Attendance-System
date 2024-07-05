import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtGui import QIcon
from login_ui import Ui_Login
from changePass import Ui_ChangePass
from forgotPass import Ui_ForgotPass
from confirmOTP import Ui_OTP



class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Login')
        self.setWindowIcon(QIcon("Interface/Png/Icon/face-id.png"))
        self.setGeometry(100, 100, 800, 500)

        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        
        main_layout = QtWidgets.QVBoxLayout(central_widget)
        self.stacked_widget = QtWidgets.QStackedWidget(self)
        main_layout.addWidget(self.stacked_widget)

        self.forgot_pass_page = QtWidgets.QMainWindow()
        self.login_page = QtWidgets.QMainWindow()
        self.change_pass_page = QtWidgets.QMainWindow()
        self.confirmOTP_page = QtWidgets.QMainWindow()
        
        self.forgot_pass_ui = Ui_ForgotPass()
        self.forgot_pass_ui.setupUi(self.forgot_pass_page)
        self.forgot_pass_ui.MainWindow = self  # Truyền MainWindow tới forgot_pass_ui

        self.login_ui = Ui_Login()
        self.login_ui.setupUi(self.login_page)
        self.login_ui.MainWindow = self
        
        self.change_pass_ui = Ui_ChangePass()
        self.change_pass_ui.setupUi(self.change_pass_page)

        self.confirm_OTP_ui = Ui_OTP()
        self.confirm_OTP_ui.setupUi(self.confirmOTP_page)
        
        self.stacked_widget.addWidget(self.login_page)
        self.stacked_widget.addWidget(self.change_pass_page)
        self.stacked_widget.addWidget(self.forgot_pass_page)
        self.stacked_widget.addWidget(self.confirmOTP_page)
        
        self.btnLogin = QtWidgets.QPushButton(self)
        self.btnLogin.setFixedSize(60, 40)
        self.btnLogin.setIcon(QtGui.QIcon("Interface/Png/Icon/back.png"))
        self.btnLogin.setIconSize(QtCore.QSize(30, 30))
        self.btnLogin.move(10, 10)
        self.btnLogin.clicked.connect(self.show_login)
        
        self.btnLogin.raise_()
        self.login_ui.pushButton.clicked.connect(self.show_change_pass)
        self.login_ui.btnForgotPassword.clicked.connect(self.show_forgot_pass)

        self.show_login()

    def show_login(self, event=None):
        self.stacked_widget.setCurrentWidget(self.login_page)
        self.btnLogin.hide()
    
    def show_change_pass(self, event=None):
        self.stacked_widget.setCurrentWidget(self.change_pass_page)
        self.btnLogin.show()

    def show_forgot_pass(self, event=None):
        self.stacked_widget.setCurrentWidget(self.forgot_pass_page)
        self.btnLogin.show()

    def show_confirm_OTP(self, event=None):
        self.stacked_widget.setCurrentWidget(self.confirmOTP_page)
        self.btnLogin.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
