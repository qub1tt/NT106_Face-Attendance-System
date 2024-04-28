# Form implementation generated from reading ui file 'registerpage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

# Kết nối với database

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import cv2
import sys
sys.path.insert(1, 'Interface\Students\Home')
from face_matching import *
import os


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMessageBox, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog
from PyQt6.QtGui import QIcon, QPixmap
cred = credentials.Certificate(r"ServiceAccountKey.json")

firebase_admin.initialize_app(cred, {"databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                        "storageBucket":"faceregconition-80c55.appspot.com"})
image_path=None

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(930, 701)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 930, 701))
        self.widget.setStyleSheet("background-color: rgb(165,213,255);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(parent=self.widget)
        self.widget_3.setGeometry(QtCore.QRect(20, 20, 891, 661))
        self.widget_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "border-radius: 20px;")
        self.widget_3.setObjectName("widget_3")
        self.txtEmail = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtEmail.setGeometry(QtCore.QRect(40, 500, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtEmail.setFont(font)
        self.txtEmail.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                "border:none;\n"
                                "border: 2px solid rgb(122, 122, 122);\n"
                                "border-radius: 10px;\n"
                                "color:rgba(0,0,0,240);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "font-size: 18px;\n"
                                "")
        self.txtEmail.setText("")
        self.txtEmail.setObjectName("txtEmail")
        self.txtFaculty = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtFaculty.setGeometry(QtCore.QRect(470, 300, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")

        self.txtFaculty.setFont(font)
        self.txtFaculty.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                "border:none;\n"
                                "border: 2px solid rgb(122, 122, 122);\n"
                                "border-radius: 10px;\n"
                                "color:rgba(0,0,0,240);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "font-size: 18px;\n"
                                "")
        self.txtFaculty.setText("")
        self.txtFaculty.setObjectName("txtFaculty")
        self.txtName = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtName.setGeometry(QtCore.QRect(40, 400, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtName.setFont(font)
        self.txtName.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                "border:none;\n"
                                "border: 2px solid rgb(122, 122, 122);\n"
                                "border-radius: 10px;\n"
                                "color:rgba(0,0,0,240);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "font-size: 18px;\n"
                                "")
        self.txtName.setText("")
        self.txtName.setObjectName("txtName")
        self.txtMajor = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtMajor.setGeometry(QtCore.QRect(470, 400, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtMajor.setFont(font)
        self.txtMajor.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                "border:none;\n"
                                "border: 2px solid rgb(122, 122, 122);\n"
                                "border-radius: 10px;\n"
                                "color:rgba(0,0,0,240);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "font-size: 18px;\n"
                                "")
        self.txtMajor.setText("")
        self.txtMajor.setObjectName("txtMajor")
        self.txtStuID = QtWidgets.QLineEdit(parent=self.widget_3)
        self.txtStuID.setGeometry(QtCore.QRect(40, 300, 391, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        self.txtStuID.setFont(font)
        self.txtStuID.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                "border:none;\n"
                                "border: 2px solid rgb(122, 122, 122);\n"
                                "border-radius: 10px;\n"
                                "color:rgba(0,0,0,240);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "font-size: 18px;\n"
                                "")
        self.txtStuID.setText("")
        self.txtStuID.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
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
        self.btnUpAvatar = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnUpAvatar.setGeometry(QtCore.QRect(150, 40, 151, 151))
        self.btnUpAvatar.setStyleSheet("border: none;\n"
                                "background-color: transparent;")
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
                                "border:none;\n"
                                "border: 2px solid rgb(122, 122, 122);\n"
                                "border-radius: 10px;\n"
                                "color:rgba(0,0,0,240);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "font-size: 18px;\n"
                                "")
        self.txtYear.setText("")
        self.txtYear.setObjectName("txtYear")
        self.btnRegister = QtWidgets.QPushButton(parent=self.widget_3)
        self.btnRegister.setGeometry(QtCore.QRect(690, 590, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btnRegister.setFont(font)
        self.btnRegister.setStyleSheet("background-color: rgb(0, 119, 182);\n"
                                "border-radius: 20px;\n"
                                "font-family:Ms Sans Serif Regular;\n"
                                "font-size:22px;\n"
                                "color:rgb(255, 255, 255);\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "font-size: 22px;\n"
                                "font-weight:bold;")
        self.btnRegister.setObjectName("btnRegister")
        self.label_14 = QtWidgets.QLabel(parent=self.widget_3)
        self.label_14.setGeometry(QtCore.QRect(460, 40, 401, 201))
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
        self.labelFaculity = QtWidgets.QLabel(parent=self.widget_3)
        self.labelFaculity.setGeometry(QtCore.QRect(470, 270, 111, 16))
        self.labelFaculity.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
                                "font-size: 18px;\n"
                                "font-weight: bold;\n"
                                "background-color: transparent;")
        self.labelFaculity.setObjectName("labelFaculity")
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
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        # Hàm bắt sự kiện click btnRegister
        self.btnRegister.clicked.connect(self.AddStudent)
        # Hàm bắt sự kiện click btnAvatar
        self.btnUpAvatar.clicked.connect(self.AddAvatar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.txtEmail.setPlaceholderText(_translate("MainWindow", "Enter your Email"))
        self.txtFaculty.setPlaceholderText(_translate("MainWindow", "Enter your Faculty"))
        self.txtName.setPlaceholderText(_translate("MainWindow", "Enter your Name"))
        self.txtMajor.setPlaceholderText(_translate("MainWindow", "Enter your Major"))
        self.txtStuID.setPlaceholderText(_translate("MainWindow", "Enter your Student ID"))
        self.lblUpAvatar.setText(_translate("MainWindow", "Upload your avatar"))
        self.txtYear.setPlaceholderText(_translate("MainWindow", "Enter your Year"))
        self.btnRegister.setText(_translate("MainWindow", "Register"))
        self.labelStuID.setText(_translate("MainWindow", "Student ID:"))
        self.labelName.setText(_translate("MainWindow", "Name:"))
        self.labelEmail.setText(_translate("MainWindow", "Email:"))
        self.labelFaculity.setText(_translate("MainWindow", "Faculity:"))
        self.labelMajor.setText(_translate("MainWindow", "Major:"))
        self.labelYear.setText(_translate("MainWindow", "Year:"))
            
    def AddStudent(self):
        if (self.txtEmail.text() == '' or self.txtFaculty.text() == '' or
            self.txtMajor.text() == '' or self.txtName.text() == '' or
            self.txtYear.text() == '' or self.txtStuID.text() == ''):
            self.MessBoxErr1()
        elif image_path is None:
            self.MessBoxErr2()
        else:
            try:
                # Kết nối tới Firebase Realtime Database
                ref = db.reference('Students/')
                user_ref = ref.child(self.txtStuID.text())
                user_ref.update({
                    'Email': self.txtEmail.text(),
                    'Faculty': self.txtFaculty.text(),
                    'Major': self.txtMajor.text(),
                    'Name': self.txtName.text(),
                    'Year': self.txtYear.text(),
                })

                # Đường dẫn tới tệp trên máy tính
                local_file_path = image_path[0]

                # Lấy đuôi tệp từ đường dẫn tệp hình ảnh
                file_name, file_extension = os.path.splitext(local_file_path)
            
                data = cv2.imread(local_file_path)

                # Detect faces in the image
                faces = detect_faces(data)

                for face in faces:
                    # Align the face
                    aligned_face = align_face(data, face)

                    # Extract features from the face
                    embedding = extract_features(aligned_face)
                    break

                ref.child(self.txtStuID.text()).update({'embeddings':embedding[0]['embedding']})
                # Kết nối tới Firebase Storage
                bucket = storage.bucket()
                blob = bucket.blob(f'images/{self.txtStuID.text()}{file_extension}')  # Đường dẫn tới tệp trên Firebase Storage
                
                # Upload tệp từ máy tính lên Firebase Storage
                blob.upload_from_filename(local_file_path)

            except Exception as e:
                print("Error processing image:", e)
     
    def AddAvatar(self):
        # Tạo dialog chọn ảnh
        dialog =QFileDialog()
        dialog.setNameFilter("Hình ảnh (*.png *.jpg)")
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        dialog.exec()
        file_path=dialog.selectedFiles()

        # Lưu đường dẫn ảnh vào biến toàn cục
        global image_path
        image_path = file_path

        # Hiển thị dialog và lấy đường dẫn ảnh
        if file_path:
            # Đọc ảnh từ đường dẫn
            pixmap = QPixmap(file_path[0])

            # Thay thế ảnh cho btnUpAvatar
            self.btnUpAvatar.setIcon(QIcon(pixmap))
            self.btnUpAvatar.setIconSize(QtCore.QSize(150, 150))
            
    def MessBoxErr1(self):
        dialog = QMessageBox()
        dialog.setText("Bạn chưa nhập đủ thông tin")
        dialog.setWindowTitle("Lỗi")
        dialog.setIcon(QMessageBox.Icon.Critical)
        
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.exec()
        
    def MessBoxErr2(self):
        dialog = QMessageBox()
        dialog.setText("Bạn chưa upload hình ảnh")
        dialog.setWindowTitle("Lỗi")
        dialog.setIcon(QMessageBox.Icon.Critical)
        
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.exec()
    

        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
