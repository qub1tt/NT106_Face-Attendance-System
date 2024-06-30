import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import requests,json
import cv2
import sys
sys.path.insert(1, 'Interface\Students\Home')

import os
import io
import datetime
import threading
import numpy as np
from chooseupload import Ui_MainWindow as ChooseUploadWindow
from registerpage import Ui_MainWindow as RegisterPageWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMessageBox, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QFileDialog, QMainWindow
from PyQt6.QtGui import QIcon, QPixmap

# Khởi tạo kết nối tới Firebase
cred = credentials.Certificate(r"ServiceAccountKey.json")

firebase_admin.initialize_app(cred, {"databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     "storageBucket": "faceregconition-80c55.appspot.com"})
global_image_data = None
global_image_extension = '.png'


class ChooseUpload(QMainWindow, ChooseUploadWindow):
    def __init__(self, register_page):
        super().__init__()
        self.setupUi(self)
        self.register_page = register_page
        self.btnCamera.clicked.connect(self.CaptureImage)
        self.btnFile.clicked.connect(self.LoadImage)
        
    def CaptureImage(self):
        # Khởi tạo luồng mới để chụp ảnh từ camera
        self.thread = threading.Thread(target=self.CaptureImageThread)
        self.thread.start()
    
    def CaptureImageThread(self):
        global global_image_data, global_image_extension
        cam = cv2.VideoCapture(0)
        while True:
            ret, frame = cam.read()

            if not ret:
                break

            cv2.imshow("VideoCapture", frame)

            k = cv2.waitKey(1)

            if k == 27:
                print("Nhấn phím Escape, đóng ứng dụng")
                break
            elif k == 13 or k == 32:
                _, buffer = cv2.imencode(global_image_extension, frame)
                global_image_data = io.BytesIO(buffer)

                print("Chụp màn hình thành công")
                cv2.destroyAllWindows()
                break

        cam.release()
        self.register_page.UpdateAvatar()

    def LoadImage(self):
        global global_image_data, global_image_extension
        # Tạo hộp thoại chọn ảnh
        dialog = QFileDialog()
        dialog.setNameFilter("Hình ảnh (*.png *.jpg)")
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)

        # Mở hộp thoại và kiểm tra kết quả trả về
        if dialog.exec():
            # Lấy đường dẫn của ảnh được chọn
            selected_files = dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]  # Lấy đường dẫn của ảnh đầu tiên
                global_image_data = open(image_path, 'rb')  # Mở file ảnh và đọc dữ liệu
                global_image_extension = os.path.splitext(image_path)[1]  # Lấy đuôi tệp
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

        global global_image_data, global_image_extension
        missing_fields = []  # Danh sách lưu các trường còn thiếu
        # Kiểm tra các trường văn bản còn thiếu
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

        # Kiểm tra ảnh còn thiếu và xử lý lỗi có thể xảy ra
        if global_image_data is None:
            missing_fields.append("Image")

        # Xử lý các trường còn thiếu và hiển thị thông báo lỗi nếu có
        if missing_fields:
            self.RegisterFail(missing_fields)
            return
        else:
            # Nếu tất cả các trường hợp hợp lệ, tiến hành cập nhật Firebase Realtime Database
            try:
                # Xử lý hình ảnh (giả định các thư viện cần thiết đã được nhập)
                # Chuyển đổi dữ liệu ảnh từ io.BytesIO sang định dạng có thể xử lý bởi OpenCV
                global_image_data.seek(0)
                file_bytes = np.asarray(bytearray(global_image_data.read()), dtype=np.uint8)
                embedding = None
                
                img_bytes = file_bytes.tobytes()
                response = requests.post('https://face-attendance.azurewebsites.net/detect_faces', files={'image':img_bytes})
                faces = response.json()

                # Phát hiện khuôn mặt trong ảnh
                for face in faces:
                    # Align the face
                    align_response = requests.post(
                            'https://face-attendance.azurewebsites.net/align_face', 
                            files={'image': img_bytes}, 
                            data={'face': json.dumps(face)}, # Ensure the JSON data is sent correctly
                    )
                    aligned_face = align_response.json()

                    # Convert the aligned face back to an image format
                    aligned_face_img = np.array(aligned_face, dtype=np.uint8)
                    _, buffer = cv2.imencode('.jpg', aligned_face_img)
                    aligned_face_bytes = buffer.tobytes()

                    # Extract features from the aligned face
                    features_response = requests.post('https://face-attendance.azurewebsites.net/extract_features', files={'image': aligned_face_bytes})
                    embedding = features_response.json()
 
                    break

                # Cập nhật Firebase Realtime Database
                ref = db.reference('Students/')
                user_ref = ref.child(self.txtStuID.text())
                user_ref.update({
                    'Email': self.txtEmail.text(),
                    'Faculty': self.txtFaculty.text(),
                    'Major': self.txtMajor.text(),
                    'Name': self.txtName.text(),
                    'Year': self.txtYear.text(),
                    'embeddings': embedding,  # Giả định trích xuất đặc trưng thành công
                    'Classes': {}
                })
                Classes_ref = user_ref.child('Classes/')
                # Giả định 'class' là danh sách các tên lớp học
                for c in Class:
                    now = datetime.datetime.now()
                    # Định dạng chuỗi ngày và giờ
                    Date = now.strftime("%Y-%m-%d %H:%M:%S")
                    class_ref = Classes_ref.child(c)
                    class_ref.update({
                        'AttendanceCount': 0,
                        'Datetime': Date
                    })

                # Tải lên Firebase Storage
                # Kết nối tới Firebase Storage
                bucket = storage.bucket()
                blob = bucket.blob(f'images/{self.txtStuID.text()}{global_image_extension}')  # Đường dẫn tới tệp trên Firebase Storage

                # Tải tệp từ bộ nhớ lên Firebase Storage
                global_image_data.seek(0)
                blob.upload_from_file(global_image_data, content_type=f'image/{global_image_extension.strip(".")}')
                # Hiển thị thông báo thành công
                self.RegisterSuccess()

            except Exception as e:
                # Hiển thị thông báo thất bại
                self.UploadFail(e)
                print("Không thể thêm sinh viên vào cơ sở dữ liệu:", e)

    def UpdateAvatar(self):
        global global_image_data
        if global_image_data:
            # Đọc ảnh từ image_data
            global_image_data.seek(0)
            pixmap = QPixmap()
            pixmap.loadFromData(global_image_data.read())

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
        # Định dạng các trường còn thiếu thành một chuỗi với dấu gạch nối và dòng mới
        missing_fields_str = "- " + ", ".join(missing_fields)

        # Đặt thông báo lỗi với các trường còn thiếu được định dạng
        self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "font-size: 14px;\n"
                                      "font-family: \"Tahoma\", sans-serif;\n"
                                      "font-weight: bold;\n")

        self.labelError.setText("Bạn chưa nhập đủ thông tin:\n" + missing_fields_str)
        
    def UploadFail(self, e):
        dialog = QMessageBox()
        dialog.setText(f"Không thể thêm sinh viên vào cơ sở dữ liệu: {e}")
        dialog.setWindowTitle("Lỗi")
        dialog.setIcon(QMessageBox.Icon.Critical)
        dialog.setStandardButtons(QMessageBox.StandardButton.Ok)
        dialog.exec()


def main():
    app = QApplication(sys.argv)
    # Tạo một instance của cửa sổ RegisterPage
    register_page_window = RegisterPage()
    register_page_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
