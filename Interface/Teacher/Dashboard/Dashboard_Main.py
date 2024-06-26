import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QGridLayout, QVBoxLayout, QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont
import socket
import cv2
import pickle
import struct
import base64
import time
import numpy as np
import threading
import sys
import pyshine as ps


# Import the UI class from the 'main_ui' module
from Dashboard_UI import Ui_MainWindow
from SM import Ui_StudentManagement
from AM import Ui_Attendance

class Ui_CheckCamera(object):
    def setupUi(self, CheckCamera):
        CheckCamera.setObjectName("CheckCamera")
        CheckCamera.resize(1272, 680)
        CheckCamera.setStyleSheet("""
            #CheckCamera {
                background-color: rgb(255, 255, 255);
            }
            #Header {
                background-color: rgb(165, 213, 255);
            }
            #Header #Logo {
                image: url(:/Pic/logo.png);
                border: none;
            }
            #Header #NameSW {
                font-family: "Roboto", sans-serif;
                font-size: 25px;
                font-weight: bold;
            }
            #result_frame {
                border-radius: 10px;
                border: 1px solid black;
                background-color: #fff;
            }
            QHeaderView::section {
                border: none;
                border-bottom: 1px solid black;
                padding: 3px 5px;
            }
            #btn_frame {
                border: 1px solid black;
                border-radius: 10px;
                background-color: rgb(255, 255, 255);
            }
            #btn_frame QPushButton {
                background-color: #a5d5ff;
                border-radius: 10px;
            }
            #btn_frame QPushButton:hover {
                background-color: rgb(3, 105, 161);
                border-color: rgb(65, 173, 255);
                color: rgb(255, 255, 255);
            }
            #scroll_area {
                background-color: rgb(255, 255, 255);
            }
            #scroll_area_widget {
                background-color: rgb(255, 255, 255);
            }
            #scroll_area_layout {
                background-color: white;
            }
        """)
        self.centralwidget = QtWidgets.QWidget(CheckCamera)
        self.centralwidget.setObjectName("centralwidget")

        self.Header = QtWidgets.QFrame(self.centralwidget)
        self.Header.setGeometry(QtCore.QRect(0, 0, 1281, 71))
        self.Header.setObjectName("Header")

        self.NameSW = QtWidgets.QLabel(self.Header)
        self.NameSW.setGeometry(QtCore.QRect(30, 20, 501, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.NameSW.setFont(font)
        self.NameSW.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.NameSW.setObjectName("NameSW")

        self.label_class = QtWidgets.QLabel(self.Header)
        self.label_class.setGeometry(QtCore.QRect(680, 20, 311, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(True)
        font.setWeight(75)
        self.label_class.setFont(font)
        self.label_class.setAlignment(QtCore.Qt.AlignmentFlag.AlignBottom | QtCore.Qt.AlignmentFlag.AlignLeading | QtCore.Qt.AlignmentFlag.AlignLeft)
        self.label_class.setObjectName("label_class")

        self.scroll_area = QtWidgets.QScrollArea(self.centralwidget)
        self.scroll_area.setGeometry(QtCore.QRect(30, 80, 1211, 600))
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setStyleSheet("background-color: white; border: 1px solid black;")

        self.scroll_area_widget = QtWidgets.QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)

        self.scroll_area_layout = QtWidgets.QGridLayout(self.scroll_area_widget)
        self.scroll_area_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_area_layout.setSpacing(10)

        # Create widgets and add them to the layout
        for i in range(3):
            for j in range(3):
                widget = QtWidgets.QWidget()
                widget.setMinimumSize(400, 300)  # Set minimum size for each widget
                self.scroll_area_layout.addWidget(widget, i, j)

        # Set the layout of the scroll area widget
        self.scroll_area_widget.setLayout(self.scroll_area_layout)

        CheckCamera.setCentralWidget(self.centralwidget)
        self.retranslateUi(CheckCamera)
        QtCore.QMetaObject.connectSlotsByName(CheckCamera)
        CheckCamera.resizeEvent = self.on_window_resized

    def retranslateUi(self, CheckCamera):
        _translate = QtCore.QCoreApplication.translate
        CheckCamera.setWindowTitle(_translate("CheckCamera", "CheckCamera"))
        self.NameSW.setText(_translate("CheckCamera", "STUDENT CAMERA"))

    def on_window_resized(self, event):
        window_size = event.size()
        self.centralwidget.setGeometry(0, 0, window_size.width(), window_size.height())
        self.Header.setGeometry(0, 0, window_size.width(), 71)
        self.scroll_area.setGeometry(30, 100, window_size.width() - 60, window_size.height() - 120)

BUFF_SIZE = 65536

class VideoStreamServer(QtCore.QObject):
    update_frame = QtCore.pyqtSignal(str, QtGui.QImage)
    client_disconnected = QtCore.pyqtSignal(str)

    def __init__(self, host_ip, port):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, BUFF_SIZE)
        self.server_socket.settimeout(5.0)  # Set timeout for receiving data
        self.host_ip = host_ip
        self.port = port
        self.socket_address = (self.host_ip, self.port)
        self.clients = {}  # Dictionary to store client information

    def start(self):
        self.server_socket.bind(self.socket_address)
        print('Server is listening at:', self.socket_address)
        self.accept_clients()

    def accept_clients(self):
        while True:
            try:
                packet, client_addr = self.server_socket.recvfrom(BUFF_SIZE)
                if client_addr not in self.clients:
                    print(f"Accepted connection from {client_addr}")
                    self.clients[client_addr] = True  # Mark the client as connected
                    client_thread = threading.Thread(target=self.handle_client, args=(client_addr,))
                    client_thread.start()
            except socket.timeout:
                continue  # Continue accepting clients even if no data is received

    def handle_client(self, client_addr):
        fps, st, frames_to_count, cnt = (0, 0, 20, 0)
        while self.clients.get(client_addr):
            try:
                packet, addr = self.server_socket.recvfrom(BUFF_SIZE)

                if addr != client_addr:
                    continue  # Ignore packets from other clients

                additional_string_encoded, data = packet.split(b'||')
                additional_string = base64.b64decode(additional_string_encoded).decode()
                npdata = np.frombuffer(base64.b64decode(data), dtype=np.uint8)
                frame = cv2.imdecode(npdata, 1)

                txt = f"client: {additional_string}"
                frame = cv2.putText(frame, 'FPS: ' + str(fps), (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                frame = cv2.putText(frame, txt, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                height, width, channel = frame_rgb.shape
                bytes_per_line = 3 * width
                q_img = QtGui.QImage(frame_rgb.data, width, height, bytes_per_line, QtGui.QImage.Format.Format_RGB888)
                self.update_frame.emit(txt, q_img)

                key = cv2.waitKey(1) & 0xFF
                if key == ord('q'):
                    self.clients[client_addr] = False
                    break
                if cnt == frames_to_count:
                    try:
                        fps = round(frames_to_count / (time.time() - st))
                        st = time.time()
                        cnt = 0
                    except ZeroDivisionError:
                        pass
                cnt += 1

            except socket.timeout:
                self.clients[client_addr] = False
                self.client_disconnected.emit(additional_string)
                break

        del self.clients[client_addr]
        self.client_disconnected.emit(additional_string)
        print(f"Connection with {client_addr} closed.")



class MyMainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CheckCamera()
        self.ui.setupUi(self)

        self.video_server = VideoStreamServer("10.20.7.190", 9999)
        self.video_server.update_frame.connect(self.update_image)
        self.video_server.client_disconnected.connect(self.remove_client_widget)

        self.server_thread = threading.Thread(target=self.video_server.start)
        self.server_thread.daemon = True
        self.server_thread.start()

        self.client_widgets = {}
        self.grid_positions = {}
        self.max_rows = 3
        self.max_cols = 3
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
    def update_image(self, client_id_with_prefix, q_img):
        client_id = client_id_with_prefix.split(': ')[-1]

        if q_img is not None:
            if client_id not in self.client_widgets:
                position = self.get_next_position()
                client_widget = ClientVideoWidget(client_id)
                self.ui.scroll_area_layout.addWidget(client_widget, position[0], position[1], alignment=QtCore.Qt.AlignmentFlag.AlignTop | QtCore.Qt.AlignmentFlag.AlignLeft)
                self.client_widgets[client_id] = client_widget
                self.grid_positions[position] = client_widget

            self.client_widgets[client_id].update_image(q_img)

    @QtCore.pyqtSlot(str)
    def remove_client_widget(self, client_id_with_prefix):
        client_id = client_id_with_prefix.split(': ')[-1]

        if client_id in self.client_widgets:
            client_widget = self.client_widgets.pop(client_id)
            
            self.ui.scroll_area_layout.removeWidget(client_widget)
            client_widget.deleteLater()  

            for pos, widget in list(self.grid_positions.items()):
                if widget == client_widget:
                    del self.grid_positions[pos]


class ClientVideoWidget(QtWidgets.QWidget):
    def __init__(self, client_id):
        super().__init__()
        self.client_id = client_id
        self.layout = QtWidgets.QVBoxLayout()
        self.setFixedSize(400, 300)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.image_label = QtWidgets.QLabel()
        self.image_label.setFixedSize(400, 280)
        self.layout.addWidget(self.image_label)
        self.setLayout(self.layout)

    def update_image(self, q_img):
        self.image_label.setPixmap(QtGui.QPixmap.fromImage(q_img))

    def clear_image(self):
        self.image_label.clear()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        

        # Initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setFixedSize(1550, 900)
        # Set window properties
        self.setWindowTitle("Teacher's UI")

        # Initialize UI elements
        self.title_label = self.ui.title_label
        self.title_label.setText("Dashboard")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        self.title_icon.setPixmap(QPixmap("Interface/Png/DashboardIcon/teacher.png"))
        self.title_icon.setScaledContents(True)

        self.side_menu = self.ui.listWidget
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only = self.ui.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only.hide()
        self.main_content = self.ui.stackedWidget

        # Define a list of menu items with names and icons
        self.menu_list = [
            {
                "name": "Menu",
                "icon": "Interface/Png/DashboardIcon/dashboard.svg"
            },
            {
                "name": "Student Management",
                "icon": "Interface/Png/DashboardIcon/customers.svg"
            },
            {
                "name": "Attendance Management",
                "icon": "Interface/Png/DashboardIcon/orders.svg"
            },
            {
                "name": "Check Camera",
                "icon": "Interface/Png/DashboardIcon/camera.svg"
            },
        ]

        # Initialize the UI elements and slots
        self.init_list_widget()
        self.init_stackwidget()
        self.init_single_slot()

    def init_single_slot(self):

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged['int'].connect(self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.side_menu.setCurrentRow)
        # self.menu_btn.toggled.connect(self.button_icon_change)

    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu_icon_only.clear()
        self.side_menu.clear()

        for menu in self.menu_list:
            # Set items for the side menu with icons only
            item = QListWidgetItem()
            item.setIcon(QIcon(menu.get("icon")))
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon_only.addItem(item)
            self.side_menu_icon_only.setCurrentRow(0)

            # Set items for the side menu with icons and text
            item_new = QListWidgetItem()
            item_new.setIcon(QIcon(menu.get("icon")))
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
            self.side_menu.setCurrentRow(0)
            
    

    def init_stackwidget(self):
        main_window = MyMainWindow()
        # Create an instance of Ui_TestMainWindow
        test_ui = Ui_StudentManagement()
        test_ui2 = Ui_Attendance()
        # Create a QMainWindow to hold the UI
        test_window = QMainWindow()
        test_window2 = QMainWindow()
        # Setup the UI inside the QMainWindow
        test_ui.setupUi(test_window)
        test_ui2.setupUi(test_window2)
        # Add the QMainWindow to the QStackWidget
        self.main_content.insertWidget(1, test_window)
        self.main_content.insertWidget(2, test_window2)
        self.main_content.insertWidget(3, main_window)                 
    



if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load style file
    with open("Interface\Teacher\Dashboard\Dashboard.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())