from PyQt6 import QtCore, QtGui, QtWidgets
import socket
import cv2
import pickle
import struct
import threading
import sys
import pyshine as ps


class Ui_CheckCamera(object):
    def setupUi(self,CheckCamera):
        CheckCamera.setObjectName("CheckCamera")
        CheckCamera.resize(1272, 680)
        CheckCamera.setStyleSheet("#CheckCamera{\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"#Header {\n"
"    background-color: rgb(165, 213, 255);\n"
"}\n"
"\n"
"#Header #Logo{\n"
"    image: url(:/Pic/logo.png);\n"
"    border: none;\n"
"}\n"
"\n"
"#Header #NameSW{\n"
"    font-family: \"Robotol\", sans-serif;\n"
"    font-size: 25px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"#result_frame {\n"
"    border-radius: 10px;\n"
"    border: 1px solid black;\n"
"    background-color: #fff;\n"
"}\n"
"\n"
"\n"
"QHeaderView::section {\n"
"    border: none;\n"
"    border-bottom: 1px solid black;\n"
"    padding: 3px 5px;\n"
"}\n"
"\n"
"\n"
"#btn_frame {\n"
"    border: 1px solid black;\n"
"    border-radius: 10px;\n"
"    background-color: rgb(255,255,255);\n"
"}\n"
"\n"
"#btn_frame QPushButton{\n"
"    background-color: #a5d5ff;\n"
"    border-radius: 10px;\n"
"}\n"
"\n"
"#btn_frame QPushButton:hover{\n"
"    background-color: rgb(3, 105, 161); /* Màu nền mới khi hover */\n"
"    border-color: rgb(65, 173, 255);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"#scroll_area{\n"
"    background-color: rgb(255, 255, 255);"
"}\n"
"#scroll_area_widget{\n"
"    background-color: rgb(255, 255, 255);"
"}\n"
"#scroll_area_layout{\n"
"    background-color: white;"
"}\n"
"\n"
"")          
        
        self.centralwidget = QtWidgets.QWidget(parent=CheckCamera)
        self.centralwidget.setObjectName("centralwidget")
        
        self.Header = QtWidgets.QFrame(parent=self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(0, 0, 1281, 71))
        self.Header.setStyleSheet("")
        self.Header.setObjectName("Header")
        self.NameSW = QtWidgets.QLabel(parent=self.Header)
        self.NameSW.setGeometry(QtCore.QRect(30, 20, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Robotol")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.NameSW.setFont(font)
        self.NameSW.setStyleSheet("")
        self.NameSW.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.NameSW.setObjectName("NameSW")
        self.label_class = QtWidgets.QLabel(parent=self.Header)
        self.label_class.setGeometry(QtCore.QRect(680, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Robotol")
        font.setBold(True)
        font.setWeight(75)
        self.label_class.setFont(font)
        self.label_class.setStyleSheet("")
        self.label_class.setText("")
        self.label_class.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom|QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_class.setObjectName("label_class")
        self.widget = QtWidgets.QWidget(parent=self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 70, 1281, 631))
        self.widget.setStyleSheet("")
        self.widget.setObjectName("widget")
        
        # Create a scroll area to hold multiple client video widgets
        self.scroll_area = QtWidgets.QScrollArea(parent=self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(30, 80, 1211, 600))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background-color: white; border: 1px solid black;")
        
        self.scroll_area_widget = QtWidgets.QWidget()
        self.scroll_area_layout = QtWidgets.QGridLayout(self.scroll_area_widget)
        self.scroll_area.setWidget(self.scroll_area_widget)
        
        # Divide the window into a 3x3 grid
        for i in range(3):
            for j in range(4):
                frame = QtWidgets.QFrame()
                frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
                self.scroll_area_layout.addWidget(frame, i, j)
                
        CheckCamera.setCentralWidget(self.centralwidget)
        self.retranslateUi(CheckCamera)
        QtCore.QMetaObject.connectSlotsByName(CheckCamera)
        CheckCamera.resizeEvent = self.on_window_resized
        
    def retranslateUi(self, CheckCamera):
        _translate = QtCore.QCoreApplication.translate
        CheckCamera.setWindowTitle(_translate("CheckCamera", "CheckCamera"))
        self.NameSW.setText(_translate("CheckCamera", "STUDENT CAMERA"))
        
    def on_window_resized(self, event):
        # Lấy kích thước mới của cửa sổ
        window_size = event.size()

        # Cập nhật kích thước và vị trí của các thành phần
        self.centralwidget.setGeometry(0, 0, window_size.width(), window_size.height())
        self.Header.setGeometry(0, 0, window_size.width(), 71)
        self.widget.setGeometry(0, 71, window_size.width(), window_size.height() - 71)
        self.scroll_area.setGeometry(30, 100, window_size.width() - 60, window_size.height() - 120)


class ClientVideoWidget(QtWidgets.QWidget):
    def __init__(self, client_id):
        super().__init__()
        self.client_id = client_id
        self.setFixedSize(350, 230)
        self.layout = QtWidgets.QVBoxLayout(self)  # Vertical layout to stack elements vertically
        self.video_label = QtWidgets.QLabel(self)
        self.video_label.setFixedSize(340, 220)
        self.video_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.video_label)
        self.setLayout(self.layout)

    def update_image(self, q_img):
        resized_q_img = q_img.scaled(self.video_label.size(), QtCore.Qt.AspectRatioMode.KeepAspectRatio, QtCore.Qt.TransformationMode.SmoothTransformation)
        self.video_label.setPixmap(QtGui.QPixmap.fromImage(resized_q_img))


class VideoServer(QtCore.QObject):
    update_frame = QtCore.pyqtSignal(str, QtGui.QImage)
    client_disconnected = QtCore.pyqtSignal(str)  # New signal for client disconnection

    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host_ip = "10.20.7.190"
        self.port = 9999
        self.server_socket.bind((self.host_ip, self.port))
        self.server_socket.listen()
        print("Listening at", (self.host_ip, self.port))

    def start(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            thread = threading.Thread(target=self.show_client, args=(addr, client_socket))
            thread.start()
            print("\nTOTAL CLIENTS:", threading.active_count() - 2)

    def show_client(self, addr, client_socket):
        try:
            print('CLIENT {} CONNECTED!'.format(addr))
            if client_socket:
                data = b""
                payload_size = struct.calcsize("Q")
                while True:
                    while len(data) < payload_size:
                        packet = client_socket.recv(4 * 1024)
                        if not packet:
                            break
                        data += packet
                    if not packet:
                        break
                    packed_msg_size = data[:payload_size]
                    data = data[payload_size:]
                    msg_size = struct.unpack("Q", packed_msg_size)[0]
                    while len(data) < msg_size:
                        data += client_socket.recv(4 * 1024)
                    frame_data = data[:msg_size]
                    data = data[msg_size:]
                    student_id, frame = pickle.loads(frame_data)
                    text = f"CLIENT: {student_id}"
                    frame = ps.putBText(frame, text, 10, 10, vspace=10, hspace=1, font_scale=0.7,
                                        background_RGB=(255, 0, 0), text_RGB=(255, 250, 250))
                    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    height, width, channel = frame_rgb.shape
                    bytes_per_line = 3 * width
                    q_img = QtGui.QImage(frame_rgb.data, width, height, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
                    self.update_frame.emit(student_id, q_img)
            print(f"CLIENT {addr} DISCONNECTED")
            self.client_disconnected.emit(student_id)  # Emit signal when client disconnects
            client_socket.close()

        except Exception as e:
            print(f"CLIENT {addr} DISCONNECTED:", e)
            self.client_disconnected.emit(student_id)  # Emit signal in case of exception
            client_socket.close()



class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CheckCamera()

        self.video_server  = VideoServer()
        self.video_server.update_frame.connect(self.update_image)
        self.video_server.client_disconnected.connect(self.remove_client_widget)

        self.server_thread = threading.Thread(target=self.video_server.start)
        self.server_thread.daemon = True
        self.server_thread.start()

        self.client_widgets = {}
        self.grid_positions = {}  # Store positions of client widgets
        self.max_rows = 3
        self.max_cols = 4
        self.next_position = (0, 0)

    def get_next_position(self):
        for row in range(self.max_rows):
            for col in range(self.max_cols):
                if (row, col) not in self.grid_positions:
                    return (row, col)
        return None

    def shift_widgets(self):
        positions = sorted(self.grid_positions.keys())
        for i in range(len(positions) - 1):
            cur_pos = positions[i]
            next_pos = positions[i + 1]
            widget = self.grid_positions.pop(next_pos)
            self.ui.scroll_area_layout.addWidget(widget, cur_pos[0], cur_pos[1], alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
            self.grid_positions[cur_pos] = widget

    @QtCore.pyqtSlot(str, QtGui.QImage)
    def update_image(self, client_id, q_img):
        if q_img is not None:
            if client_id not in self.client_widgets:
                position = self.get_next_position()
                if position is None:
                    print("No more space in the grid")
                    return
                client_widget = ClientVideoWidget(client_id)
                self.ui.scroll_area_layout.addWidget(client_widget, position[0], position[1], alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
                self.client_widgets[client_id] = client_widget
                self.grid_positions[position] = client_widget

            self.client_widgets[client_id].update_image(q_img)

    @QtCore.pyqtSlot(str)
    def remove_client_widget(self, client_id):
        if client_id in self.client_widgets:
            client_widget = self.client_widgets.pop(client_id)
            for pos, widget in self.grid_positions.items():
                if widget == client_widget:
                    del self.grid_positions[pos]
                    break
            self.ui.scroll_area_layout.removeWidget(client_widget)
            client_widget.deleteLater()
            self.shift_widgets()
            self.next_position = self.get_next_position()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())


