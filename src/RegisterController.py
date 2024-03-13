from PyQt5.QtWidgets import QMessageBox


class RegisterController:
    def __init__(self, window, model):
        self.window = window
        self.model = model

        self.window.register_button.clicked.connect(self.on_register_button_click)

    def on_register_button_click(self):
        username = self.window.username_entry.text()
        email = self.window.email_entry.text()
        password = self.window.password_entry.text()

        if self.model.register_user(username, email, password):
            QMessageBox.information(self.window, "Registration Successful", "Please check your email for verification.")
            self.model.send_verification_email(email)
        else:
            QMessageBox.critical(self.window, "Registration Failed", "Failed to register user.")
