import firebase_admin
from firebase_admin import credentials, db, storage
import cv2
import sys
import requests
import json
import os
import io
import datetime
import threading
import numpy as np
from chooseupload import Ui_MainWindow as ChooseUploadWindow
from registerpage import Ui_MainWindow as RegisterPageWindow
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLineEdit, QPushButton, QTextEdit, QVBoxLayout, QMessageBox, QApplication, QWidget, QLabel, QFileDialog, QMainWindow, QListWidget, QLabel, QListWidgetItem, QDialog, QDialogButtonBox
from PyQt6.QtGui import QIcon, QPixmap
import re

# Các hàm kiểm tra ràng buộc
def is_valid_student_id(student_id):
    return student_id.isdigit() and len(student_id) == 8

def is_valid_name(name):
    return all(word[0].isupper() for word in name.split())


def is_valid_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.]\w+)+$'
    return re.search(regex, email)

def is_valid_text_with_spaces(text):
    regex = r'^[a-zA-Z\s]+$'
    return re.match(regex, text)

def is_valid_year(year):
    return year.isdigit() and int(year) < 8

# Khởi tạo kết nối tới Firebase
cred = credentials.Certificate(r"ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     "storageBucket": "faceregconition-80c55.appspot.com"})
global_image_data = None
global_image_extension = '.jpg'

class ChooseUpload(QMainWindow, ChooseUploadWindow):
    def __init__(self, register_page):
        super().__init__()
        self.setupUi(self)
        self.register_page = register_page
        self.btnCamera.clicked.connect(self.CaptureImage)
        self.btnFile.clicked.connect(self.LoadImage)
        self.thread = None
        self.stop_thread = threading.Event()
    
    def CaptureImage(self):
        if self.thread is not None:
            self.stop_thread.set()
            self.thread.join()
            self.thread = None
        self.stop_thread.clear()
        self.thread = threading.Thread(target=self.CaptureImageThread)
        self.thread.start()

    def CaptureImageThread(self):
        global global_image_data, global_image_extension
        cam = cv2.VideoCapture(0)
        while not self.stop_thread.is_set():
            ret, frame = cam.read()
            if not ret:
                break
            cv2.imshow("VideoCapture", frame)
            k = cv2.waitKey(1)
            if k == 27:
                print("Pressed Escape, closing application")
                break
            elif k == 13 or k == 32:
                _, buffer = cv2.imencode(global_image_extension, frame)
                global_image_data = io.BytesIO(buffer)
                print("Screenshot taken successfully")
                break
        cam.release()
        cv2.destroyAllWindows()
        self.register_page.UpdateAvatar()
        QtCore.QMetaObject.invokeMethod(self, "close", QtCore.Qt.ConnectionType.QueuedConnection)
        

    def LoadImage(self):
        global global_image_data, global_image_extension
        dialog = QFileDialog()
        dialog.setNameFilter("Image (*.jpg)")
        dialog.setFileMode(QFileDialog.FileMode.AnyFile)
        if dialog.exec():
            selected_files = dialog.selectedFiles()
            if selected_files:
                image_path = selected_files[0]
                global_image_data = open(image_path, 'rb')  # Mở file ảnh và đọc dữ liệu
                global_image_extension = os.path.splitext(image_path)[1]  # Lấy đuôi tệp
                print(image_path)
                self.register_page.UpdateAvatar()
                self.close()

    def closeEvent(self, event):
        if self.thread is not None:
            self.stop_thread.set()
            self.thread.join()
            self.thread = None
        event.accept()

class RegisterPage(QMainWindow, RegisterPageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnUpAvatar.clicked.connect(self.show_choose_upload_window)
        self.btnRegister.clicked.connect(self.AddStudent)
        self.btnSelectClasses.clicked.connect(self.openClassSelectionDialog)

    def show_choose_upload_window(self):
        self.choose_upload_window = ChooseUpload(register_page=self)  # Truyền thể hiện của RegisterPage vào ChooseUpload
        self.choose_upload_window.show()
    
    def AddStudent(self):
        global global_image_data, global_image_extension
        missing_fields = []  # Danh sách lưu các trường còn thiếu

        # Kiểm tra các trường văn bản còn thiếu và các ràng buộc
        if self.txtStuID.text() == '':
            missing_fields.append("Student ID")
        elif not is_valid_student_id(self.txtStuID.text()):
            self.labelError.setText("Student ID phải là 8 ký tự số.")
            return

        if self.txtName.text() == '':
            missing_fields.append("Name")
        elif not is_valid_name(self.txtName.text()):
            self.labelError.setText("Mỗi chữ cái đầu của tên phải viết hoa.")
            return

        if self.txtEmail.text() == '':
            missing_fields.append("Email")
        elif not is_valid_email(self.txtEmail.text()):
            self.labelError.setText("Email không đúng định dạng.")
            return

        if self.txtFaculty.text() == '':
            missing_fields.append("Faculty")
        elif not is_valid_text_with_spaces(self.txtFaculty.text()):
            self.labelError.setText("Faculty chỉ bao gồm chữ cái.")
            return

        if self.txtMajor.text() == '':
            missing_fields.append("Major")
        elif not is_valid_text_with_spaces(self.txtMajor.text()):
            self.labelError.setText("Major chỉ bao gồm chữ cái.")
            return

        if self.txtYear.text() == '':
            missing_fields.append("Year")
        elif not is_valid_year(self.txtYear.text()):
            self.labelError.setText("Year phải là số và nhỏ hơn 8")
            return

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
                self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                              "font-weight: bold;\n"
                                            "font-size: 16px;\n")
                self.labelError.setText("Vui lòng chọn ảnh có khuôn mặt")

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
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n")
        self.labelError.setText("Đăng ký thành công")
        
    def RegisterFail(self, missing_fields):
        # Định dạng các trường còn thiếu thành một chuỗi với dấu gạch nối và dòng mới
        if len(missing_fields) > 4:
        # Chia thành các dòng, mỗi dòng không quá 4 phần tử
            lines = []
            for i in range(0, len(missing_fields), 4):
                lines.append(", ".join(missing_fields[i:i + 4]))
            missing_fields_str = "- " + "\n- ".join(lines)
        else:
            missing_fields_str = "- " + ", ".join(missing_fields)

        # Đặt thông báo lỗi với các trường còn thiếu được định dạng
        self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n")
        self.labelError.setText("Bạn chưa nhập đủ thông tin:\n" + missing_fields_str)
        
    def openClassSelectionDialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Select Classes")
        dialog.setGeometry(100, 100, 400, 300)
        dialog.setStyleSheet("""background-color: rgb(165,213,255);""")
        listClass = QtWidgets.QListWidget(dialog)
        listClass.setGeometry(QtCore.QRect(10, 10, 380, 200))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        listClass.setFont(font)
        listClass.setStyleSheet("""
        border: 2px solid rgb(122, 122, 122);
        border-radius: 10px;                            
        padding:10px;
        background-color: rgb(255, 255, 255);
        font-size: 18px;
        color:rgb(0, 0, 0);
        font-family: "Tahoma", sans-serif;
    QListWidget::item{
        padding:10px;
        border: none;
    }
""")
        listClass.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        listClass.setObjectName("listClass")

        # Thêm class từ firebase
        self.addClassesFromFirebase(listClass)

        buttonBox = QtWidgets.QDialogButtonBox(parent=dialog)
        buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)
        
        # Sử dụng QVBoxLayout để sắp xếp các thành phần
        mainLayout = QtWidgets.QVBoxLayout(dialog)
        mainLayout.addWidget(listClass)
        mainLayout.addWidget(buttonBox, alignment=QtCore.Qt.AlignmentFlag.AlignRight)  # Căn nút Ok và Cancel về phía phải

        buttonBox.setStyleSheet("""
            QPushButton {
                background-color: rgb(0, 119, 182);
                border-radius: 20px;
                font-size: 18px;
                color: rgb(255, 255, 255);
                font-family: "Tahoma", sans-serif;
                font-weight: bold;
                min-width: 100px;  
                min-height: 40px; 
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

        buttonBox.accepted.connect(lambda: self.updateSelectedClasses(listClass, dialog))
        buttonBox.rejected.connect(dialog.reject)

        dialog.exec()

    def updateSelectedClasses(self, listClass, dialog):
        selected_classes = [item.text() for item in listClass.selectedItems()]
        self.txtClass.setText(", ".join(selected_classes))
        dialog.accept()
        
    def addClassesFromFirebase(self, listWidget):
        try:
            ref = db.reference('Classes')
            classes = ref.get()
            
            if classes:
                for cls in classes:
                    item = QListWidgetItem(cls)
                    listWidget.addItem(item)
            else:
                QMessageBox.warning(self, "Warning", "No classes found in Firebase.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unable to fetch classes from Firebase: {e}")

def main():
    app = QApplication(sys.argv)
    # Tạo một instance của cửa sổ RegisterPage

    register_page_window = RegisterPage()
    register_page_window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
