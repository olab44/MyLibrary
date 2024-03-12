import sys
from PyQt5.QtWidgets import QApplication
from loginGUI import LoginGUI


def main():
    app = QApplication(sys.argv)

    login_window = LoginGUI()
    login_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
