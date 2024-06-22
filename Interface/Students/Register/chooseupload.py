# Form implementation generated from reading ui file 'chooseupload.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMessageBox, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon, QPixmap

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 259)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 521, 261))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.btnCamera = QtWidgets.QPushButton(parent=self.widget)
        self.btnCamera.setGeometry(QtCore.QRect(110, 60, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.btnCamera.setFont(font)
        self.btnCamera.setStyleSheet("""
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface/Png/Icon/camera.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCamera.setIcon(icon)
        self.btnCamera.setIconSize(QtCore.QSize(50, 50))
        self.btnCamera.setObjectName("btnCamera")
        self.btnFile = QtWidgets.QPushButton(parent=self.widget)
        self.btnFile.setGeometry(QtCore.QRect(110, 140, 311, 61))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setWeight(75)
        self.btnFile.setFont(font)
        self.btnFile.setStyleSheet("""
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Interface/Png/Icon/folder.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnFile.setIcon(icon1)
        self.btnFile.setIconSize(QtCore.QSize(50, 50))
        self.btnFile.setObjectName("btnFile")
        self.label = QtWidgets.QLabel(parent=self.widget)
        self.label.setGeometry(QtCore.QRect(0, 0, 520, 260))
        self.label.setStyleSheet("background-color: rgb(165,213,255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.widget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 480, 220))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 25px;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label.raise_()
        self.label_2.raise_()
        self.btnCamera.raise_()
        self.btnFile.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Upload Option"))
        self.btnCamera.setText(_translate("MainWindow", "Load from Camera"))
        self.btnFile.setText(_translate("MainWindow", "Load form Local File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
