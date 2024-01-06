from PyQt5.QtWidgets import QPushButton

# 带有id的button
class IdButton(QPushButton):
    def __init__(self, text, id):
        super().__init__()
        self.text= text
        self.id= id
        self.setText(text)