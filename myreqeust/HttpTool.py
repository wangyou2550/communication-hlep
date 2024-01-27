import sys
import json
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from PyQt5.QtCore import Qt

# from login.LoginWindow import LoginWindow


class HttpTool:
    token = ''

    @staticmethod
    def load_token():
        try:
            with open('config.json', 'r') as file:
                config = json.load(file)
                return config.get('token', '')
        except Exception as e:
            print(f"Failed to load token: {str(e)}")
            return ''

    @staticmethod
    def save_token(token):
        try:
            with open('config.json', 'w') as file:
                config = {'token': token}
                json.dump(config, file)
        except Exception as e:
            print(f"Failed to save token: {str(e)}")

    @staticmethod
    def request(method, url, data=None):
        headers = {}
        if HttpTool.token:
            headers['Authorization'] = f"Bearer {HttpTool.token}"

        try:
            if method=='GET':
                response = requests.get(url, params=data)
            else:
                response = requests.request(method, url, headers=headers, json=data)
            response.raise_for_status()
            return HttpTool.deal_request(response.json())
        except requests.exceptions.RequestException as e:
            print(f"HTTP request failed: {str(e)}")
            return None

    @staticmethod
    def get(url,params=None):
        return HttpTool.request('GET', url,params)

    @staticmethod
    def post(url, data):
        return HttpTool.request('POST', url, data)

    @staticmethod
    def put(url, data):
        return HttpTool.request('PUT', url, data)

    @staticmethod
    def delete(url):
        return HttpTool.request('DELETE', url)

    @staticmethod
    def deal_request(response):
        if response:
            code = response.get('code', None)
            message = response.get('msg', None)

            if code == 200:
                # 请求成功
                if 'data' in response:
                    data = response.get('data', None)
                    return data
                # 处理返回的数据
                else:
                    return response
            elif code == 401:
                # Token 失效，需要重新登录
                HttpTool.token = ''
                QMessageBox.warning(

                    '登录过期',
                    '登录过期，退出重新登录.'
                )
                HttpTool.show_login_page()
            else:
                # 处理请求失败的情况
                error_message = f"Request failed with code {code}: {message}"
                HttpTool.handle_error(error_message)

    @staticmethod
    def handle_error( error_message):
        # 处理请求失败的情况
        object=QWidget()
        QMessageBox.critical(
            object,
            'Request Failed',
            f"错误原因:\n\n{error_message}"
        )

    @staticmethod
    def show_login_page(self):
        print(123)
        # 显示登录页面
        # login=LoginWindow()
        # login.show()

