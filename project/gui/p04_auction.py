from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QGridLayout

class auctionPage(QWidget):
    def __init__(self,fantasyFootball,role):
        super(auctionPage, self).__init__()

        self.fantasyFootball = fantasyFootball
        self.role = role

        self.externalLayout = QVBoxLayout()

        self.externalLayout.addWidget(self.createRandomGroup())
        self.externalLayout.addWidget(self.createContendentButtonsGroup())
        self.externalLayout.addWidget(self.createUtilityButtonsGroup())
        self.setLayout(self.externalLayout)

        

        self.setLayout(self.externalLayout)

    def setRole(self,role):
        self.role = role

    # _________METHODS TO CREATE GUI GROUPS___________________
    def createRandomGroup(self):
        self.randomGroup = QGroupBox('random player')

        self.randomButton = QPushButton()
        self.randomButton.setText('random ' + self.role)
        self.randomPlayerName = QLabel('')
        self.randomPlayerTeam = QLabel('')
        self.randomPlayerQuote = QLabel('')

        self.vBox = QVBoxLayout()
        self.vBox.addWidget(self.randomButton)
        self.vBox.addWidget(self.randomPlayerName)
        self.vBox.addWidget(self.randomPlayerTeam)
        self.vBox.addWidget(self.randomPlayerQuote)
        
        self.randomGroup.setLayout(self.vBox)

        self.randomButton.clicked.connect(self.randomButtonAction)
        return self.randomGroup

    # SLOT
    def randomButtonAction(self):

        print(self.fantasyFootball.roleLists.goalkeeperDF)

        # setButton disable or enable
        for button in self.buttonDict.values():
            button.setEnabled(True)
        self.randomButton.setEnabled(False)

        # if rolePlayerDF is empty
        if (    (self.role == 'goalkeeper' and self.fantasyFootball.roleLists.goalkeeperDF.empty) or
                (self.role == 'midfielder' and self.fantasyFootball.roleLists.midfielderDF.empty) or
                (self.role == 'defender' and self.fantasyFootball.roleLists.defenderDF.empty) or
                (self.role == 'forward' and self.fantasyFootball.roleLists.forwardDF.empty)
            ):
            self.randomPlayerName.setText('no more ' + self.role + ' to choose')
            self.randomPlayerTeam.setText('')
            self.randomPlayerQuote.setText('')
        else:
            self.singlePlayer = self.fantasyFootball.randomPick(self.role)
            # toPrint = name + squadra + quota iniziale
            toPrint = [] 
            toPrint.append(self.singlePlayer.iloc[0,2])
            toPrint.append(self.singlePlayer.iloc[0,3])
            toPrint.append(str(self.singlePlayer.iloc[0,5]))
            
            self.randomPlayerName.setText('Name:  ' + toPrint[0])
            self.randomPlayerTeam.setText('Team:  ' + toPrint[1])
            self.randomPlayerQuote.setText('Quote:  ' + toPrint[2])
            
            # self.randomPlayerText.setText(singlePlayer)

    def createContendentButtonsGroup(self):
        self.contendentGroup = QGroupBox('insert player in contender teams')
        self.GBox = QVBoxLayout()
        print('createContendentButtonsGroup')
        
        self.buttonDict = {}
        self.buttonL = []
        for name in self.fantasyFootball.contendersTeams.contendersNames:
            self.buttonDict[name] = QPushButton(name)
            self.buttonDict[name].setEnabled(False)
            
            self.GBox.addWidget(self.buttonDict[name])

            self.buttonL.append(self.buttonDict[name])
            print(name)

            self.buttonDict[name].clicked.connect(lambda x=False, i=name: self.insertPlayerInTeam(x,i))

        
        

        self.contendentGroup.setLayout(self.GBox)
        return self.contendentGroup

    # SLOT
    # IMPORTANTEEEEEEEEEEEEEE REJECTED PLAYER E' UN CASO  PARTICOLARE E BISOGNA CHIAMARE LA FUNZIONE REJECTEDPLAYER DI CONTENDERSTEAM
    def insertPlayerInTeam(self,isClicked,name):
        for button in self.buttonDict.values():
            button.setEnabled(False)
        self.randomButton.setEnabled(True)
        print(name)
        self.fantasyFootball.addPlayerToTeam(name,self.singlePlayer)
        print(self.fantasyFootball.contendersTeams.contendersTeams)


    def createUtilityButtonsGroup(self):
        self.utilityGroup = QGroupBox('')

        self.backOneButton = QPushButton()
        self.backOneButton.setText('back one')
        self.discardsButton = QPushButton()
        self.discardsButton.setText('restore discards')
        self.saveButton = QPushButton()
        self.saveButton.setText('save and change role')
        
        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.backOneButton)
        self.hBox.addWidget(self.discardsButton)
        self.hBox.addWidget(self.saveButton)
        
        self.utilityGroup.setLayout(self.hBox)

        self.backOneButton.clicked.connect()
        self.discardsButton.clicked.connect()
        self.saveButton.clicked.connect()
        return self.utilityGroup