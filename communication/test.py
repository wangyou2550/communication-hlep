import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox, QDialog, QVBoxLayout, QFileDialog
from PyQt5.QtGui import QPixmap

class EditDialog(QDialog):
    def __init__(self, parent=None, id=None, name=None, image=None):
        super().__init__(parent)
        self.id = id
        self.name = name
        self.image = image
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.name_input.setText(self.name)
        layout.addWidget(QLabel('Name:'))
        layout.addWidget(self.name_input)

        self.image_label = QLabel()
        if self.image:
            pixmap = QPixmap(self.image)
            self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label)

        self.image_button = QPushButton('Select Image')
        self.image_button.clicked.connect(self.select_image)
        layout.addWidget(self.image_button)

        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save)
        layout.addWidget(self.save_button)

        self.setLayout(layout)

    def select_image(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        image_path, _ = QFileDialog.getOpenFileName(self, 'Select Image', '', 'Image Files (*.png *.jpg *.bmp);;All Files (*)', options=options)
        if image_path:
            self.image = image_path
            pixmap = QPixmap(image_path)
            self.image_label.setPixmap(pixmap)

    def save(self):
        self.name = self.name_input.text()
        self.accept()

class CRUDApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle('CRUD App')
        self.data=[]

        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        layout = QVBoxLayout()

        self.name_input = QLineEdit()
        self.image_label = QLabel()

        self.addButton = QPushButton('Add')
        self.addButton.clicked.connect(self.add_item)

        layout.addWidget(QLabel('Name:'))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel('Image:'))
        layout.addWidget(self.image_label)
        layout.addWidget(self.addButton)

        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['ID', 'Name', 'Image'])

        layout.addWidget(self.table)

        self.page = 1
        self.page_size = 5

        self.load_data()

        self.prevButton = QPushButton('Previous')
        self.prevButton.clicked.connect(self.prev_page)
        self.nextButton = QPushButton('Next')
        self.nextButton.clicked.connect(self.next_page)

        layout.addWidget(self.prevButton)
        layout.addWidget(self.nextButton)

        main_widget.setLayout(layout)

        self.show()

    def add_item(self):
        dialog = EditDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.data.append({'id': len(self.data) + 1, 'name': dialog.name, 'image': dialog.image})
            self.load_data()

    def edit_item(self, row):
        item = self.data[row]
        dialog = EditDialog(self, id=item['id'], name=item['name'], image=item['image'])
        if dialog.exec_() == QDialog.Accepted:
            self.data[row]['name'] = dialog.name
            self.data[row]['image'] = dialog.image
            self.load_data()

    def delete_item(self, row):
        self.data.pop(row)
        self.load_data()

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self.load_data()


    def next_page(self):
        max_page = (len(self.data) - 1) // self.page_size + 1
        if self.page < max_page:
            self.page += 1
            self.load_data()

    def load_data(self):
        self.table.clearContents()
        self.table.setRowCount(0)

        start = (self.page - 1) * self.page_size
        end = start + self.page_size

        for item in self.data[start:end]:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.table.setItem(row, 0, QTableWidgetItem(str(item['id'])))
            self.table.setItem(row, 1, QTableWidgetItem(item['name']))
            self.table.setItem(row, 2, QTableWidgetItem(item['image']))

        # self.prevButton.setEnabled(self.page > 1)
        # max_page = (len(self.data) - 1) // self.page_size + 1
        # self.nextButton.setEnabled(self.page < max_page)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CRUDApp()
    sys.exit(app.exec_())
