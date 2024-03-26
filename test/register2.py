import base64

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

from component.ClickableLabel import ClickableLabel
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
import re
import hashlib
import pyotp

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
        self.username_input.setPlaceholderText('请输入姓名（不超过5个字符）')  # 添加占位文本
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

        # 确认密码
        confirm_password_layout = QHBoxLayout()
        confirm_password_label = QLabel('确认密码:')
        self.confirm_password_input = QLineEdit()
        self.confirm_password_input.setEchoMode(QLineEdit.Password)
        self.confirm_password_input.setFixedWidth(200)
        confirm_password_layout.addWidget(confirm_password_label)
        confirm_password_layout.addWidget(self.confirm_password_input)
        layout.addLayout(confirm_password_layout)

        # 学校
        school_layout = QHBoxLayout()
        school_label = QLabel('学校:')
        self.school_input = QLineEdit()
        self.school_input.setFixedWidth(200)
        school_layout.addWidget(school_label)
        school_layout.addWidget(self.school_input)
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

        # 设置样式抱歉，由于回答的文本长度限制，我无法完整地提供修改后的代码。以下是剩余的代码部分：


        with open('styles.css', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

    def register(self):
        captcha = self.captcha_input.text()
        phone = self.phone_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        confirm_password = self.confirm_password_input.text()
        school = self.school_input.text()
        gender = self.gender_combo.currentText()
        # 验证手机号格式
        if not re.match(r'^1[3456789]\d{9}$', phone):
            QMessageBox.warning(self, '错误', '手机号格式不正确！')
            return

        # 验证用户名长度
        if len(username) > 5:
            QMessageBox.warning(self, '错误', '姓名不能超过5个字符！')
            return

        # 验证密码和确认密码是否一致
        if password != confirm_password:
            QMessageBox.warning(self, '错误', '密码和确认密码不一致！')
            return

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
        data = HttpTool.get(PathConstant.GET_CAPTCHAIMAGE)
        self.image = data["img"]
        self.uuid = data["uuid"]

        # 解码图像数据
        image_data = base64.b64decode(self.image)
        # 创建 QPixmap 对象并设置图像
        pixmap = QPixmap()
        pixmap.loadFromData(image_data)

        self.code_image_label.setPixmap(pixmap)

    # 生成随机的密钥
    def generate_key(self):
        key = pyotp.random_base32()
        return key

    # 保存密钥到文件
    def save_key(self,key):
        with open("key.key", "w") as file:
            file.write(key)

    # 加载密钥
    def load_key(self):
        with open("key.key", "r") as file:
            key = file.read()
        return key

    def generate_otp(self,secret_key):
        totp = pyotp.TOTP(secret_key)
        return totp.now()

if __name__ == '__main__':
    app = QApplication([])
    window = RegisterWindow()
    window.save_key(window.generate_key())
    window.show()
    app.exec_()