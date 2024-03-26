from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItem


class StepItem(QStandardItem):
    def __init__(self, id, text,imageSrc,sectionId):
        super().__init__(text)
        self.id = id
        self.imageSrc=imageSrc
        self.sectionId=sectionId
        self.setData(text, Qt.DisplayRole)  # 设置text为显示角色的数据
        self.setData(id, Qt.UserRole)  # 设置id为自定义角色的数据
        self.setData(imageSrc, Qt.UserRole)  # 设置id为自定义角色的数据
        self.setData(sectionId, Qt.UserRole)  # 设置id为自定义角色的数据
