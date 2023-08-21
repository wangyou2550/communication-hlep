from PyQt5.QtWidgets import QPushButton


class InfoButton(QPushButton):
    def __init__(self,  text, id,name,parent=None):
        super().__init__(text,parent)
        self.id= id
        self.name=name
