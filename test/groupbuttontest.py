import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox, QGridLayout, QPushButton, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("GroupButton Example")

        self.groupbox = QGroupBox("选择题")
        # self.groupbox.setCheckable(True)
        # self.groupbox.setChecked(True)
        # self.groupbox.toggled.connect(self.toggle_groupbox)

        self.grid_layout = QGridLayout()
        self.populate_buttons(15)  # 填充按钮，这里示例创建了20个按钮

        self.vbox_layout = QVBoxLayout()
        self.vbox_layout.addWidget(self.groupbox)

        self.widget = QWidget()
        self.widget.setLayout(self.vbox_layout)
        self.setCentralWidget(self.widget)

    def populate_buttons(self, num_buttons):
        num_columns = 10
        num_rows = (num_buttons + num_columns - 1) // num_columns

        for i in range(num_buttons):
            button = QPushButton(f"{i+1}")
            button.setFixedSize(100, 30)
            button.clicked.connect(self.show_current_qustion)
            self.grid_layout.addWidget(button, i // num_columns, i % num_columns)

        self.groupbox.setLayout(self.grid_layout)

    def show_current_qustion(self):
        button = self.sender()  # 获取发出信号的按钮对象
        button_text = button.text()
        print(f"Button clicked: {button_text}")
    # def toggle_groupbox(self, checked):
    #     # self.groupbox.setChecked(checked)
    #     # self.groupbox.setTitle("GroupButton" if checked else "")
    #     if checked:
    #         for button in self.buttons:
    #             self.grid_layout.addWidget(button)
    #     else:
    #         for button in self.buttons:
    #             self.grid_layout.removeWidget(button)
    #             button.setParent(None)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())