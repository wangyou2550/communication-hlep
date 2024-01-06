import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt


class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('若依后台管理系统')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(400, 300)

        layout = QVBoxLayout()

        title_label = QLabel('若依后台管理系统')
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('账号')
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('密码')
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText('验证码')
        layout.addWidget(self.code_input)

        self.remember_me_checkbox = QCheckBox('记住密码')
        layout.addWidget(self.remember_me_checkbox)

        login_button = QPushButton('登录')
        login_button.clicked.connect(self.handle_login)
        layout.addWidget(login_button)

        self.setLayout(layout)

        self.setStyleSheet('''
            QWidget {
                background-image: url('background.jpg');
                background-size: cover;
            }

            QLabel {
                color: #707070;
                font-size: 18px;
            }

            QLineEdit {
                height: 38px;
                font-size: 14px;
            }

            QPushButton {
                height: 38px;
                font-size: 14px;
                background-color: #007bff;
                color: white;
            }
        ''')

    def handle_login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        code = self.code_input.text()
        remember_me = self.remember_me_checkbox.isChecked()

        # 在这里执行登录逻辑，根据需要使用上述获取到的数据进行处理

        # 示例代码中只是简单打印获取到的数据
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Code: {code}")
        print(f"Remember Me: {remember_me}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())