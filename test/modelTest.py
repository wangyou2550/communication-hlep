from PyQt5.QtGui import QStandardItem, QStandardItemModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView

class CustomStandardItem(QStandardItem):
    def __init__(self, id, text):
        super().__init__(text)
        self.id = id

if __name__ == '__main__':
    app = QApplication([])

    model = QStandardItemModel()

    item = CustomStandardItem(2, "Apple")
    item.setData(item.text(), Qt.DisplayRole)  # 设置text为显示角色的数据
    item.setData(item.id, Qt.UserRole)  # 设置id为自定义角色的数据

    model.appendRow(item)

    view = QTableView()
    view.setModel(model)

    def on_item_clicked(index):
        item = model.itemFromIndex(index)
        item_id = item.id
        print(f"Selected item id: {item_id}")


    view.clicked.connect(on_item_clicked)
    window = QMainWindow()
    window.setCentralWidget(view)
    window.show()

    app.exec_()