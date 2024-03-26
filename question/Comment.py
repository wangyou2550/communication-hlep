import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QTextEdit, QPushButton, \
    QScrollArea, QFrame, QHBoxLayout
from PyQt5.QtGui import QPixmap


class CommentWidget(QWidget):
    def __init__(self, user_name, comment_text, avatar_path):
        super().__init__()
        self.user_name = user_name
        self.comment_text = comment_text
        self.avatar_path = avatar_path
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        avatar_label = QLabel()
        avatar_pixmap = QPixmap(self.avatar_path).scaled(50, 50)
        avatar_label.setPixmap(avatar_pixmap)
        layout.addWidget(avatar_label, alignment=Qt.AlignLeft)

        user_label = QLabel(self.user_name)
        layout.addWidget(user_label, alignment=Qt.AlignLeft)

        comment_frame = QFrame()
        comment_frame.setFrameShape(QFrame.Panel)
        comment_frame.setFrameShadow(QFrame.Sunken)
        comment_layout = QVBoxLayout(comment_frame)
        comment_label = QLabel(self.comment_text)
        comment_layout.addWidget(comment_label)
        layout.addWidget(comment_frame)

        self.setLayout(layout)


class CommentArea(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("评论区")
        self.setGeometry(100, 100, 800, 600)

        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)

        self.comment_input = QTextEdit()
        self.comment_input.setLineWrapMode(QTextEdit.WidgetWidth)  # 自动换行
        self.comment_input.setFixedHeight(60)
        self.submit_button = QPushButton("提交")
        self.submit_button.clicked.connect(self.submit_comment)

        layout = QVBoxLayout()
        layout.addWidget(self.scroll_area)
        layout.addWidget(self.comment_input)
        layout.addWidget(self.submit_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        # 设置样式表
        self.setStyleSheet("""
                  QLabel#CommentFrame {
                      background-color: #F5F5F5;
                      border-radius: 5px;
                      padding: 10px;
                  }

                  QPushButton {
                      background-color: #4CAF50;
                      color: white;
                      padding: 5px 10px;
                      border: none;
                      border-radius: 3px;
                  }

                  QTextEdit {
                      background-color: #F5F5F5;
                      border: 1px solid #CCCCCC;
                      border-radius: 5px;
                      padding: 5px;
                  }
              """)

    def submit_comment(self):
        user_name = "John Doe"  # 替换为实际的用户名
        comment_text = self.comment_input.toPlainText()
        avatar_path = "../test/avatar.jpg"  # 替换为实际的头像文件路径

        if comment_text:
            comment_widget = CommentWidget(user_name, comment_text, avatar_path)
            self.scroll_layout.addWidget(comment_widget)
            self.comment_input.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    comment_area = CommentArea()
    comment_area.show()
    sys.exit(app.exec_())