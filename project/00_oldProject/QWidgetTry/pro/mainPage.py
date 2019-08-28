from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout
# from PySide2.QtCore import  Signal, Slot

class introductionPage(QWidget):
    
    

    def __init__(self):
        super(introductionPage, self).__init__()

        self.resize(500,500)
        self.setWindowTitle("Fantasy football")

        self.b1 = QPushButton('New auction')
        self.b2 = QPushButton('Load auction')

        self.b1.setMinimumHeight(250)
        self.b2.setMinimumHeight(250)

        self.firstPage = firstPage()
        self.secondPage = secondPage()

        self.firstPage.hide()
        self.secondPage.hide()

        self.b1.clicked.connect(self.goTofirstPage)
        self.b2.clicked.connect(self.goToSecondPage)

        
        self.firstPage.b1.clicked.connect(self.goToMainPageFromFirst)
        self.secondPage.b1.clicked.connect(self.goToMainPageFromSecond)
        
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.b1)
        self.layout.addWidget(self.b2)

        

        self.setLayout(self.layout)

    def goTofirstPage(self):
        self.firstPage.setVisible(True)
        self.hide()

    def goToSecondPage(self):
        self.secondPage.setVisible(True)
        self.hide()

    def goToMainPageFromFirst(self):
        self.setVisible(True)
        self.firstPage.hide()

    def goToMainPageFromSecond(self):
        self.setVisible(True)
        self.secondPage.hide()


class firstPage(QWidget):
    def __init__(self):
        super(firstPage, self).__init__()

        self.resize(500,500)

        self.b1 = QPushButton('firstPage')
        self.setWindowTitle("Fantasy football")

        

        # b2.setVisible(False)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.b1)

        

        self.setLayout(self.layout)

        

        


class secondPage(QWidget):
    def __init__(self):
        super(secondPage, self).__init__()

        self.resize(500,500)

        self.b1 = QPushButton('secondPage')
        self.setWindowTitle("Fantasy football")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.b1)

        

        self.setLayout(self.layout)

        