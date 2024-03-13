from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from RegisterGUI import RegisterWindow
from database import Database


class LoginGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login")
        self.setGeometry(400, 400, 400, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.login_button = QPushButton("Login")
        self.register_button = QPushButton("No account yet? Register")

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.login_button)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

        self.controller = LoginController(self)

        self.register_button.clicked.connect(self.controller.on_register_button_click)


class LoginModel:
    def __init__(self):
        self.database = Database()

    def login(self, username, password):
        return username != "" and password != ""


class LoginController:
    def __init__(self, window):
        self.window = window
        self.model = LoginModel()

        self.window.login_button.clicked.connect(self.on_login_button_click)

    def on_login_button_click(self):
        username = self.window.username_entry.text()
        password = self.window.password_entry.text()

        if self.model.login(username, password):
            QMessageBox.information(self.window, "Login Successful", f"Welcome, {username}")
        else:
            QMessageBox.critical(self.window, "Login Failed", "Invalid username or password")

    def on_register_button_click(self):
        self.window.hide()  # Hide the login window
        register_window = RegisterWindow()
        register_window.show()


if __name__ == "__main__":
    app = QApplication([])
    login_window = LoginGUI()
    login_window.show()
    app.exec_()
