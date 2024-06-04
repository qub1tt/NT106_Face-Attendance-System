import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QLabel, QListWidgetItem, QWidget, QGridLayout, QVBoxLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon, QPixmap, QFont

# Import the UI class from the 'main_ui' module
from Dashboard_UI import Ui_MainWindow

from SM import Ui_StudentManagement
from AM import Ui_Attendance
from CK import MyMainWindow
from CK import Ui_CheckCamera

# Define a custom MainWindow class
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.my_main_window = MyMainWindow()
        self.ui = Ui_CheckCamera()
        self.ui.setupUi(self.my_main_window)

        # Initialize the UI from the generated 'main_ui' class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        self.menu_btn = self.ui.menu_btn
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("Interface/Png/DashboardIcon/close.svg"))
        self.menu_btn.setIconSize(QSize(30, 30))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)

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
        # Connect signals and slots for menu button and side menu
        self.menu_btn.toggled['bool'].connect(self.side_menu.setHidden)
        self.menu_btn.toggled['bool'].connect(self.title_label.setHidden)
        self.menu_btn.toggled['bool'].connect(self.side_menu_icon_only.setVisible)
        self.menu_btn.toggled['bool'].connect(self.title_icon.setHidden)

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged['int'].connect(self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged['int'].connect(self.side_menu.setCurrentRow)
        self.menu_btn.toggled.connect(self.button_icon_change)

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
    

    def button_icon_change(self, status):
        # Change the menu button icon based on its status
        if status:
            self.menu_btn.setIcon(QIcon("Interface/Png/DashboardIcon/open.svg"))
        else:
            self.menu_btn.setIcon(QIcon("Interface/Png/DashboardIcon/close.svg"))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load style file
    with open("Interface\Teacher\Dashboard\Dashboard.qss") as f:
        style_str = f.read()

    app.setStyleSheet(style_str)

    window = MainWindow()
    window.showMaximized()

    sys.exit(app.exec())