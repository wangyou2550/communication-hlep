import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget

class CustomButton(QPushButton):
    def __init__(self, text, custom_parameter, parent=None):
        super().__init__(text, parent)
        self.custom_parameter = custom_parameter

class ButtonExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('Custom QPushButton Example')

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        custom_button = CustomButton('Click Me!', custom_parameter='Custom Value')
        custom_button.clicked.connect(self.on_button_click)
        layout.addWidget(custom_button)

        main_widget.setLayout(layout)

        self.show()

    def on_button_click(self):
        sender = self.sender()
        if isinstance(sender, CustomButton):
            print("Button clicked with custom parameter:", sender.custom_parameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ButtonExample()
    sys.exit(app.exec_())
