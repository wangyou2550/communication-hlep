from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction
from PyQt5.QtGui import QImage, QTextImageFormat
from PyQt5.QtCore import Qt


class RichTextEditor(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Rich Text Editor")

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        toolbar = self.addToolBar("Formatting")
        toolbar.addAction("Bold", self.make_bold)
        toolbar.addAction("Italic", self.make_italic)
        toolbar.addAction("Underline", self.make_underline)
        toolbar.addSeparator()

        insert_image_action = QAction("Insert Image", self)
        insert_image_action.triggered.connect(self.insert_image)
        toolbar.addAction(insert_image_action)

    def make_bold(self):
        format = self.text_edit.currentCharFormat()
        format.setFontWeight(2)
        self.text_edit.mergeCurrentCharFormat(format)

    def make_italic(self):
        format = self.text_edit.currentCharFormat()
        format.setFontItalic(True)
        self.text_edit.mergeCurrentCharFormat(format)

    def make_underline(self):
        format = self.text_edit.currentCharFormat()
        format.setFontUnderline(True)
        self.text_edit.mergeCurrentCharFormat(format)

    def insert_image(self):
        image_path, _ = QFileDialog.getOpenFileName(self, "Insert Image", "", "Image Files (*.png *.jpg *.jpeg *.gif)")
        if image_path:
            image = QImage(image_path)
            if not image.isNull():
                image_format = QTextImageFormat()
                image_format.setName(image_path)
                image_format.setWidth(image.width())
                image_format.setHeight(image.height())
                self.text_edit.textCursor().insertImage(image_format)


if __name__ == "__main__":
    app = QApplication([])
    window = RichTextEditor()
    window.show()
    app.exec_()