from PyQt5.QtWidgets import QTreeWidgetItem

class QTreeWidgetItem(QTreeWidgetItem):
    def __init__(self, parent, text, id, parent_id):
        super().__init__(parent, [text])
        self.id= id
        self.name=text
        self.parent_id=parent_id
