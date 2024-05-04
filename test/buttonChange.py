import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtGui import QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.feedback_value = 0
        self.favorite_value = 0

        self.initUI()

    def initUI(self):
        layout = QHBoxLayout()

        self.feedback_button = QPushButton()
        self.feedback_button.clicked.connect(self.feedbackClicked)
        layout.addWidget(self.feedback_button)

        self.favorite_button = QPushButton()
        self.favorite_button.clicked.connect(self.favoriteClicked)
        layout.addWidget(self.favorite_button)

        self.updateButtons()

        self.setLayout(layout)
        self.setWindowTitle('Button Example')
        self.show()

    def updateButtons(self):
        if self.feedback_value == 0:
            self.feedback_button.setText('反馈')
            self.feedback_button.setStyleSheet("background-color: green;")
            self.feedback_button.setEnabled(True)
        else:
            self.feedback_button.setText('已反馈')
            self.feedback_button.setStyleSheet("background-color: red;")
            self.feedback_button.setEnabled(False)

        if self.favorite_value == 0:
            self.favorite_button.setText('收藏')
            self.favorite_button.setStyleSheet("background-color: green;")
            self.favorite_button.setEnabled(True)
        else:
            self.favorite_button.setText('已收藏')
            self.favorite_button.setStyleSheet("background-color: red;")
            self.favorite_button.setEnabled(False)

    def feedbackClicked(self):
        self.feedback_value = 1
        self.updateButtons()

    def favoriteClicked(self):
        self.favorite_value = 1
        self.updateButtons()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())