import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

import cv2
import sys
sys.path.insert(1, 'Interface\Students\Home')
from face_matching import *
import os
import datetime
import threading
from chooseupload import Ui_MainWindow as ChooseUploadWindow
from registerpage import Ui_MainWindow as RegisterPageWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMessageBox, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog,QMainWindow
from PyQt6.QtGui import QIcon, QPixmap

cred = credentials.Certificate(r"ServiceAccountKey.json")

firebase_admin.initialize_app(cred, {"databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                        "storageBucket":"faceregconition-80c55.appspot.com"})
image_path=None

class ChooseUpload(QMainWindow, ChooseUploadWindow):
    def __init__(self, register_page):
        super().__init__()
        self.setupUi(self)
        self.register_page = register_page
        self.btnCamera.clicked.connect(self.CaptureImage)
        self.btnFile.clicked.connect(self.LoadImage)
        
    def closeEvent(self, event):
        global image_path
        print("Image path when closing ChooseUpload:", image_path)
        event.accept()  # Chấp nhận sự kiện đóng cửa sổ
        
    def CaptureImage(self):
        # Khởi tạo luồng mới để chụp ảnh từ camera
        self.thread = threading.Thread(target=self.CaptureImageThread)
        self.thread.start()
    
    def CaptureImageThread(self):
        cam = cv2.VideoCapture(0)
        global image_path
        while True:
            ret, frame = cam.read()

            if not ret:
                print("failed to grab frame")
                break

            cv2.imshow("VideoCapture", frame)

            k = cv2.waitKey(1)

            if k == 27:
                print("Escape hit, closing app")
                break
            elif k == 13 or k == 32:
                img_name = "Interface\\Students\\Register\\Capture\\Capture.png"
                cv2.imwrite(img_name, frame)
                print("screenshot taken")
                image_path = img_name  # Lưu đường dẫn của ảnh
                cv2.destroyAllWindows()  # Đóng tất cả các cửa sổ
                break

        cam.release()
        print(image_path)
        self.register_page.UpdateAvatar()

        
    def LoadImage(self):
        global image_path
        
        # Tạo dialog chọn ảnh
        dialog = QFileDialog()
        dialog.setNameFilter("Hình ảnh (*.png *.jpg)")
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        
        # Mở dialog và kiểm tra kết quả trả về
        if dialog.exec():
                # Lấy đường dẫn của ảnh được chọn
                selected_files = dialog.selectedFiles()
                if selected_files:
                        image_path = selected_files[0]  # Lấy đường dẫn của ảnh đầu tiên
        print(image_path)
        self.register_page.UpdateAvatar()

class RegisterPage(QMainWindow, RegisterPageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnUpAvatar.clicked.connect(self.show_choose_upload_window)
        self.btnRegister.clicked.connect(self.AddStudent)

    def show_choose_upload_window(self):
        self.choose_upload_window = ChooseUpload(register_page=self)  # Truyền thể hiện của RegisterPage vào ChooseUpload
        self.choose_upload_window.show()
        
    def AddStudent(self):
        global image_path
        missing_fields = []  # List to store missing fields
        # Check for missing text fields
        if self.txtEmail.text() == '':
                missing_fields.append("Email")
        if self.txtFaculty.text() == '':
                missing_fields.append("Faculty")
        if self.txtMajor.text() == '':
                missing_fields.append("Major")
        if self.txtName.text() == '':
                missing_fields.append("Name")
        if self.txtYear.text() == '':
                missing_fields.append("Year")
        if self.txtStuID.text() == '':
                missing_fields.append("Student ID")
        if self.txtClass.text() == '':
                missing_fields.append("Class")
        else:
                StrClass = self.txtClass.text()
                # Chuyển toàn bộ chuỗi lớp thành chữ in hoa
                StrClass = StrClass.upper()

                # Loại bỏ khoảng trắng
                StrClass = StrClass.replace(" ", "")

                # Tách Class
                Class = StrClass.split(",")

                # Loại bỏ các lớp bị trùng lặp
                Class = list(set(Class))

        # Check for missing image and handle potential errors
        if image_path is None:
                missing_fields.append("Image")

        # Handle missing fields and display error message if any
        if missing_fields:
                self.RegisterFail(missing_fields)
                return
        else:
                # If all fields are valid, proceed with Firebase Realtime Database update
                try:
                        # Image processing logic (assuming appropriate libraries are imported)
                        # Đường dẫn tới tệp trên máy tính
                        local_file_path = image_path

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

                        # Firebase Realtime Database update logic
                        ref = db.reference('Students/')
                        user_ref = ref.child(self.txtStuID.text())
                        user_ref.update({
                                'Email': self.txtEmail.text(),
                                'Faculty': self.txtFaculty.text(),
                                'Major': self.txtMajor.text(),
                                'Name': self.txtName.text(),
                                'Year': self.txtYear.text(),
                                'embeddings': embedding[0]['embedding'],  # Assuming embedding extraction is successful
                                'Classes': {}
                        })
                        Classes_ref = user_ref.child('Classes/')
                        # Assuming 'class' is a list of class names
                        for c in Class:
                                now = datetime.datetime.now()
                                # Định dạng chuỗi ngày và giờ
                                Date = now.strftime("%Y-%m-%d %H:%M:%S")
                                class_ref = Classes_ref.child(c)
                                class_ref.update({
                                'AttendanceCount': '0',
                                'Datetime': Date
                                })

                        # Firebase Storage upload logic
                        # Đường dẫn tới tệp trên máy tính
                        local_file_path = image_path

                        # Lấy đuôi tệp từ đường dẫn tệp hình ảnh
                        file_name, file_extension = os.path.splitext(local_file_path)
                        # Kết nối tới Firebase Storage
                        bucket = storage.bucket()
                        blob = bucket.blob(f'images/{self.txtStuID.text()}{file_extension}')  # Đường dẫn tới tệp trên Firebase Storage

                        # Upload tệp từ máy tính lên Firebase Storage
                        blob.upload_from_filename(local_file_path)
                        # ... Success message or logic ...
                        self.RegisterSuccess()

                except Exception as e:
                        self.UploadFail(e)
                        print("Không thể thêm student vào database:", e)
     
    def UpdateAvatar(self):
        global image_path
        if image_path:
                # Đọc ảnh từ đường dẫn
                pixmap = QPixmap(image_path)

                # Thay thế ảnh cho btnUpAvatar
                self.btnUpAvatar.setIcon(QIcon(pixmap))
                self.btnUpAvatar.setIconSize(QtCore.QSize(150, 150))
    
    def RegisterSuccess(self):
        self.labelError.setStyleSheet("color:rgb(0, 255, 0);\n"
                                "background-color: rgb(255, 255, 255);\n"
                                "font-size: 20px;\n"
                                "font-family: \"Tahoma\", sans-serif;\n"
                                "qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
                                "font-weight: bold;\n")
        self.labelError.setText("Đã đăng kí thành công")
        
    def RegisterFail(self, missing_fields):
        # Format missing fields into a string with line breaks
        missing_fields_str = "- " + ", ".join(missing_fields)

        # Set the error message with formatted missing fields
        self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "font-size: 14px;\n"
                                    "font-family: \"Tahoma\", sans-serif;\n"
                                    "font-weight: bold;\n")
        self.labelError.setText("Bạn chưa nhập đủ thông tin:\n" + missing_fields_str)
        
    def UploadFail(self, e):
        dialog = QMessageBox()
        dialog.setText(f"Không thể thêm student vào database:{e}")
        dialog.setWindowTitle("Lỗi")
        dialog.setIcon(QMessageBox.Icon.Critical)
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.exec()


def main():
    app = QApplication(sys.argv)
    # Create an instance of the RegisterPage window
    register_page_window = RegisterPage()
    register_page_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
