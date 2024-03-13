from PyQt5.QtWidgets import QApplication
from loginGUI import LoginGUI, LoginModel, LoginController


def main():
    app = QApplication([])
    window = LoginGUI()
    # model = LoginModel()
    controller = LoginController(window)
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
