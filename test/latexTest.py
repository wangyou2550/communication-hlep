import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

app = QApplication(sys.argv)
window = QWidget()
layout = QVBoxLayout()

# 创建一个QWebEngineView控件来显示数学公式
view = QWebEngineView()

# 设置HTML内容，包含LaTeX数学公式
html_content = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML"></script>
</head>
<body>
    <div id="math-content" style="font-size: 18px;">
        Here is a math formula: \(E = mc^2\)
    </div>
    <script type="text/javascript">
        MathJax.Hub.Queue(['Typeset', MathJax.Hub, 'math-content']);
    </script>
</body>
</html>
"""

# 将HTML内容加载到QWebEngineView控件
view.setHtml(html_content)

layout.addWidget(view)
window.setLayout(layout)
window.show()

sys.exit(app.exec_())