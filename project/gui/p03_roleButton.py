from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QButtonGroup

class roleButtonPage(QWidget):
    def __init__(self,fantasyFootball):
        super(roleButtonPage, self).__init__()

        self.fantasyFootball = fantasyFootball

        self.goalkeeperButton = QPushButton('goalkeeper')
        self.defenderButton = QPushButton('defender')
        self.midfielderButton = QPushButton('midfielder')
        self.forwardButton = QPushButton('forward')

        self.goalkeeperButton.setMinimumHeight(100)
        self.defenderButton.setMinimumHeight(100)
        self.midfielderButton.setMinimumHeight(100)
        self.forwardButton.setMinimumHeight(100)

        self.saveAllButton = QPushButton('save Auction')
        self.saveAllButton.clicked.connect(self.saveAllAction)

        self.layout = QVBoxLayout()

        # self.layout.addWidget(self.groupButton)
        self.layout.addWidget(self.goalkeeperButton)
        self.layout.addWidget(self.defenderButton)
        self.layout.addWidget(self.midfielderButton)
        self.layout.addWidget(self.forwardButton)
        self.layout.addWidget(self.saveAllButton)
        # self.layout.addWidget(self.b1)

        

        self.setLayout(self.layout)

    def saveAllAction(self):
        self.fantasyFootball.saveAuction()