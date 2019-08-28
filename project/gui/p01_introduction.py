from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout

class introductionPage(QWidget):
    def __init__(self):
        super(introductionPage, self).__init__()

        self.startAuction = QPushButton('Start new auction')
        self.loadAuction = QPushButton('Load auction')
        self.exitAuction = QPushButton('Exit')

        self.startAuction.setMinimumHeight(150)
        self.loadAuction.setMinimumHeight(150)
        self.exitAuction.setMinimumHeight(150)
        self.loadAuction.setEnabled(False)
        

        # b2.setVisible(False)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.startAuction)
        self.layout.addWidget(self.loadAuction)
        self.layout.addWidget(self.exitAuction)

        

        self.setLayout(self.layout)