import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout


class FullNameDisplayApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Midterm in OOP")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Enter your fullname:", self)
        self.label.move(60, 20)
        self.label.setStyleSheet("color: red;")
        self.name_input = QLineEdit(self)
        self.name_input.move(200, 20)

        self.button = QPushButton("Click to display your Fullname", self)
        self.button.clicked.connect(self.display_name)
        self.button.move(60, 80)
        self.button.setStyleSheet("color: red;")

        self.output = QLineEdit(self)
        self.output.setReadOnly(True)
        self.output.move(200, 80)

        self.setLayout(layout)

    def display_name(self):
        name = self.name_input.text()
        self.output.setText(name)


app = QApplication(sys.argv)
window = FullNameDisplayApp()
window.show()
sys.exit(app.exec_())