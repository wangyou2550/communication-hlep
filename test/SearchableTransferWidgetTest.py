from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListView, QLineEdit, QPushButton
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QModelIndex


class SearchableTransferWidget(QWidget):
    def __init__(self, source_items, target_items):
        super().__init__()
        self.source_items = source_items
        self.target_items = target_items
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Search Input
        self.searchInput = QLineEdit()
        self.searchInput.textChanged.connect(self.filterItems)
        layout.addWidget(self.searchInput)

        # ListViews
        self.source_model = QStandardItemModel()
        self.target_model = QStandardItemModel()
        self.leftListView = QListView()
        self.leftListView.setModel(self.source_model)
        self.rightListView = QListView()
        self.rightListView.setModel(self.target_model)
        layout.addWidget(self.leftListView)
        layout.addWidget(self.rightListView)

        # Transfer Buttons
        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.transferItem)
        self.removeButton = QPushButton("Remove")
        self.removeButton.clicked.connect(self.transferItem)
        layout.addWidget(self.addButton)
        layout.addWidget(self.removeButton)

        self.setLayout(layout)
        self.populateListViews()

    def populateListViews(self):
        for item in self.source_items:
            qitem = QStandardItem(item)
            self.source_model.appendRow(qitem)

    def filterItems(self, searchText):
        for row in range(self.source_model.rowCount()):
            item = self.source_model.item(row)
            if searchText.lower() in item.text().lower():
                item.setHidden(False)
            else:
                item.setHidden(True)

    def transferItem(self):
        sender = self.sender()

        if sender == self.addButton:
            source_view = self.leftListView
            target_view = self.rightListView
            source_model = self.source_model
            target_model = self.target_model
            source_items = self.source_items
            target_items = self.target_items
        elif sender == self.removeButton:
            source_view = self.rightListView
            target_view = self.leftListView
            source_model = self.target_model
            target_model = self.source_model
            source_items = self.target_items
            target_items = self.source_items
        else:
            return

        selected_indexes = source_view.selectedIndexes()
        for index in selected_indexes:
            row = index.row()
            item = source_model.item(row)
            text = item.text()
            source_model.removeRow(row)
            target_model.appendRow(QStandardItem(text))

            # Update data source
            source_items.remove(text)
            target_items.append(text)

        source_view.clearSelection()
        target_view.clearSelection()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    source_items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']
    target_items = []
    widget = SearchableTransferWidget(source_items, target_items)
    widget.show()

    sys.exit(app.exec_())