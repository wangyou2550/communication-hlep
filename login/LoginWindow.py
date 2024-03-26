import os
import sys

import pyotp
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QCheckBox, QHBoxLayout
from PyQt5.QtGui import QIcon, QPixmap, QPainter, QImage
from PyQt5.QtCore import Qt
import random
import string
import base64

from component.ClickableLabel import ClickableLabel
from login.RegistWindow import RegisterWindow
from myreqeust.HttpTool import HttpTool
from myreqeust.PathConstant import PathConstant
from ui.MainWindow import MainWindow





class LoginWindow(QWidget):
    def __init__(self,main_window):
        super().__init__()
        self.setWindowTitle('北邮通信原理')
        self.setWindowIcon(QIcon('icon.png'))
        self.resize(400, 300)
        self.main_window=main_window

        layout = QVBoxLayout()

        title_label = QLabel('北邮通信原理')
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText('账号')
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText('密码')
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # self.code_input = QLineEdit()
        # self.code_input.setPlaceholderText('验证码')
        # layout.addWidget(self.code_input)
        #
        # self.code_image_label = ClickableLabel()
        # layout.addWidget(self.code_image_label)
        # self.code_image_label.clicked.connect(self.generate_code_image)
        # self.generate_code_image()

        code_layout = QHBoxLayout()

        self.code_input = QLineEdit()
        self.code_input.setPlaceholderText('验证码')
        code_layout.addWidget(self.code_input)

        self.code_image_label = ClickableLabel()
        code_layout.addWidget(self.code_image_label)
        self.generate_code_image()
        self.code_image_label.clicked.connect(self.generate_code_image)

        layout.addLayout(code_layout)

        login_layout=QHBoxLayout()


        login_button = QPushButton('登录')
        login_button.clicked.connect(self.handle_login)
        regist_button=QPushButton('没有账号去注册')
        regist_button.clicked.connect(self.handle_regist)
        regist_button.setObjectName("regist")
        layout.addWidget(login_button)
        layout.addWidget(regist_button)
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
            
            QPushButton#regist {
                height: 38px;
                font-size: 14px;
                background-color: #4CAF50;;
                color: white;
            }
        ''')

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

    def handle_login(self):
        user = {}
        user["username"] = self.username_input.text()
        user["password"] = self.password_input.text()
        user["code"] = self.code_input.text()
        user["uuid"]=self.uuid
        user["key"]=str(self.generate_otp(self.load_key()))
        data=HttpTool.post(PathConstant.LOGIN,user)
        # 存token
        if data:
            HttpTool.save_token(data["token"])
            HttpTool.token=data["token"]
            self.save_user_info()

            self.close()
            # self.main_window.show()
            self.main_window.showMaximized()  # 将窗口全屏显示


    def save_user_info(self):
        data = HttpTool.get(PathConstant.GET_INFO)
        HttpTool.user=data["user"]


    def handle_regist(self):
        self.regist_window=RegisterWindow()
        self.regist_window.show()

    def load_key(self):
        # 获取用户账户目录的路径
        user_dir = os.path.expanduser("~")
        # 拼接文件路径
        file_path = os.path.join(user_dir, "key.key")
        with open(file_path, "r") as file:
            key = file.read()
        return key

    def generate_otp(self,secret_key):
        totp = pyotp.TOTP(secret_key)
        return totp.now()