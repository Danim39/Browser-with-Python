import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import*
from PyQt6.QtCore import*
from PyQt6.QtWidgets import*
from PyQt6.QtWebEngineWidgets import*

class Form(QMainWindow):
    def __init__(self) :
        super().__init__()

        self.setWindowTitle("Danim Browser🪐")
        self.resize(600,600)

        self.browser=QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.browser.urlChanged.connect(self.update_Addressbar)
        self.setCentralWidget(self.browser)

        self.bookmarks_toolbar = QToolBar('Bookmarks', self)
        self.addToolBar(self.bookmarks_toolbar)

        self.addToolBarBreak() # Insert the distance between the bookmarks and the URL bar

        self.toolbar=QToolBar("Toolbar")
        self.addToolBar(self.toolbar)
        

        back_button=QAction("Back" , self)
        back_button.setToolTip("Go to previous page you visited ")
        back_button.triggered.connect(self.browser.back)
        self.toolbar.addAction(back_button)

        next_button=QAction("Next" , self)
        next_button.setToolTip("Go to next page ")
        next_button.triggered.connect(self.browser.forward)
        self.toolbar.addAction(next_button)

        refresh_button=QAction("Refresh" , self)
        refresh_button.setToolTip("Reload the page ")
        refresh_button.triggered.connect(self.browser.reload)
        self.toolbar.addAction(refresh_button)

        refresh_button=QAction("Home" , self)
        refresh_button.setToolTip("go to home(google.com)")
        refresh_button.triggered.connect(self.home)
        self.toolbar.addAction(refresh_button)

        Gitub_bookmark=QAction("Github(Danim)" , self)
        Gitub_bookmark.triggered.connect(lambda:self.browser.setUrl(QUrl("https://github.com/Danim39")))
        self.bookmarks_toolbar.addAction(Gitub_bookmark)
        

        linkedin = QAction("LinkedIn", self)
        linkedin.setStatusTip("Go to LinkedIn")
        linkedin.triggered.connect(lambda: self.browser.setUrl(QUrl("https://in.linkedin.com")))
        self.bookmarks_toolbar.addAction(linkedin)


        instagram = QAction("Instagram", self)
        instagram.setStatusTip("Go to Instagram")
        instagram.triggered.connect(lambda: self.browser.setUrl(QUrl("https://www.instagram.com")))
        self.bookmarks_toolbar.addAction(instagram)


        self.urlbar=QLineEdit()
        self.urlbar.returnPressed.connect(lambda:self.url_bar(QUrl(self.urlbar.text())))  # This specifies what to do when enter is pressed in the Entry field
        self.toolbar.addWidget(self.urlbar)
        

    def update_Addressbar(self , url):
        self.urlbar.setText(url.toString())
        self.urlbar.setCursorPosition(0)

    def home(self):
        self.browser.setUrl(QUrl('https://google.com'))

    def url_bar(self, url: QUrl):
        if url.scheme() == '':
            url.setScheme('https://')
        self.browser.setUrl(url)
        self.update_Addressbar(url)


app=QApplication(sys.argv)
form=Form()
form.show()
sys.exit(app.exec())