import socket
import cv2
import pickle
import struct
import threading
import pyshine as ps
from PyQt6 import QtCore, QtGui

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
