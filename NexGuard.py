import sys
import platform
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QLabel, QPushButton, QWidget

class NexGuard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NexGuardOS - Security Enhancer")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Detect OS
        os_name = platform.system()
        os_label = QLabel(f"Detected Operating System: {os_name}")
        os_label.setStyleSheet("color: green; font-size: 18px;")
        layout.addWidget(os_label)

        # Add options for security configurations
        layout.addWidget(QLabel("Choose your security profile:"))
        personal_btn = QPushButton("Personal Use")
        personal_btn.clicked.connect(self.setup_personal)
        layout.addWidget(personal_btn)

        business_btn = QPushButton("Business")
        business_btn.clicked.connect(self.setup_business)
        layout.addWidget(business_btn)

        advanced_btn = QPushButton("Advanced")
        advanced_btn.clicked.connect(self.setup_advanced)
        layout.addWidget(advanced_btn)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def setup_personal(self):
        self.show_message("Configuring for Personal Use...")
        # Code for configuring personal security features

    def setup_business(self):
        self.show_message("Configuring for Business Use...")
        # Code for configuring business security features

    def setup_advanced(self):
        self.show_message("Configuring for Advanced Use...")
        # Code for configuring advanced security features

    def show_message(self, message):
        msg_label = QLabel(message)
        msg_label.setStyleSheet("color: lightgreen; font-size: 16px;")
        self.centralWidget().layout().addWidget(msg_label)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = NexGuard()
    mainWin.show()
    sys.exit(app.exec_())
