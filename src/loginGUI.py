from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from database import Database


class LoginGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.database = Database()

        if self.database.test_connection():
            print("Connection to the database is successful.")
        else:
            print("Error: Unable to connect to the database.")

        self.setWindowTitle("Login")
        self.setGeometry(300, 300, 300, 150)

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.on_login_button_click)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def on_login_button_click(self):
        username = self.username_entry.text()
        password = self.password_entry.text()

        if self.login(username, password):
            QMessageBox.information(self, "Login Successful", "Welcome, {}".format(username))
        else:
            QMessageBox.critical(self, "Login Failed", "Invalid username or password")

    def login(self, username, password):
        return username != "" and password != ""
