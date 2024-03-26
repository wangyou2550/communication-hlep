import base64

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from component.ClickableLabel import ClickableLabel
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('用户注册')
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()



        # 手机号
        phone_layout = QHBoxLayout()
        phone_label = QLabel('手机号:')
        self.phone_input = QLineEdit()
        self.phone_input.setFixedWidth(200)
        phone_layout.addWidget(phone_label)
        phone_layout.addWidget(self.phone_input)
        layout.addLayout(phone_layout)

        # 用户名
        username_layout = QHBoxLayout()
        username_label = QLabel('姓名:')
        self.username_input = QLineEdit()
        self.username_input.setFixedWidth(200)
        username_layout.addWidget(username_label)
        username_layout.addWidget(self.username_input)
        layout.addLayout(username_layout)

        # 密码
        password_layout = QHBoxLayout()
        password_label = QLabel('密码:')
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        self.password_input.setFixedWidth(200)
        password_layout.addWidget(password_label)
        password_layout.addWidget(self.password_input)
        layout.addLayout(password_layout)


        # 学校
        school_layout = QHBoxLayout()
        school_label = QLabel('学校:')
        self.school_combo = QComboBox()
        self.school_combo.addItems(['学校A', '学校B', '学校C'])  # 自定义学校选项
        school_layout.addWidget(school_label)
        school_layout.addWidget(self.school_combo)
        layout.addLayout(school_layout)

        # 性别
        gender_layout = QHBoxLayout()
        gender_label = QLabel('性别:')
        self.gender_combo = QComboBox()
        self.gender_combo.addItems(['男', '女'])
        gender_layout.addWidget(gender_label)
        gender_layout.addWidget(self.gender_combo)
        layout.addLayout(gender_layout)

        # 图片验证码
        code_layout = QHBoxLayout()

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText('验证码')
        code_layout.addWidget(self.code_input)

        self.code_image_label = ClickableLabel()
        code_layout.addWidget(self.code_image_label)
        self.generate_code_image()
        self.code_image_label.clicked.connect(self.generate_code_image)

        layout.addLayout(code_layout)

        # 注册按钮
        register_button = QPushButton('注册')
        register_button.clicked.connect(self.register)
        layout.addWidget(register_button)

        self.setLayout(layout)

        # 设置样式
        with open('styles.css', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def register(self):
        captcha = self.captcha_input.text()
        phone = self.phone_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        school = self.school_combo.currentText()
        gender = self.gender_combo.currentText()

        # 在此处添加注册逻辑，验证输入等
        # ...

        # 打印用户信息
        print('验证码:', captcha)
        print('手机号:', phone)
        print('用户名:', username)
        print('密码:', password)
        print('学校:', school)
        print('性别:', gender)

        # 提示注册成功
        QMessageBox.information(self, '注册成功', '注册成功！')
    def generate_code_image(self):
        # 图像数据,base64
        data=HttpTool.get(PathConstant.GET_CAPTCHAIMAGE)
        self.image=data["img"]
        self.uuid=data["uuid"]

        # 解码图像数据
        image_data = base64.b64decode(self.image)
        # 创建 QPixmap 对象并设置图像
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        self.code_image_label.setPixmap(pixmap)

if __name__ == '__main__':
    app = QApplication([])
    window = RegisterWindow()
    window.show()
    app.exec_()