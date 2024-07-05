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
import subprocess

# Khởi tạo kết nối tới Firebase
cred = credentials.Certificate(r"ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     "storageBucket": "faceregconition-80c55.appspot.com"})
global_image_data = None
global_image_extension = '.jpg'
user_id = None
global_update_information = False

# Các hàm kiểm tra ràng buộc
def is_valid_student_id(student_id):
    return student_id.isdigit() and len(student_id) == 8

def is_valid_name(name):
    return all(word[0].isupper() for word in name.split())

def is_valid_email(email):
    regex = r'^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+([.]\w+)+$'
    return re.search(regex, email)

def is_valid_text_with_spaces(text):
    regex = r'^[a-zA-Z\s&\-_]+$'
    return re.match(regex, text)

def is_valid_year(year):
    return year.isdigit() and int(year) < 8

class ChooseUpload(QMainWindow, ChooseUploadWindow):
    def __init__(self, register_page):
        super().__init__()
        self.setupUi(self)
        self.register_page = register_page
        self.btnCamera.clicked.connect(self.capture_image)
        self.btnFile.clicked.connect(self.load_image_from_local)
        self.thread = None
        self.stop_thread = threading.Event()
        self.closing = False  # Cờ để theo dõi trạng thái đóng cửa sổ

    def capture_image(self):
        if self.thread is not None:
            self.stop_thread.set()
            self.thread.join()
            self.thread = None
        self.stop_thread.clear()
        self.closing = False  # Đặt lại cờ đóng cửa sổ
        self.thread = threading.Thread(target=self.capture_image_thread)
        self.thread.start()

    def capture_image_thread(self):
        global global_image_data, global_image_extension
        cam = cv2.VideoCapture(0)
        while not self.stop_thread.is_set() and not self.closing:
            ret, frame = cam.read()
            if not ret or self.closing:
                break
            cv2.imshow("VideoCapture", frame)
            k = cv2.waitKey(1)
            # Kiểm tra nếu cửa sổ bị đóng
            if cv2.getWindowProperty("VideoCapture", cv2.WND_PROP_VISIBLE) < 1:
                self.closing = True
                break
            if k == 27:  # ESC
                print("Pressed Escape, closing application")
                self.closing = True
                break
            elif k == 13 or k == 32:  # Enter or Space
                _, buffer = cv2.imencode(global_image_extension, frame)
                global_image_data = io.BytesIO(buffer)
                print("Screenshot taken successfully")
                break
        cam.release()
        cv2.destroyAllWindows()
        if not self.closing:
            self.register_page.update_avatar()
            QtCore.QMetaObject.invokeMethod(self, "close", QtCore.Qt.ConnectionType.QueuedConnection)

    def load_image_from_local(self):
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
                self.register_page.update_avatar()
                self.close()

    def closeEvent(self, event):
        if self.thread is not None:
            self.closing = True  # Đặt cờ đóng cửa sổ
            self.stop_thread.set()
            self.thread.join()
            self.thread = None
        event.accept()

class RegisterPage(QMainWindow, RegisterPageWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnUpAvatar.clicked.connect(self.show_choose_upload_window)
        self.btnRegister.clicked.connect(self.add_student)
        self.btnSelectClasses.clicked.connect(self.open_class_selection_dialog)
        self.btnBack.clicked.connect(self.open_login_file)
        self.load_user_id()
        self.txtStuID.setText(user_id)
        self.txtStuID.setReadOnly(True)
        self.check_update_or_register(user_id)

    def open_login_file(self):
        try:
            # Run register.py file using subprocess
            subprocess.Popen(["python", r"Interface\Students\Home\homepage.py"])
            self.close()
        except Exception as e:
            print("Error opening homepage file:", e)
            
    def load_user_id(self):
        global user_id
        user_id = os.getenv('USER_ID')
        if not user_id:
            print("No user_id found. Please log in first.")
            return
        else:
            print("Logged in user:", user_id)

    def show_choose_upload_window(self):
        self.choose_upload_window = ChooseUpload(register_page=self)
        self.choose_upload_window.show()

    def check_update_or_register(self, user_id):
        required_fields = ['Email', 'Faculty', 'Major', 'Name', 'Year', 'embeddings', 'Classes']
        ref = db.reference(f'Students/{user_id}')
        user_data = ref.get()

        if user_data:
            if all(field in user_data for field in required_fields):
                self.switch_to_update_interface()
            else:
                self.switch_to_register_interface()
        else:
            self.switch_to_register_interface()

    def switch_to_update_interface(self):
        global global_update_information
        global_update_information = True
        self.btnRegister.setText("Update")
        self.lblUpAvatar.setText("Change your avatar")
        ref = db.reference(f'Students/{user_id}')
        user_data = ref.get()
        self.txtEmail.setText(user_data.get('Email', ''))
        self.txtFaculty.setText(user_data.get('Faculty', ''))
        self.txtMajor.setText(user_data.get('Major', ''))
        self.txtName.setText(user_data.get('Name', ''))
        self.txtYear.setText(user_data.get('Year', ''))
        classes = user_data.get('Classes', {}).keys()
        self.txtClass.setText(", ".join(classes))
        self.load_image_from_storage(user_id)

    def switch_to_register_interface(self):
        self.btnRegister.setText("Register")

    def load_image_from_storage(self, user_id):
        global global_image_data, global_image_extension
        bucket = storage.bucket()
        blob = bucket.blob(f'images/{user_id}{global_image_extension}')

        if blob.exists():
            image_data = blob.download_as_bytes()
            global_image_data = io.BytesIO(image_data)  # Cập nhật global_image_data với ảnh từ Firebase Storage
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.btnUpAvatar.setIcon(QIcon(pixmap))
            self.btnUpAvatar.setIconSize(QtCore.QSize(150, 150))
        else:
            print("Image does not exist in Firebase Storage")

    def add_student(self):
        global global_image_data, global_image_extension, global_update_information
        missing_fields = []
        self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                              "font-weight: bold;\n"
                                              "font-size: 16px;\n")
        self.labelError.setText("")
        if self.txtStuID.text() == '':
            missing_fields.append("Student ID")
        elif not is_valid_student_id(self.txtStuID.text()):
            self.labelError.setText("Student ID must be an 8-digit number.")
            return

        if self.txtName.text() == '':
            missing_fields.append("Name")
        elif not is_valid_name(self.txtName.text()):
            self.labelError.setText("Each word in the name must start with an uppercase letter.")
            return

        if self.txtEmail.text() == '':
            missing_fields.append("Email")
        elif not is_valid_email(self.txtEmail.text()):
            self.labelError.setText("Invalid email format.")
            return

        if self.txtFaculty.text() == '':
            missing_fields.append("Faculty")
        elif not is_valid_text_with_spaces(self.txtFaculty.text()):
            self.labelError.setText("Faculty should only contain letters.")
            return

        if self.txtMajor.text() == '':
            missing_fields.append("Major")
        elif not is_valid_text_with_spaces(self.txtMajor.text()):
            self.labelError.setText("Major should only contain letters.")
            return

        if self.txtYear.text() == '':
            missing_fields.append("Year")
        elif not is_valid_year(self.txtYear.text()):
            self.labelError.setText("Year must be a number and less than 8.")
            return

        if self.txtClass.text() == '':
            missing_fields.append("Class")
        else:
            str_class = self.txtClass.text().upper().replace(" ", "")
            classes = str_class.split(",")

        if global_image_data is None:
            missing_fields.append("Image")

        if missing_fields:
            self.register_fail(missing_fields)
            return
        else:
            try:
                global_image_data.seek(0)
                file_bytes = np.asarray(bytearray(global_image_data.read()), dtype=np.uint8)
                embedding = None
                
                img_bytes = file_bytes.tobytes()
                response = requests.post('https://face-attendance.azurewebsites.net/detect_faces', files={'image':img_bytes})
                faces = response.json()

                for face in faces:
                    align_response = requests.post(
                        'https://face-attendance.azurewebsites.net/align_face', 
                        files={'image': img_bytes}, 
                        data={'face': json.dumps(face)}
                    )
                    aligned_face = align_response.json()

                    aligned_face_img = np.array(aligned_face, dtype=np.uint8)
                    _, buffer = cv2.imencode('.jpg', aligned_face_img)
                    aligned_face_bytes = buffer.tobytes()

                    features_response = requests.post('https://face-attendance.azurewebsites.net/extract_features', files={'image': aligned_face_bytes})
                    embedding = features_response.json()
                    break

                ref = db.reference('Students/')
                user_ref = ref.child(self.txtStuID.text())
                user_ref.update({
                    'Email': self.txtEmail.text(),
                    'Faculty': self.txtFaculty.text(),
                    'Major': self.txtMajor.text(),
                    'Name': self.txtName.text(),
                    'Year': self.txtYear.text(),
                    'embeddings': embedding
                })
                if not global_update_information:
                    classes_ref = user_ref.child('Classes/')
                    for c in classes:
                        class_ref = classes_ref.child(c)
                        class_ref.update({
                            'AttendanceCount': 0,
                            'Datetime': ""
                        })

                else:
                    classes_ref = user_ref.child('Classes/')
                    existing_classes = classes_ref.get().keys()
                    
                    # Xóa các lớp không còn trong danh sách classes
                    for existing_class in existing_classes:
                        if existing_class not in classes:
                            class_ref = classes_ref.child(existing_class)
                            class_ref.delete()
                            
                    # Thêm các lớp mới không tồn tại trong existing_classes
                    for c in classes:
                        if c not in existing_classes:
                            class_ref = classes_ref.child(c)
                            class_ref.update({
                                'AttendanceCount': 0,
                                'Datetime': ""
                            })

                bucket = storage.bucket()
                blob = bucket.blob(f'images/{self.txtStuID.text()}{global_image_extension}')

                global_image_data.seek(0)
                blob.upload_from_file(global_image_data, content_type=f'image/{global_image_extension.strip(".")}')
                self.register_success()

            except Exception as e:
                self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                              "font-weight: bold;\n"
                                              "font-size: 16px;\n")
                self.labelError.setText("Please select an image with a face.")

    def update_avatar(self):
        global global_image_data
        if global_image_data:
            global_image_data.seek(0)
            pixmap = QPixmap()
            pixmap.loadFromData(global_image_data.read())
            self.btnUpAvatar.setIcon(QIcon(pixmap))
            self.btnUpAvatar.setIconSize(QtCore.QSize(150, 150))

    def register_success(self):
        self.labelError.setStyleSheet("color:rgb(0, 255, 0);\n"
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n")
        global global_update_information
        if global_update_information:
            self.labelError.setText("Update information successful")
        else: self.labelError.setText("Registration successful")

    def register_fail(self, missing_fields):
        if len(missing_fields) > 4:
            lines = []
            for i in range(0, len(missing_fields), 4):
                lines.append(", ".join(missing_fields[i:i + 4]))
            missing_fields_str = "- " + "\n- ".join(lines)
        else:
            missing_fields_str = "- " + ", ".join(missing_fields)

        self.labelError.setStyleSheet("color:rgb(255, 0, 0);\n"
                                      "font-weight: bold;\n"
                                      "font-size: 16px;\n")
        self.labelError.setText("You have not entered enough information:\n" + missing_fields_str)

    def open_class_selection_dialog(self):
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("Select Classes")
        dialog.setGeometry(100, 100, 400, 300)
        dialog.setStyleSheet("""background-color: rgb(165,213,255);""")
        list_class = QtWidgets.QListWidget(dialog)
        list_class.setGeometry(QtCore.QRect(10, 10, 380, 200))
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        list_class.setFont(font)
        list_class.setStyleSheet("""
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
        list_class.setSelectionMode(QtWidgets.QAbstractItemView.SelectionMode.MultiSelection)
        list_class.setObjectName("listClass")

        self.add_classes_from_firebase(list_class)

        button_box = QtWidgets.QDialogButtonBox(parent=dialog)
        button_box.setOrientation(QtCore.Qt.Orientation.Horizontal)
        button_box.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok | QtWidgets.QDialogButtonBox.StandardButton.Cancel)

        main_layout = QtWidgets.QVBoxLayout(dialog)
        main_layout.addWidget(list_class)
        main_layout.addWidget(button_box, alignment=QtCore.Qt.AlignmentFlag.AlignRight)

        button_box.setStyleSheet("""
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

        button_box.accepted.connect(lambda: self.update_selected_classes(list_class, dialog))
        button_box.rejected.connect(dialog.reject)

        dialog.exec()

    def update_selected_classes(self, list_class, dialog):
        selected_classes = [item.text() for item in list_class.selectedItems()]
        self.txtClass.setText(", ".join(selected_classes))
        dialog.accept()

    def add_classes_from_firebase(self, list_widget):
        try:
            ref = db.reference('Classes')
            classes = ref.get()

            if classes:
                for cls in classes:
                    item = QListWidgetItem(cls)
                    list_widget.addItem(item)
            else:
                QMessageBox.warning(self, "Warning", "No classes found in Firebase.")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Unable to fetch classes from Firebase: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    register_page_window = RegisterPage()
    register_page_window.show()
    sys.exit(app.exec())
