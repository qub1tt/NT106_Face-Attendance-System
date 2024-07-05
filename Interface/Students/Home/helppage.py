import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QWidget, QTextEdit, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon

class HelpWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Face Attendance System Help")
        self.setWindowIcon(QIcon("Interface/Png/Icon/face-id.png"))
        self.setGeometry(100, 100, 800, 600)
        self.center_window()
        layout = QVBoxLayout()
        
        # Centered Title
        title_container = QHBoxLayout()
        title = QLabel("Face Attendance System Help Page")
        title.setStyleSheet("font-size: 24px; font-weight: bold; color: #333;background-color: rgb(165,213,255);")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Align title to the center
        title_container.addWidget(title)
        layout.addLayout(title_container)

        # Combined Sections
        combined_text = QTextEdit()
        combined_text.setReadOnly(True)
        combined_text.setHtml("""
        <h2 style="color: #0056b3;">1. Face Registration</h2>
        <h3 style="color: #007bff;">Registration Conditions:</h3>
        <ul>
            <li>The face photo must be clear, unobstructed, and only contain the user's face.</li>
            <li>Do not use sunglasses, masks, or accessories that obstruct the face.</li>
            <li>Only well-lit faces will be accepted.</li>
            <li>All information must be filled out completely.</li>
            <li>Information fields must meet the following constraints:</li>
            <ul>
                <li><strong>Name:</strong> Must be alphabetic, with the first letter of each name capitalized.</li>
                <li><strong>Email:</strong> Must be in the format &lt;username&gt;@&lt;domain&gt;.</li>
                <li><strong>Faculty, Major:</strong> Must be alphabetic.</li>
                <li><strong>Year:</strong> Must be a number and less than 8.</li>
            </ul>
        </ul>
        
        <h3 style="color: #007bff;">Registration Guide:</h3>
        <ol>
            <li>Log in to the provided account.</li>
            <li>Click the “New” button to proceed to the registration interface.</li>
            <li>Fill in all personal information including: Name, Email, Class, Faculty, Major, Year.</li>
            <li>Choose the registration mode:
                <ul>
                    <li><strong>Using Camera:</strong> Ensure good lighting and that the face is within the frame. Press Enter to capture the photo from the camera.</li>
                    <li><strong>Uploading Photo:</strong> Ensure the face photo is clear and unobstructed.</li>
                </ul>
            </li>
            <li>Click the “Register” button to complete the process.</li>
        </ol>

        <h2 style="color: #0056b3;">2. Face Recognition Attendance</h2>
        <h3 style="color: #007bff;">Usage Conditions:</h3>
        <ul>
            <li>Users must have completed face registration before using the attendance function.</li>
            <li>The face must be clearly recognized, unobstructed, and well-lit.</li>
            <li>Do not use a photo for attendance.</li>
        </ul>
        
        <h3 style="color: #007bff;">Attendance Guide:</h3>
        <ol>
            <li>Log in using the account with the registered face.</li>
            <li>Ensure good lighting and that the face is within the frame.</li>
            <li>Press Enter for the system to recognize the face.</li>
            <li>Select the class for the system to record the attendance.</li>
        </ol>

        <h2 style="color: #0056b3;">3. Notes on Face Registration and Attendance</h2>
        <h3 style="color: #007bff;">Lighting:</h3>
        <ul>
            <li>Choose a space with sufficient lighting, avoiding backlight or too dark areas.</li>
            <li>Ensure lighting comes from the front or both sides of the face.</li>
        </ul>
        <h3 style="color: #007bff;">Photo Taking:</h3>
        <ul>
            <li>Take the photo at a moderate distance so that the face occupies most of the frame.</li>
            <li>Ensure the face is not obstructed by hair or accessories.</li>
            <li>The face must exhibit a natural expression, not squinting or too stiff.</li>
            <li><strong>Photos are only supported in jpg format</strong>
        </ul>
        <h3 style="color: #007bff;">Using Camera:</h3>
        <ul>
            <li>Choose a position with enough light for the system to accurately recognize the face.</li>
            <li>Ensure the camera is clean, not blurry or dirty.</li>
            <li>Maintain a distance of 30-50 cm between the face and the camera.</li>
        </ul>
        """)
        layout.addWidget(combined_text)
        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
    def center_window(self):
        screen_geometry = QApplication.primaryScreen().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HelpWindow()
    window.show()
    sys.exit(app.exec())
