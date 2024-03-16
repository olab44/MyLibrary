from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel
from PyQt5.QtWidgets import QMessageBox, QWidget, QVBoxLayout
from gui.RegisterGUI import RegisterWindow
from gui.login_model import LoginModel
from gui.dashboard import Dashboard


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MyLibrary")
        self.setGeometry(500, 500, 500, 300)
        self.dashboard = Dashboard()
        self.model = LoginModel()

        self.login_widgets = self.setup_login_widgets()
        self.dashboard_widgets = self.dashboard.setup_ui()

        self.show_login_widgets()

    def setup_login_widgets(self):
        login_widgets = QWidget()
        layout = QVBoxLayout()

        header_label = QLabel("Welcome to MyLibrary")
        font = header_label.font()
        font.setPointSize(20)
        font.setBold(True)
        header_label.setFont(font)
        layout.addWidget(header_label)

        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.setStyleSheet("background-color: #4CAF50; color: white;")
        self.register_button = QPushButton("No account yet? Register")
        self.register_button.setStyleSheet("background-color: #008CBA; color: white;")

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        login_widgets.setLayout(layout)
        self.login_button.clicked.connect(self.on_login_button_click)
        self.register_button.clicked.connect(self.on_register_button_click)

        return login_widgets

    def show_login_widgets(self):
        self.setCentralWidget(self.login_widgets)

    def show_dashboard_widgets(self):
        self.setCentralWidget(self.dashboard_widgets)

    def on_register_button_click(self):
        self.register_window = RegisterWindow()
        self.register_window.show()

    def on_login_button_click(self):
        username = self.username_entry.text().strip()
        password = self.password_entry.text().strip()
        if not username or not password:
            QMessageBox.critical(self, "Login Failed", "Please enter both username and password")
            return
        if self.model.login(username, password):
            QMessageBox.information(self, "Login Successful", f"Welcome, {username}")
            self.show_dashboard_widgets()
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password")
