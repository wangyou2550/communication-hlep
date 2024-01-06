import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QPushButton, QMessageBox, QScrollArea
from PyQt5.QtCore import Qt


class QuizPage(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        # 创建水平布局
        layout = QHBoxLayout()

        # 创建滚动区域
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # 创建滚动内容的窗口小部件
        scroll_content = QWidget(scroll_area)

        # 创建垂直布局，将其设置为滚动内容的布局
        scroll_layout = QVBoxLayout(scroll_content)

        # 题目
        question_label = QLabel("这是一个选择题的题目")
        question_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        scroll_layout.addWidget(question_label)

        # 选项
        options = ["A", "B", "C", "D"]
        self.option_buttons = []

        for i, option in enumerate(options):
            option_button = QRadioButton(option)
            option_button.setStyleSheet(
                "QRadioButton::indicator { width: 16px; height: 16px; }"
                "QRadioButton::indicator:checked { background-color: #4CAF50; }"
                "QRadioButton::indicator:unchecked { background-color: transparent; border: 2px solid #4CAF50; }"
                "QRadioButton::indicator:checked:hover { border: 2px solid #45a049; }"
            )
            option_button.clicked.connect(self.option_selected)
            scroll_layout.addWidget(option_button)
            self.option_buttons.append(option_button)

        # 答案解析
        self.answer_label = QLabel("答案解析：这是正确答案")
        self.answer_label.hide()  # 初始隐藏
        self.answer_label.setStyleSheet("font-size: 14px; font-weight: bold; color: #4CAF50; margin: 16px;")
        scroll_layout.addWidget(self.answer_label)

        # 设置滚动内容的布局
        scroll_content.setLayout(scroll_layout)

        # 将滚动内容设置为滚动区域的小部件
        scroll_area.setWidget(scroll_content)

        # 设置滚动区域的宽度为页面宽度的10%
        # scroll_area.setMaximumWidth(int(self.width() * 0.1))

        # 将滚动区域添加到水平布局
        layout.addWidget(scroll_area)

        # 设置水平布局为窗口的布局
        self.setLayout(layout)

    def option_selected(self):
        for button in self.option_buttons:
            if button.isChecked():
                button.setStyleSheet("QRadioButton::indicator:checked { background-color: #4CAF50; }"
                                     "QRadioButton::indicator:checked:hover { border: 2px solid #45a049; }")
            else:
                button.setStyleSheet("QRadioButton::indicator:checked { background-color: transparent; border: 2px solid #4CAF50; }"
                                     "QRadioButton::indicator:checked:hover { border: 2px solid #45a049; }")


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QuizPage()
    window.show()

    sys.exit(app.exec_())