import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt

class OnlineImageDisplay(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Online Image Display")

        layout = QVBoxLayout()

        self.image_label = QLabel()
        layout.addWidget(self.image_label)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Load and display the online image
        image_url = "http://116.204.108.17:9000/images/python.png"  # 替换为实际的图片URL
        self.display_online_image(image_url)

    def display_online_image(self, image_url):
        response = requests.get(image_url)
        if response.status_code == 200:
            image_data = response.content
            pixmap = QPixmap()
            pixmap.loadFromData(image_data)
            self.image_label.setPixmap(pixmap)
            self.image_label.setScaledContents(True)  # 自动缩放图片以适应标签大小
        else:
            self.image_label.setText("Failed to load image")

def main():
    app = QApplication(sys.argv)
    window = OnlineImageDisplay()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
