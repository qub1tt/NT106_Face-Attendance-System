import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from PyQt6 import QtCore, QtGui, QtWidgets
from openpyxl import Workbook
import sys

# Khởi tạo Firebase với tệp JSON chứa khóa xác thực
cred = credentials.Certificate("ServiceAccountKey.json")

firebase_admin.initialize_app(cred, {
    "databaseURL":"https://faceregconition-80c55-default-rtdb.firebaseio.com/",
    "storageBucket":"faceregconition-80c55.appspot.com"
})

# Lấy reference đến nút "Students" trong Firebase Realtime Database
class_ref = db.reference('Classes')

# Lấy dữ liệu từ Firebase
class_data = class_ref.get()

# Lấy reference đến nút "Students" trong Firebase Realtime Database
students_ref = db.reference('Students')

# Lấy dữ liệu từ Firebase
s1 = students_ref.get()
student_data = {}

class Ui_StudentManagement(object):
    def setupUi(self, StudentManagement):
        StudentManagement.setObjectName("StudentManagement")
        StudentManagement.resize(1272, 680)
        self.centralwidget = QtWidgets.QWidget(parent=StudentManagement)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1281, 631))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        self.result_frame = QtWidgets.QFrame(parent=self.widget)
        self.result_frame.setGeometry(QtCore.QRect(30, 120, 1211, 481))
        self.result_frame.setStyleSheet("")
        self.result_frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.result_frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.result_frame.setObjectName("result_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.result_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.result_frame)
        self.tableWidget.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        self.tableWidget.setStyleSheet("")
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setColumnWidth(0, 100)
        self.tableWidget.setColumnWidth(1, 180)
        self.tableWidget.setColumnWidth(2, 180)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.btn_frame = QtWidgets.QFrame(parent=self.widget)
        self.read_btn = QtWidgets.QPushButton(parent=self.btn_frame)
        self.read_btn.setGeometry(QtCore.QRect(210, 20, 111, 41))
        self.read_btn.setStyleSheet("")
        self.read_btn.setObjectName("read_btn")
        self.read_btn = QtWidgets.QPushButton(parent=self.btn_frame)
        self.read_btn.setGeometry(QtCore.QRect(210, 20, 111, 41))
        self.read_btn.setStyleSheet("")
        self.read_btn.setObjectName("read_btn")
        
        StudentManagement.setCentralWidget(self.centralwidget)
        self.retranslateUi(StudentManagement)
        QtCore.QMetaObject.connectSlotsByName(StudentManagement)

    def retranslateUi(self, StudentManagement):
        _translate = QtCore.QCoreApplication.translate
        StudentManagement.setWindowTitle(_translate("StudentManagement", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("StudentManagement", "StudentID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("StudentManagement", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("StudentManagement", "Email"))
        self.read_btn.setText(_translate("StudentManagement", "search"))
        self.read_btn.clicked.connect(self.search_data)
        

    
    def search_data(self):
        if class_data:
            class_names = list(class_data.keys())
            # Hiển thị dialog tìm kiếm và chọn lớp
            search_dialog = SearchDialog(class_names)
            if search_dialog.exec():
                selected_class = search_dialog.get_selected_class()
                
                if selected_class:
                    if selected_class in class_names:
                        # Lọc dữ liệu sinh viên dựa trên lớp đã chọn
                        self.tableWidget.clearContents()
                        self.tableWidget.setRowCount(0)
                    else:
                        qmb_custom("No Classes", "No classes found, please try again later.")
        else:
            qmb_custom("No Classes", "No classes found, please try again later.")
        
    def filter_student_data(self, selected_class):
        student_data.clear()
        if s1:
            for student_id, student_info in s1.items():
                classes = student_info.get("Classes", {})
                if selected_class in classes:
                    student_data[student_id] = student_info
        self.load_data()



    # def load_data(self):
    #     response = requests.get("http://127.0.0.1:5000/students")
        #if response.status_code == 200:
            #student_data = response.json()
            # if student_data:
            #     self.tableWidget.setRowCount(len(student_data))
            #     row = 0
            #     for student_id, student_info in student_data.items():
            #         self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student_id))
            #         self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student_info.get("Name", "")))
            #         self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student_info.get("Email", "")))
            #         row += 1    

def qmb_custom(string1, string2):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle(string1)
    msg_box.setText(string2)
    # Thiết lập StyleSheet để căn giữa văn bản
    msg_box.setStyleSheet(
        "QLabel{font-size: 20px; min-height:150 px; min-width: 400px;} QPushButton{ width:100px; height:30px; border-radius: 5px; font-size: 15px; background-color: rgb(165, 213, 255);} QPushButton:hover{background-color: rgb(3, 105, 161); color: rgb(255,255,255);}"
        )
    msg_box.exec()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    StudentManagement = QtWidgets.QMainWindow()
    ui = Ui_StudentManagement()
    ui.setupUi(StudentManagement)
    StudentManagement.show()
    sys.exit(app.exec())
