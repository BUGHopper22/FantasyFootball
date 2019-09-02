from PySide2.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGroupBox, QHBoxLayout, QLabel, QGridLayout, QListWidget 

class auctionPage(QWidget):
    def __init__(self,fantasyFootball,role):
        super(auctionPage, self).__init__()

        self.fantasyFootball = fantasyFootball
        self.role = role


        self.externalLayout = QHBoxLayout()
        self.externalLayout.addWidget(self.sxGroupBox())
        self.externalLayout.addWidget(self.dxGroupBox())
        self.setLayout(self.externalLayout)

        

        

        

    def sxGroupBox(self):
        self.sxGroupBox = QGroupBox('new Player')

        self.auctionLayout = QVBoxLayout()
        self.auctionLayout.addWidget(self.createRandomGroup())
        self.auctionLayout.addWidget(self.createContendentButtonsGroup())
        self.auctionLayout.addWidget(self.createUtilityButtonsGroup())
        self.sxGroupBox.setLayout(self.auctionLayout)

        return self.sxGroupBox






    def dxGroupBox(self):
        self.dxGroupBox = QGroupBox('Teams')

        self.teamListLayout = QGridLayout()
        i = 0
        self.listWidgetCol = {}
        self.removeButtonList = {}

        for contender in self.fantasyFootball.contendersTeams.contendersNames:
            self.titleList = QLabel(contender)

            self.listWidgetCol[contender] = QListWidget()

            

            i_button = 0
            for singlePlayer in self.fantasyFootball.contendersTeams.contendersTeams[contender].iterrows(): 
                print('singlePlayer = ',singlePlayer)
                playerToAdd = singlePlayer[1]
                playerName = playerToAdd.get(key = 'Nome')
                playerRole = playerToAdd.get(key = 'R')
                finalString = playerRole + ' ' + playerName
                self.listWidgetCol[contender].addItem(finalString)

                
            self.removeButtonList[contender] = (QPushButton('Remove Selected'))
            self.removeButtonList[contender].setEnabled(False)
            self.removeButtonList[contender].clicked.connect(lambda x=False, contender=contender: self.removeFromContender(x,contender))

            print('i',i)
            
            self.teamListLayout.setColumnMinimumWidth(i,130)
            # self.teamListLayout.setColumnMinimumWidth(i+1,1)

            self.teamListLayout.addWidget(self.titleList,0,i)
            
            self.teamListLayout.addWidget(self.listWidgetCol[contender],1,i)
            self.teamListLayout.addWidget(self.removeButtonList[contender],2,i)
            
            i += 1

        self.dxGroupBox.setLayout(self.teamListLayout)
        return self.dxGroupBox

    def removeFromContender(self,isClicked,contender):

        itemSelected = self.listWidgetCol[contender].selectedItems()
        print(itemSelected)
        print(itemSelected)
        print(itemSelected)
        print(itemSelected)
        if itemSelected: 
            print("ECCOLO")
            # self.listWidgetCol[contender].takeTopLevelItem(itemSelected)
            # self.fantasyFootball.backOne()

        # else:
        #     self.
        # for item in listItems:
        #     itemIndex=self.listA.indexOfTopLevelItem(item)
        #     self.listA.takeTopLevelItem(itemIndex)
        # print '\n\t Number of items remaining', self.listA.topLevelItemCount()



        # check if is possible to return player or we are in another role aution
        # if (len(self.fantasyFootball.contendersTeams.contendersTeams[contender]) == 0):
        #     self.reintegrateButton.setEnabled(False)
        # else:
        #     self.reintegrateButton.setEnabled(True)
        #     self.fantasyFootball.backOne()

        #     lastContender = self.historyInsertion[len(self.historyInsertion)-1]
        #     # remove last item insert
        #     self.listWidgetCol[lastContender].takeItem(self.listA.row(item))
        #     self.listWidgetCol[lastContender].item((QStringList.size()-1)).setSelected(True)






    # def createsingleListView(self):
    #     print('p')
    #     self.test = QLabel('dfizuvhp')
    #     return self.test

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

    

    def createContendentButtonsGroup(self):
        self.contendentGroup = QGroupBox('insert player in contender teams')
        self.GBox = QVBoxLayout()
        print('createContendentButtonsGroup')
        
        self.buttonDict = {}
        # buttonL non utilizzato, potrebbe servire?
        self.buttonL = []
        for name in self.fantasyFootball.contendersTeams.contendersNames:
            self.buttonDict[name] = QPushButton(name)
            self.buttonDict[name].setEnabled(False)
            
            self.GBox.addWidget(self.buttonDict[name])

            self.buttonL.append(self.buttonDict[name])

            self.buttonDict[name].clicked.connect(lambda x=False, i=name: self.insertPlayerInTeam(x,i))
        self.contendentGroup.setLayout(self.GBox)
        return self.contendentGroup

    def createUtilityButtonsGroup(self):
        self.utilityGroup = QGroupBox('')

        self.backToRole = QPushButton()
        self.backToRole.setText('back to roles')
        
        self.hBox = QHBoxLayout()
        self.hBox.addWidget(self.backToRole)
        
        self.utilityGroup.setLayout(self.hBox)


        # self.backToRole.clicked.connect is implement in page 0

        return self.utilityGroup
    
    # SLOT utility buttons
    def reintegrateAction(self):
        # check if is possible to return player or we are in another role aution

            lastContender = self.historyInsertion[len(self.historyInsertion)-1]
            # remove last item insert
            self.listWidgetCol[lastContender].takeItem(self.listA.row(item))
            self.listWidgetCol[lastContender].item((QStringList.size()-1)).setSelected(True)
            # self.listWidgetCol[contender].remove

        # if self.fantasyFootball.checkRole(self.role):
        #     self.reintegrateButton.setEnabled(True)
            
        #     self.fantasyFootball.backOne(self.role)

    def discardsButtonAction(self):
        self.fantasyFootball.discardRejected()


    # SLOT click teamName
    # check if rejected in ok
    def insertPlayerInTeam(self,isClicked,name):
        # reset random playerView
        self.randomPlayerName.setText('')
        self.randomPlayerTeam.setText('')
        self.randomPlayerQuote.setText('')

        # setButton disable or enable
        for button in self.buttonDict.values():
            button.setEnabled(False)
        self.randomButton.setEnabled(True)

        self.fantasyFootball.addPlayerToTeam(name,self.singlePlayer)
        print('________ALL REMAIN PLAYER TEST WITH GOALKEEPER____________')
        print(self.fantasyFootball.roleLists.goalkeeperDF)
        print('________ALL CONTENDER TEAMS____________')
        print(self.fantasyFootball.contendersTeams.contendersTeams)

        playerToAdd = self.singlePlayer.iloc[0,2]
        self.listWidgetCol[name].addItem(playerToAdd)

    # SLOT click random button
    def randomButtonAction(self):
        # check if possible to turn back a player or not and set right button visibility
        print(self.fantasyFootball.checkRole(self.role))
        print(self.role)
        print(len(self.fantasyFootball.contendersTeams.historyInsertion))
        print(len(self.fantasyFootball.contendersTeams.historyInsertion))
        print(len(self.fantasyFootball.contendersTeams.historyInsertion))
        print(len(self.fantasyFootball.contendersTeams.historyInsertion))
        print(len(self.fantasyFootball.contendersTeams.historyInsertion))

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
            # name
            toPrint.append(self.singlePlayer.iloc[0,2])
            # team
            toPrint.append(self.singlePlayer.iloc[0,3])
            # quote
            toPrint.append(str(self.singlePlayer.iloc[0,5]))
            
            self.randomPlayerName.setText('Name:  ' + toPrint[0])
            self.randomPlayerTeam.setText('Team:  ' + toPrint[1])
            self.randomPlayerQuote.setText('Quote:  ' + toPrint[2])
            


    