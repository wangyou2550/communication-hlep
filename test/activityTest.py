from PyQt5.QtCore import QUrl, pyqtSlot
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebChannel import QWebChannel
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建QWebEngineView小部件
        self.web_view = QWebEngineView()

        # 创建QWebChannel对象
        self.channel = QWebChannel()

        # 将QWebChannel对象注册到QWebEngineView的页面中
        self.page = QWebEnginePage()
        self.page.setWebChannel(self.channel)
        self.web_view.setPage(self.page)

        # 加载mxGraph的Web页面
        self.web_view.setUrl(QUrl("test.html"))

        # 将QWebEngineView添加到布局中或设置为窗口的中心部件（与前面的例子相同）

        # 将Python对象暴露给JavaScript
        self.channel.registerObject("pythonObject", self)

    # 在Python中处理mxGraph事件的函数
    @pyqtSlot(str)
    def mxGraphEvent(self, event):
        print("Handling mxGraph event in Python:", event)
        # TODO: 在这里处理mxGraph事件

# 创建PyQt应用程序和主窗口
app = QApplication([])
window = MainWindow()
window.show()

# 运行应用程序
app.exec_()