from sys import argv
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

def WebView(url: str, windowName: str):
    class Browser(QMainWindow):
        def __init__(self):
            super(Browser, self).__init__()
            self.browser = QWebEngineView()
            self.browser.setUrl(QUrl(url))
            self.setCentralWidget(self.browser)
            self.showMaximized()

    app = QApplication(argv)
    app.setApplicationName(windowName)
    b = Browser()
    app.exec_()
