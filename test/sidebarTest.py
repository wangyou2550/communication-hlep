import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton, QHBoxLayout

from question.MultipleChoiceQuestion import MultipleChoiceQuestion


class SidebarButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self.setFixedHeight(50)
        self.setStyleSheet('QPushButton { background-color: gray; }'
                           'QPushButton:hover { background-color: green; }')


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置主窗口的整体布局
        self.layout = QHBoxLayout()

        # 创建侧边栏部件
        sidebar = QWidget()
        sidebar.setFixedWidth(int(self.width() * 0.2))  # 设置侧边栏宽度为主窗口宽度的 20%
        sidebar.setStyleSheet('background-color: #F0F0F0;')

        # 创建侧边栏按钮
        button_titles = ['题目', '提示', '评论', '题解','做题记录']
        button_functions = [self.show_title, self.show_hint, self.show_comments, self.show_solution,self.show_record]
        sidebar_layout = QVBoxLayout()

        for title, func in zip(button_titles, button_functions):
            button = SidebarButton(title)
            button.clicked.connect(func)
            sidebar_layout.addWidget(button)

        sidebar.setLayout(sidebar_layout)

        # 创建右侧显示区域
        self.content_area = QWidget()
        self.content_area.setStyleSheet('background-color: white;')

        # 设置主窗口布局
        self.layout.addWidget(sidebar)
        # self.layout.addWidget(QWidget())  # 占位部件，用于显示 widget2 或 widget3
        self.layout.addWidget(self.content_area)

        main_widget = QWidget()
        main_widget.setLayout(self.layout)
        self.setCentralWidget(main_widget)

    def show_title(self):
        self.show_content_widget('题目')

    def show_hint(self):
        self.show_content_widget('提示')

    def show_comments(self):
        self.show_content_widget('评论')

    def show_solution(self):
        self.show_content_widget('题解')

    def show_record(self):
        self.show_content_widget('题解')

    def show_content_widget(self, text):
        content_widget = MultipleChoiceQuestion()
        # 删除占位部件并添加新的部件
        self.layout.itemAt(1).widget().deleteLater()
        self.layout.addWidget(content_widget)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.setWindowTitle("Sidebar Demo")
    window.setGeometry(100, 100, 800, 600)
    window.show()
    sys.exit(app.exec_())