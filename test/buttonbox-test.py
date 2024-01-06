import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QDialogButtonBox


class MyDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Button Box Example')
        self.setGeometry(100, 100, 300, 200)

        self.setup_ui()

    def setup_ui(self):
        # 创建对话框的布局
        layout = QVBoxLayout()

        # 创建 Button Box
        button_box = QDialogButtonBox()

        # 添加标准按钮到 Button Box
        button_box.addButton("确定", QDialogButtonBox.AcceptRole)
        button_box.addButton("取消", QDialogButtonBox.RejectRole)
        button_box.addButton("应用", QDialogButtonBox.ApplyRole)
        button_box.addButton("重置", QDialogButtonBox.ResetRole)

        # 连接按钮的信号与槽函数
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)
        button_box.clicked.connect(self.button_clicked)

        # 将 Button Box 添加到对话框的布局中
        layout.addWidget(button_box)

        # 设置对话框的布局
        self.setLayout(layout)

    def button_clicked(self, button):
        print(f"Button clicked: {button.text()}")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = MyDialog()
    dialog.show()
    sys.exit(app.exec_())