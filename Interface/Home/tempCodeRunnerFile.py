def start_camera(self):
#         # Start the camera
#         self.vid = cv2.VideoCapture(0)
#         self.timer = QtCore.QTimer(self)
#         self.timer.timeout.connect(self.update_frame)
#         self.timer.start(10)  # Update frame every 10 milliseconds

#     def update_frame(self):
#         # Capture frame-by-frame
#         ret, frame = self.vid.read()

#         # Convert frame to RGB format
#         frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

#         # Convert frame to QImage
#         height, width, channel = frame_rgb.shape
#         bytes_per_line = 3 * width
#         q_img = QtGui.QImage(frame_rgb.data, width, height, bytes_per_line, QtGui.QImage.Format.Format_RGB888)


#         # Set the QImage to the QLabel for display
#         self.ui.BorderCamera_2.setPixmap(QtGui.QPixmap.fromImage(q_img))