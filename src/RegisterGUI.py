from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton, QVBoxLayout


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Register")
        self.setGeometry(400, 400, 400, 200)

        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()

        self.email_label = QLabel("Email Address:")
        self.email_entry = QLineEdit()

        self.password_label = QLabel("Password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.Password)

        self.register_button = QPushButton("Register")

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_entry)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_entry)
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.register_button)

        self.setLayout(layout)
