from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QFileDialog 
from PySide2.QtCore import QDir
from model.fantasyFootball import fantasyFootball
from gui.p01_introduction import introductionPage
from gui.p02_contender import contenderPage
from gui.p03_roleButton import roleButtonPage
from gui.p04_auction import auctionPage

class mainPage(QWidget):
    
    

    def __init__(self):
        super(mainPage, self).__init__()

        self.fantasyFootball = fantasyFootball()

        self.resize(500,500)
        self.setWindowTitle("Fantasy football")

        self.introductionPage = introductionPage()
        self.contenderPage = contenderPage(self.fantasyFootball)
        self.roleButtonPage = roleButtonPage(self.fantasyFootball)
        # self.auctionPage = auctionPage(self.fantasyFootball,'')

        self.introductionPage.setVisible(True)
        self.contenderPage.hide()
        self.roleButtonPage.hide()
        # self.auctionPage.hide()

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.introductionPage)
        self.layout.addWidget(self.contenderPage)
        self.layout.addWidget(self.roleButtonPage)
        # self.layout.addWidget(self.auctionPage)

        self.introductionPage.startAuction.clicked.connect(self.startAuctionAction)
        self.introductionPage.loadAuction.clicked.connect(self.loadAuctionAction)

        self.contenderPage.contenderFinishButton.clicked.connect(self.finishContenderAction)
        


        # self.roleButtonPage.goalkeeperButton.clicked.connect(lambda: self.roleButtonAction('goalkeeper')) OPEN PAGE IN NEW WINDOW
        self.roleButtonPage.goalkeeperButton.clicked.connect(lambda: self.roleButtonAction('goalkeeper'))
        self.roleButtonPage.defenderButton.clicked.connect(lambda: self.roleButtonAction('defender'))
        self.roleButtonPage.midfielderButton.clicked.connect(lambda: self.roleButtonAction('midfielder'))
        self.roleButtonPage.forwardButton.clicked.connect(lambda: self.roleButtonAction('forward'))


        

        self.setLayout(self.layout)

    def startAuctionAction(self):
        print('OK')
        self.introductionPage.hide() 
        self.contenderPage.setVisible(True)
        

    def loadAuctionAction(self):
        # fd = QFileDialog()
        # fd.setOption(tr('0x00000001'), True)
        # path_to_file = fd.getOpenFileName(self, self.tr("Load Fasta"), self.tr("./data") , self.tr("Folders"))
        # path_to_file = fd.getOpenFileName(self, self.tr("Load Fasta"), self.tr("./data") , self.tr("Folders"))

        dirToLoad = QFileDialog.getExistingDirectory(self, self.tr("Open Directory"),
                                            self.tr("Load Fasta"),
                                            QFileDialog.ShowDirsOnly or QFileDialog.DontResolveSymlinks)

        print('CALL LOAD DATA FROM PAGE BUTTON')
        self.fantasyFootball = fantasyFootball(isNewAuction = False, folderPath = dirToLoad)
        
        self.introductionPage.hide() 
        self.roleButtonPage.setVisible(True)

    def finishContenderAction(self):
        print('OK')
        self.contenderPage.hide()
        self.roleButtonPage.setVisible(True)
        print(self.contenderPage.lineEditText)
        print(self.fantasyFootball.contendersTeams.contendersNames)
        print(self.fantasyFootball.roleLists.goalkeeperDF)

    def roleButtonAction(self,role):
        print(role)
        print(self.fantasyFootball.contendersTeams.contendersNames)

        self.auctionPage = auctionPage(self.fantasyFootball,role)
        self.layout.addWidget(self.auctionPage)
        # self.auctionPage.setRole(role)
        
        # self.auctionPage.createContendentButtonsGroup()
        # self.auctionPage.externalLayout.update()
        self.roleButtonPage.hide()
        # self.auctionPage.setVisible(True)

        self.auctionPage.backToRole.clicked.connect(self.backToRoleAuction)

    def backToRoleAuction(self):
        self.auctionPage.hide()
        self.roleButtonPage.setVisible(True)

