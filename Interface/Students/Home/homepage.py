# Form implementation generated from reading ui file 'homepage.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


# Import the necessary libraries
from PIL import Image
from numpy import asarray
import cv2
from datetime import datetime
import sys
import socket, pickle,struct
import requests, json
# caution: path[0] is reserved for script path (or '' in REPL)
import base64
import os

import numpy as np

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

import subprocess

# Get the form data
cred = credentials.Certificate("ServiceAccountKey.json")
firebase_admin.initialize_app(cred, {"databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
                                     "storageBucket":"faceregconition-80c55.appspot.com"})

user_id = None

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip

def match_with_database(img, database):
    # Detect faces in the frames
    # Convert the image to bytes
    _, img_encoded = cv2.imencode('.jpg', img)
    img_bytes = img_encoded.tobytes()
    
    # Send image to detect faces
    response = requests.post('https://face-attendance.azurewebsites.net/detect_faces', files={'image':img_bytes})
    faces = response.json()
    if faces:
        try:
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

                # Match the face to a face in the database
                match_response = requests.post('https://face-attendance.azurewebsites.net/match_face', json={'embedding': embedding, 'database': database})
                match = match_response.json()['match']

                if match is not None:
                    print(f"Match found: {match}")
                    for x, y, w, h in faces:
                        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
                        print("Face detected")
                        cv2.imshow("Detected Faces", img)
                        cv2.waitKey(0)  # Wait for a key press to close the window
                        cv2.destroyAllWindows()
                    return 1
                else:
                    print("No match found")
        except:
             print("DeepFace can't extract features")
    else:
        print("Can't detect face")



# Information to database               
ref = db.reference("Students")
bucket = storage.bucket()


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QComboBox, QPushButton,QMessageBox

found = None

class ClassSelectionDialog(QDialog):
    def __init__(self, class_data):
        super().__init__()

        self.setWindowTitle("Please select your class")

        layout = QVBoxLayout()

        self.class_combobox = QComboBox()
        self.class_combobox.addItems(class_data.keys())

        layout.addWidget(self.class_combobox)

        self.confirm_button = QPushButton("Confirm")
        self.confirm_button.clicked.connect(self.accept)

        layout.addWidget(self.confirm_button)

        self.setLayout(layout)
        self.resize(300, 200)
    def selected_class(self):
        return self.class_combobox.currentText()
    
class DateCheckDialog(QDialog):
    # Các phần khác trong class này giữ nguyên
    def __init__(self):
        super().__init__()
        # Các phần khác trong hàm __init__ giữ nguyên

    # Hàm mới để kiểm tra xem ngày hôm nay đã được điểm danh chưa
    def check_attendance_today(self, student_key, selected_class):
        today = datetime.now().date()
        # Kiểm tra xem ngày hôm nay đã được điểm danh chưa
        attendance_ref = db.reference(f"Students/{student_key}/Classes/{selected_class}/Datetime")
        res = attendance_ref.get()
        if res == "":
              return False
        last_attendance_date = datetime.strptime(res, "%Y-%m-%d %H:%M:%S").date()
        if last_attendance_date == today:
            # Nếu ngày hôm nay đã được điểm danh, hiển thị thông báo
            QMessageBox.information(self, "Attendance Check", "You have already checked in today.")
            return True  # Đã điểm danh trong ngày
        else:
            return False  # Chưa điểm danh trong ngày

class Ui_FaceRecognition(object):
    def setupUi(self, FaceRecognition):
        FaceRecognition.setObjectName("FaceRecognition")
        FaceRecognition.resize(1280, 720)
        FaceRecognition.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(parent=FaceRecognition)
        self.centralwidget.setObjectName("centralwidget")
        self.CameraMenu = QtWidgets.QFrame(parent=self.centralwidget)
        self.CameraMenu.setGeometry(QtCore.QRect(-1, 69, 951, 651))
        self.CameraMenu.setObjectName("CameraMenu")
        self.BorderCamera = QtWidgets.QLabel(parent=self.CameraMenu)
        self.BorderCamera.setGeometry(QtCore.QRect(50, 60, 861, 571))
        self.BorderCamera.setStyleSheet("background-color: transparent;")
        self.BorderCamera.setText("")
        self.BorderCamera.setPixmap(QtGui.QPixmap("Interface\Png\Image\BorderCamera.png"))
        self.BorderCamera.setScaledContents(True)
        self.BorderCamera.setObjectName("BorderCamera")
        self.CameraButton = QtWidgets.QPushButton(parent=self.CameraMenu)
        self.CameraButton.setGeometry(QtCore.QRect(440, 30, 61, 61))
        self.CameraButton.setAutoFillBackground(False)
        self.CameraButton.setStyleSheet("border: none;\n"
"background-color: transparent;")
        self.CameraButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Interface\Png\Icon\Webcam.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.CameraButton.setIcon(icon)
        self.CameraButton.setIconSize(QtCore.QSize(60, 60))
        self.CameraButton.setObjectName("CameraButton")
        self.BorderCamera_2 = QtWidgets.QLabel(parent=self.CameraMenu)
        self.BorderCamera_2.setGeometry(QtCore.QRect(90, 100, 781, 491))
        self.BorderCamera_2.setStyleSheet("background-color: transparent;")
        self.BorderCamera_2.setText("")
        self.BorderCamera_2.setPixmap(QtGui.QPixmap("Interface\Png\Image\BorderCamera.png"))
        self.BorderCamera_2.setScaledContents(True)
        self.BorderCamera_2.setObjectName("BorderCamera_2")
        self.StudentCard = QtWidgets.QFrame(parent=self.centralwidget)
        self.StudentCard.setGeometry(QtCore.QRect(950, 70, 330, 530))
        self.StudentCard.setObjectName("StudentCard")
        self.School = QtWidgets.QLabel(parent=self.StudentCard)
        self.School.setGeometry(QtCore.QRect(60, 30, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        self.School.setFont(font)
        self.School.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 26px;\n"
"font-weight: bold;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"background-color: transparent;")
        self.School.setObjectName("School")
        self.Name = QtWidgets.QLabel(parent=self.StudentCard)
        self.Name.setGeometry(QtCore.QRect(20, 310, 291, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        self.Name.setFont(font)
        self.Name.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 24px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.Name.setObjectName("Name")
        self.Role = QtWidgets.QLabel(parent=self.StudentCard)
        self.Role.setGeometry(QtCore.QRect(20, 350, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        self.Role.setFont(font)
        self.Role.setStyleSheet("font-family: \"Arial\", sans-serif;\n"
"font-size: 20px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"background-color: transparent;")
        self.Role.setObjectName("Role")
        self.Class = QtWidgets.QLabel(parent=self.StudentCard)
        self.Class.setGeometry(QtCore.QRect(10, 400, 291, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(False)
        self.Class.setFont(font)
        self.Class.setStyleSheet("font-family: \"Arial\", sans-serif;\n"
"font-size: 20px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"background-color: transparent;")
        self.Class.setObjectName("Class")
        self.ID = QtWidgets.QLabel(parent=self.StudentCard)
        self.ID.setGeometry(QtCore.QRect(90, 450, 31, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        self.ID.setFont(font)
        self.ID.setStyleSheet("font-family: \"Arial\", sans-serif;\n"
"font-size: 18px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.ID.setObjectName("ID")
        self.ID2 = QtWidgets.QLabel(parent=self.StudentCard)
        self.ID2.setGeometry(QtCore.QRect(140, 450, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        self.ID2.setFont(font)
        self.ID2.setStyleSheet("font-family: \"Arial\", sans-serif;\n"
"font-size: 18px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.ID2.setObjectName("ID2")
        self.Line = QtWidgets.QLabel(parent=self.StudentCard)
        self.Line.setGeometry(QtCore.QRect(90, 430, 181, 3))
        self.Line.setStyleSheet("background-color: rgb(95, 94, 124);")
        self.Line.setText("")
        self.Line.setObjectName("Line")
        self.Avatar = QtWidgets.QLabel(parent=self.StudentCard)
        self.Avatar.setGeometry(QtCore.QRect(60, 120, 191, 181))
        self.Avatar.setStyleSheet("background-color: transparent;\n"
"color: rgb(229, 229, 229);")
        self.Avatar.setText("")
        self.Avatar.setObjectName("Avatar")
        self.BorderStudentCard = QtWidgets.QLabel(parent=self.StudentCard)
        self.BorderStudentCard.setGeometry(QtCore.QRect(10, 10, 311, 511))
        self.BorderStudentCard.setStyleSheet("background-color: transparent;\n"
"border: 3px solid rgb(51, 50, 89);\n"
"border-radius: 20px;\n"
"")
        self.BorderStudentCard.setText("")
        self.BorderStudentCard.setObjectName("BorderStudentCard")
        self.BorderAvatar = QtWidgets.QLabel(parent=self.StudentCard)
        self.BorderAvatar.setGeometry(QtCore.QRect(60, 60, 211, 241))
        self.BorderAvatar.setStyleSheet("background-color: transparent;\n"
"border: 3px solid rgb(51, 50, 89);\n"
"border-radius: 20px;\n"
"")
        self.BorderAvatar.setText("")
        self.BorderAvatar.setObjectName("BorderAvatar")
        self.BorderStudentCard.raise_()
        self.School.raise_()
        self.Name.raise_()
        self.Role.raise_()
        self.Class.raise_()
        self.ID.raise_()
        self.ID2.raise_()
        self.Line.raise_()
        self.Avatar.raise_()
        self.BorderAvatar.raise_()
        self.Header = QtWidgets.QFrame(parent=self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(0, 0, 1280, 70))
        self.Header.setStyleSheet("")
        self.Header.setObjectName("Header")
        self.NameSW = QtWidgets.QLabel(parent=self.Header)
        self.NameSW.setGeometry(QtCore.QRect(110, 30, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        self.NameSW.setFont(font)
        self.NameSW.setStyleSheet("font-family: \"Roboto\", sans-serif;\n"
"font-size: 30px;\n"
"font-weight: bold;\n"
"text-algin: left;\n"
"background-color: transparent;")
        self.NameSW.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.NameSW.setObjectName("NameSW")
        self.HeaderBackground = QtWidgets.QLabel(parent=self.Header)
        self.HeaderBackground.setGeometry(QtCore.QRect(-20, 0, 1301, 71))
        self.HeaderBackground.setStyleSheet("background-color: rgb(165,213,255);")
        self.HeaderBackground.setText("")
        self.HeaderBackground.setScaledContents(True)
        self.HeaderBackground.setObjectName("HeaderBackground")
        self.label = QtWidgets.QLabel(parent=self.Header)
        self.label.setGeometry(QtCore.QRect(50, 10, 51, 51))
        self.label.setStyleSheet("background-color: transparent;")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Interface\Png\Icon\logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.HeaderBackground.raise_()
        self.NameSW.raise_()
        self.label.raise_()
        self.OtherButton = QtWidgets.QFrame(parent=self.centralwidget)
        self.OtherButton.setGeometry(QtCore.QRect(949, 599, 331, 121))
        self.OtherButton.setObjectName("OtherButton")
        self.HelpButton = QtWidgets.QPushButton(parent=self.OtherButton)
        self.HelpButton.setGeometry(QtCore.QRect(140, 20, 70, 70))
        self.HelpButton.setAutoFillBackground(False)
        self.HelpButton.setStyleSheet("border: none;")
        self.HelpButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Interface/Png/Icon/Help.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.HelpButton.setIcon(icon1)
        self.HelpButton.setIconSize(QtCore.QSize(50, 50))
        self.HelpButton.setObjectName("HelpButton")
        self.NewButton = QtWidgets.QPushButton(parent=self.OtherButton)
        self.NewButton.setGeometry(QtCore.QRect(60, 30, 50, 50))
        self.NewButton.setAutoFillBackground(False)
        self.NewButton.setStyleSheet("border: none;")
        self.NewButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Interface/Png/Icon/New.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.NewButton.setIcon(icon2)
        self.NewButton.setIconSize(QtCore.QSize(50, 50))
        self.NewButton.setObjectName("NewButton")
        self.Help = QtWidgets.QLabel(parent=self.OtherButton)
        self.Help.setGeometry(QtCore.QRect(150, 80, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Help.setFont(font)
        self.Help.setStyleSheet("font-family: \"Arial\", sans-serif;\n"
"font-size: 18px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.Help.setObjectName("Help")
        self.New = QtWidgets.QLabel(parent=self.OtherButton)
        self.New.setGeometry(QtCore.QRect(60, 80, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.New.setFont(font)
        self.New.setStyleSheet("font-family: \"Arial\", sans-serif;\n"
"font-size: 18px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.New.setObjectName("New")
        self.ExitButton = QtWidgets.QPushButton(parent=self.OtherButton)
        self.ExitButton.setGeometry(QtCore.QRect(230, 20, 70, 70))
        self.ExitButton.setAutoFillBackground(False)
        self.ExitButton.setStyleSheet("border: none;")
        self.ExitButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Interface/Png/Icon/logout.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.ExitButton.setIcon(icon3)
        self.ExitButton.setIconSize(QtCore.QSize(50, 50))
        self.ExitButton.setObjectName("ExitButton")
        self.Exit = QtWidgets.QLabel(parent=self.OtherButton)
        self.Exit.setGeometry(QtCore.QRect(230, 80, 55, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.Exit.setFont(font)
        self.Exit.setStyleSheet("font-family: \"Arial\", sans-serif;\n"
"font-size: 18px;\n"
"qproperty-alignment: \'AlignVCenter | AlignHCenter\';\n"
"font-weight: bold;\n"
"background-color: transparent;")
        self.Exit.setObjectName("Exit")
        FaceRecognition.setCentralWidget(self.centralwidget)

        self.retranslateUi(FaceRecognition)
        QtCore.QMetaObject.connectSlotsByName(FaceRecognition)
    
    def retranslateUi(self, FaceRecognition):
        global _translate 
        _translate = QtCore.QCoreApplication.translate
        FaceRecognition.setWindowTitle(_translate("FaceRecognition", "Homepage"))
        self.School.setText(_translate("FaceRecognition", "UIT"))
        self.Name.setText(_translate("FaceRecognition", "NAME"))
        self.Role.setText(_translate("FaceRecognition", "FACULTY"))
        self.Class.setText(_translate("FaceRecognition", "CLASS"))
        self.ID.setText(_translate("FaceRecognition", "ID"))
        self.ID2.setText(_translate("FaceRecognition", "123 456 789"))
        self.NameSW.setText(_translate("FaceRecognition", "Face Recognition"))
        self.Help.setText(_translate("FaceRecognition", "Help"))
        self.New.setText(_translate("FaceRecognition", "New"))
        self.Exit.setText(_translate("FaceRecognition", "Exit"))


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_FaceRecognition()
        self.ui.setupUi(self)
        self.start_camera()
        self.load_user_id()
        
        # Khởi tạo socket và kết nối tới server
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = '10.20.3.243'  # Change this to your server IP
        self.port = 9999
        self.client_socket.connect((self.host_ip, self.port))

        self.client_socket.sendto(self.message,(self.host_ip,self.port))

        # Connect the "New" button click event to open_register_file function
        self.ui.NewButton.clicked.connect(self.open_register_file)
        self.ui.ExitButton.clicked.connect(self.open_login_file)
        self.ui.HelpButton.clicked.connect(self.open_help_file)

    def open_register_file(self):
        try:
            # Run register.py file using subprocess
            subprocess.Popen(["python", r"Interface\Students\Register\main.py"])
            self.close()
        except Exception as e:
            print("Error opening register file:", e)
            
    def open_login_file(self):
        try:
                # Xóa biến môi trường USER_ID nếu nó tồn tại
                if 'USER_ID' in os.environ:
                        del os.environ['USER_ID']
                
                # Chạy file login_ui.py bằng subprocess
                subprocess.Popen(["python", r"Interface\Login\login_main.py"])
                self.close()
        except Exception as e:
                print("Error opening login file:", e)
                
    def open_help_file(self):
        try:
            # Run register.py file using subprocess
            subprocess.Popen(["python", r"Interface\Students\Home\helppage.py"])
        except Exception as e:
            print("Error opening help file:", e)

    def start_camera(self):
        # Start the camera
        self.vid = cv2.VideoCapture(0)
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.timer.start(10)  # Update frame every 10 milliseconds

    def update_frame(self):
        # Capture frame-by-frame
        global frame
        ret, frame = self.vid.read()

        # Convert frame to RGB format
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert frame to QImage
        height, width, channel = frame_rgb.shape
        bytes_per_line = 3 * width
        q_img = QtGui.QImage(frame_rgb.data, width, height, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
        
        # Set the QImage to the QLabel for display
        self.ui.BorderCamera_2.setPixmap(QtGui.QPixmap.fromImage(q_img))

        # global found
        # if found:
                # Send frame over socket
        if self.client_socket.fileno() != -1:
            # Send frame over socket
                try:
                        a = pickle.dumps((found,frame))
                        message = struct.pack("Q", len(a)) + a
                        self.client_socket.sendall(message)

                except Exception as e:
                        print("Error sending frame:", e)
                        QtWidgets.QMessageBox.critical(self, "Error", "Error sending frame. Application will be closed.")
                        self.client_socket.close()
                        QtCore.QCoreApplication.instance().quit()

    def closeEvent(self, event):
        self.client_socket.close()
        event.accept()
        

    def update_student_card_image(self, student_id):
        # Reference to the images in Firebase
        image_ref = storage.bucket().get_blob(f"images/{student_id}.jpg")
        
        # Download image from Firebase

        if image_ref:
                image_data = image_ref.download_as_bytes()

                # Convert bytes data to OpenCV image format
                nparr = np.frombuffer(image_data, np.uint8)
                image_cv2 = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

                image_rgb = cv2.cvtColor(image_cv2, cv2.COLOR_BGR2RGB)
                # Resize image to fit BorderAvatar
                resized_image = cv2.resize(image_rgb, (self.ui.BorderAvatar.width(), self.ui.BorderAvatar.height()))

                # Convert OpenCV image to QImage
                height, width, channel = resized_image.shape
                bytes_per_line = 3 * width
                q_img = QtGui.QImage(resized_image.data, width, height, bytes_per_line, QtGui.QImage.Format.Format_RGB888)

                # Display image on BorderAvatar
                self.ui.BorderAvatar.setPixmap(QtGui.QPixmap.fromImage(q_img))
        else:
                # If image not found, display a default image or clear the QLabel
                self.ui.BorderAvatar.clear()  # Clear the QLabel


    def keyPressEvent(self, event):
        # Check if the Enter key is pressed
        if event.key() == QtCore.Qt.Key.Key_Return or event.key() == QtCore.Qt.Key.Key_Enter: 

            ## Check if spoofed
            _, img_encoded = cv2.imencode('.jpg', frame)
            img_bytes = img_encoded.tobytes()

            response = requests.post('https://face-attendance.azurewebsites.net/anti_spoofing', files={'image':img_bytes})
            response_data = response.json()
            label = response_data.get('label')
            
            if label == 1:
                global user_id
                if user_id:
                    try:
                        database = {}
                        studentInfo = db.reference(f"Students/{user_id}").get()
                        studentName = studentInfo["Name"]
                        studentEmbedding = studentInfo["embeddings"]
                        database[studentName] = studentEmbedding
                        faces = match_with_database(frame, database)
                        if faces == 1:
                            global found
                            found = user_id

                            date = str(datetime.now().replace(microsecond=0))
                            # Lấy dữ liệu từ Firebase
                            class_data = studentInfo["Classes"]

                            dialog = ClassSelectionDialog(class_data)
                            date_check = DateCheckDialog()
                            if dialog.exec() == QDialog.DialogCode.Accepted:
                                selected_class = dialog.selected_class()
                                if not date_check.check_attendance_today(user_id, selected_class):
                                    self.ui.ID2.setText(_translate("FaceRecognition", user_id))
                                    self.ui.Name.setText(_translate("FaceRecognition", studentName))
                                    self.ui.Role.setText(_translate("FaceRecognition", studentInfo["Faculty"]))
                                    self.ui.Class.setText(_translate("FaceRecognition", selected_class))   
                                    self.update_student_card_image(user_id)

                                    ## Ghi chú điểm danh
                                    res = db.reference(f"Students/{user_id}/Classes/{selected_class}")
                                    count = res.child("AttendanceCount").get()
                                    res.update({"AttendanceCount": int(count) + 1,
                                                "Datetime": date})
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Icon.Critical)
                            msg.setText("Điểm danh không thành công. Vui lòng thử lại.")
                            msg.setWindowTitle("Thông báo")
                            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                            
                            # Hiển thị dialog box cảnh báo
                            msg.exec()
                    except:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Icon.Critical)
                        msg.setText("Vui lòng đăng kí khuôn mặt để điểm danh")
                        msg.setWindowTitle("Thông báo")
                        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                        
                        # Hiển thị dialog box cảnh báo
                        msg.exec()

                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Icon.Critical)
                    msg.setText("Không tìm thấy user_id. Vui lòng đăng nhập trước.")
                    msg.setWindowTitle("Thông báo")
                    msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                    
                    # Hiển thị dialog box cảnh báo
                    msg.exec()
            else:
                # Tạo một QMessageBox cảnh báo
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Vui lòng không sử dụng hình ảnh để gian lận trong việc điểm danh!!")
                msg.setWindowTitle("Cảnh báo")
                msg.setStandardButtons(QMessageBox.StandardButton.Ok)
                
                # Hiển thị dialog box cảnh báo
                msg.exec()

                        
    def load_user_id(self):
        global user_id
        user_id = os.getenv('USER_ID')
        if not user_id:
            print("No user_id found. Please log in first.")
            sys.exit()
        else:
            print("Logged in user:", user_id)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()       
    window.show()
    sys.exit(app.exec())