from PyQt5.QtWidgets import QTabWidget, QWidget, QVBoxLayout, QLabel


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setGeometry(400, 400, 400, 400)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.profile_tab = QWidget()
        self.books_tab = QWidget()
        self.stats_tab = QWidget()
        self.tabs.addTab(self.profile_tab, "Profile Info")
        self.tabs.addTab(self.books_tab, "Your Books")
        self.tabs.addTab(self.stats_tab, "Stats")
        self.profile_label = QLabel("Profile Information:")
        self.profile_layout = QVBoxLayout()
        self.profile_layout.addWidget(self.profile_label)
        self.profile_tab.setLayout(self.profile_layout)

        layout.addWidget(self.tabs)
# class Dashboard(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Dashboard")
#         self.setGeometry(400, 400, 400, 400)

#         self.layout = QVBoxLayout(self)  # Create layout for Dashboard
#         self.setup_tabs()

#     def setup_tabs(self):
#         self.tabs = QTabWidget()
#         self.profile_tab = QWidget()
#         self.books_tab = QWidget()
#         self.stats_tab = QWidget()
#         self.tabs.addTab(self.profile_tab, "Profile Info")
#         self.tabs.addTab(self.books_tab, "Your Books")
#         self.tabs.addTab(self.stats_tab, "Stats")
#         self.profile_label = QLabel("Profile Information:")
#         self.profile_layout = QVBoxLayout()
#         self.profile_layout.addWidget(self.profile_label)
#         self.profile_tab.setLayout(self.profile_layout)

#         self.layout.addWidget(self.tabs)  # Add tabs to the layout
