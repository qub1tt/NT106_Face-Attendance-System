import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from PyQt6 import QtCore, QtGui, QtWidgets
from openpyxl import Workbook
import datetime

from Attendance import Ui_StudentManagement


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

class SearchDialog(QtWidgets.QDialog):
    def __init__(self, class_names):
        super().__init__()

        # Lưu danh sách tên lớp vào thuộc tính của lớp
        self.class_names = class_names

        # Thiết lập tiêu đề của cửa sổ
        self.setWindowTitle("Select Class")
        
        self.setFixedSize(445, 225)

        # Tạo layout chính của cửa sổ
        main_layout = QtWidgets.QVBoxLayout()

        # Layout chứa ô nhập và combo box
        search_layout = QtWidgets.QHBoxLayout()
        self.search_input = QtWidgets.QLineEdit()  # Ô nhập văn bản
        self.search_input.setFixedSize(250, 35)

        # Tạo Completer và đặt cài đặt cho Completer
        self.completer = QtWidgets.QCompleter(class_names)
        self.completer.setCaseSensitivity(QtCore.Qt.CaseSensitivity.CaseInsensitive)  # Đảm bảo không phân biệt chữ hoa, chữ thường
        self.search_input.setCompleter(self.completer)

        self.search_input.setPlaceholderText("Enter class name")  # Placeholder cho ô nhập

        search_layout.addWidget(self.search_input)

        self.class_combo = QtWidgets.QComboBox()  # Combo box
        self.class_combo.setFixedSize(100, 35)
        self.class_combo.addItem("Select Class")
        self.class_combo.addItems(class_names)  # Thêm các tên lớp vào combo box
        search_layout.addWidget(self.class_combo)

        # Thêm các layout vào layout chính
        main_layout.addLayout(search_layout)
        
        # Layout chứa nút OK
        button_layout = QtWidgets.QHBoxLayout()
        self.ok_button = QtWidgets.QPushButton("OK")
        self.ok_button.clicked.connect(self.accept)
        self.ok_button.setFixedSize(100, 30)  # Đặt kích thước cố định cho nút OK
        button_layout.addWidget(self.ok_button)

        # Thiết lập layout chính cho cửa sổ
        main_layout.addLayout(button_layout)
        self.setLayout(main_layout)

        # Kết nối tín hiệu của combo box với hàm cập nhật ô nhập
        self.class_combo.currentIndexChanged.connect(self.update_search_input)

        # Thêm bộ lọc tùy chỉnh cho Completer
        self.completer.setFilterMode(QtCore.Qt.MatchFlag.MatchContains)
        self.search_input.textChanged.connect(self.filter_completion)
        
        self.setStyleSheet(
            "QPushButton{min-width:100px; height:30px; border-radius: 5px; font-size: 15px; background-color: rgb(165, 213, 255);} QPushButton:hover{background-color: rgb(3, 105, 161); color: rgb(255,255,255);} QLineEdit{width:250px; height: 35px;font-size: 15px; padding-left: 5px; border: 1px solid black; border-radius: 5px} QCompleter{font-size: 15px} QComboBox{padding-left: 5px;  height: 35px; font-size: 15px;}"
            )

    # Hàm cập nhật ô nhập khi chọn một lớp từ combo box
    def update_search_input(self, index):
        if index > 0:
            self.search_input.setText(self.class_combo.currentText())
        else:
            self.search_input.setText(None)


    # Hàm trả về lớp được chọn
    def get_selected_class(self):
        if self.search_input.text():
            return self.search_input.text()
        else:
            return self.class_combo.currentText()

    # Hàm lọc gợi ý dựa trên chuỗi nhập của người dùng
    def filter_completion(self, text):
        filtered_class_names = [name for name in self.class_names if text.lower() in name.lower()]
        model = QtCore.QStringListModel(filtered_class_names)
        self.completer.setModel(model)


class Ui_StudentManagementFunctionality(Ui_StudentManagement):
    def __init__(self, StudentManagement):
        super().__init__()
        self.setupUi(StudentManagement)
        
    def on_window_resized(self, event):
        # Lấy kích thước mới của cửa sổ
        window_size = event.size()

        # Cập nhật kích thước và vị trí của các thành phần
        self.centralwidget.setGeometry(0, 0, window_size.width(), window_size.height())
        self.Header.setGeometry(0, 0, window_size.width(), 71)
        self.widget.setGeometry(0, 71, window_size.width(), window_size.height() - 71)
        self.result_frame.setGeometry(30, 120, window_size.width() - 60, window_size.height() - 191)
        self.btn_frame.setGeometry(30, 20, window_size.width() - 60, 80)

    def select_class(self):
        if class_data:
            class_names = list(class_data.keys())
            # Hiển thị dialog tìm kiếm và chọn lớp
            search_dialog = SearchDialog(class_names)
            if search_dialog.exec():
                selected_class = search_dialog.get_selected_class()
                
                if selected_class:
                    if selected_class in class_names:
                        self.label_class.setText("Class: " + selected_class)
                        font = QtGui.QFont()
                        font.setPointSize(20)
                        font.setBold(True)
                        self.label_class.setFont(font)
                        # Lọc dữ liệu sinh viên dựa trên lớp đã chọn
                        self.tableWidget.clearContents()
                        self.tableWidget.setRowCount(0)
                        self.filter_student_data(selected_class)
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
        
    def load_data(self):
        if student_data:
            self.tableWidget.setRowCount(len(student_data))
            row = 0
            for student_id, student_info in student_data.items():
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student_id))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student_info.get("Name", "")))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student_info.get("Email", "")))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(student_info.get("Faculty", "")))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(student_info.get("Major", "")))
                year_str = str(student_info.get("Year", ""))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(year_str))
                
                row += 1
            set_read_only_flags(self.tableWidget)
        else:
            qmb_custom("Warning", "Please select a class.")

    def checked_data(self):
        student_data_copy = dict(student_data)
        a = student_data_copy
        a1 = {}

        if a:
            selected_class_name = self.label_class.text().split(": ")[1]
            selected_class_students = [student_id for student_id, student_info in a.items() if selected_class_name in student_info.get("Classes", [])]
            self.tableWidget.setRowCount(len(selected_class_students))

            current_date = datetime.datetime.now().date()  # Lấy ngày hiện tại ở ngoài vòng lặp
            current_date_str = str(current_date)  # Chuyển đổi thành chuỗi để so sánh

            for row, student_id in enumerate(selected_class_students):
                student_info = a.get(student_id)
                if student_info:
                    datetime_in_database = student_info.get("Classes", {}).get(selected_class_name, {}).get("Datetime", 0)
                    datetime_in_database = str(datetime_in_database)
                    database_date = datetime_in_database[:10]
                    checked_today = current_date_str == database_date

                    if checked_today:
                        a1[student_id] = student_info

            self.tableWidget.setRowCount(len(a1))

            for row, (student_id, student_info) in enumerate(a1.items()):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student_id))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student_info.get("Name", "")))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student_info.get("Email", "")))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(student_info.get("Faculty", "")))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(student_info.get("Major", "")))
                year_str = str(student_info.get("Year", ""))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(year_str))
                attendance_count = student_info.get("Classes", {}).get(selected_class_name, {}).get("Datetime", 0)
                points_item = QtWidgets.QTableWidgetItem(str(attendance_count))
                self.tableWidget.setItem(row, 6, points_item)
                set_read_only_flags(self.tableWidget)
        else:
            qmb_custom("Warning", "Please select a class.")



    def unchecked_data(self):
        student_data_copy = dict(student_data)
        b = student_data_copy
        b1 = {}

        if b:
            selected_class_name = self.label_class.text().split(": ")[1]

            selected_class_students = [student_id for student_id, student_info in b.items() if selected_class_name in student_info.get("Classes", [])]

            self.tableWidget.setRowCount(len(selected_class_students))
            current_date = datetime.datetime.now().date()  # Lấy ngày hiện tại ở ngoài vòng lặp
            current_date = str(current_date)  # Chuyển đổi thành chuỗi để so sánh

            for row, student_id in enumerate(selected_class_students):
                student_info = b.get(student_id)
                if student_info:
                    datetime_in_database = student_info.get("Classes", {}).get(selected_class_name, {}).get("Datetime", 0)
                    datetime_in_database = str(datetime_in_database)
                    database_date = datetime_in_database[:10]
                    checked_today = current_date == database_date

                    if not checked_today:
                        b1[student_id] = student_info

            self.tableWidget.setRowCount(len(b1))

            for row, (student_id, student_info) in enumerate(b1.items()):
                self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(student_id))
                self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(student_info.get("Name", "")))
                self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(student_info.get("Email", "")))
                self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(student_info.get("Faculty", "")))
                self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(student_info.get("Major", "")))
                year_str = str(student_info.get("Year", ""))
                self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(year_str))
                attendance_count = student_info.get("Classes", {}).get(selected_class_name, {}).get("Datetime", 0)
                points_item = QtWidgets.QTableWidgetItem(str(attendance_count))
                self.tableWidget.setItem(row, 6, points_item)
                set_read_only_flags(self.tableWidget)
        else:
            # Hiển thị cảnh báo nếu không có lớp nào được chọn
            qmb_custom("Warning", "Please select a class.")

    
            
def set_read_only_flags(table_widget):
    for row in range(table_widget.rowCount()):
        for column in range(table_widget.columnCount()):
            item = table_widget.item(row, column)
            if item:
                item.setFlags(QtCore.Qt.ItemFlag.ItemIsEnabled)

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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StudentManagement = QtWidgets.QMainWindow()
    ui = Ui_StudentManagementFunctionality(StudentManagement)
    StudentManagement.show()
    sys.exit(app.exec())