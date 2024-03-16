from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QMessageBox
from PyQt5.QtWidgets import QPushButton, QVBoxLayout

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


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


class RegisterModel:
    def __init__(self):
        # Initialize your email server settings here
        self.email_sender = 'your_email@example.com'
        self.email_password = 'your_email_password'
        self.smtp_server = 'smtp.example.com'
        self.smtp_port = 587  # Port for TLS

    def send_verification_email(self, email):
        sender_email = self.email_sender
        receiver_email = email
        password = self.email_password
        smtp_server = self.smtp_server
        smtp_port = self.smtp_port

        message = MIMEMultipart("alternative")
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Verification Email"

        text = """\
        Hi,
        
        Please click the link below to verify your email:
        http://yourwebsite.com/verify?email={email}
        """

        html = """\
        <html>
          <body>
            <p>Hi,<br><br>
               Please click the link below to verify your email:<br>
               <a href='http://yourwebsite.com/verify?email={email}'>Verify Email</a>
            </p>
          </body>
        </html>
        """

        part1 = MIMEText(text, "plain")
        part2 = MIMEText(html, "html")

        message.attach(part1)
        message.attach(part2)

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
            server.quit()
            return True
        except Exception as e:
            print("Error sending email:", e)
            return False

    def register_user(self, username, email, password):
        # Code to register user
        pass


class RegisterController:
    def __init__(self, window, model, login_window):
        self.window = window
        self.model = model
        self.login_window = login_window

        self.window.register_button.clicked.connect(self.on_register_button_click)

    def on_register_button_click(self):
        username = self.window.username_entry.text()
        email = self.window.email_entry.text()
        password = self.window.password_entry.text()

        if self.model.register_user(username, email, password):
            QMessageBox.information(self.window, "Registration Successful", "Verification link sent to your email.")
            if self.model.send_verification_email(email):
                QMessageBox.information(self.window, "Email Sent", "Verification link has been sent to your email.")
                # Clear fields after registration
                self.window.username_entry.clear()
                self.window.email_entry.clear()
                self.window.password_entry.clear()
                # Show login window again
                self.login_window.show()
            else:
                QMessageBox.critical(self.window, "Email Error", "Failed to send verification email.")
        else:
            QMessageBox.critical(self.window, "Registration Failed", "Failed to register user.")

