import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTextEdit, QPushButton, QLabel, QFileDialog
from PyQt5.QtGui import QPixmap

class CommentBox(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Comment Box')
        self.setGeometry(100, 100, 600, 400)

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        self.comment_edit = QTextEdit(self)
        layout.addWidget(self.comment_edit)

        self.image_label = QLabel(self)
        layout.addWidget(self.image_label)

        attach_button = QPushButton('Attach Image', self)
        attach_button.clicked.connect(self.attach_image)
        layout.addWidget(attach_button)

        submit_button = QPushButton('Submit', self)
        submit_button.clicked.connect(self.submit_comment)
        layout.addWidget(submit_button)

        main_widget.setLayout(layout)

        self.image_path = None

    def attach_image(self):
        options = QFileDialog.Options()
        image_path, _ = QFileDialog.getOpenFileName(self, "Attach Image", "", "Images (*.png *.jpg *.jpeg *.bmp);;All Files (*)", options=options)
        if image_path:
            self.image_path = image_path
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)

    def submit_comment(self):
        comment_text = self.comment_edit.toPlainText()
        if comment_text:
            if self.image_path:
                # Process both comment_text and image_path
                print("Comment:", comment_text)
                print("Image Path:", self.image_path)
            else:
                # Process only comment_text
                print("Comment:", comment_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    comment_box = CommentBox()
    comment_box.show()
    sys.exit(app.exec_())
