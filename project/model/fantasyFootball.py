import pandas as pd
from model.contendersTeams import contendersTeams 
from model.roleLists import roleLists


class fantasyFootball():
    
    # roleLists = roleLists()
    contendersTeams = contendersTeams()
    roleLists = roleLists() 


    def __init__(self, isNewAuction = True, folderPath = ''):
        print("start")
        newAuction  = True
        # build fields by default
        if newAuction:
            print('newAuction')
            # crea contendersName vuoti
            self.contendersTeams = contendersTeams()
            self.roleLists = roleLists()
            print(self.roleLists.playersRemainDF)
            print(self.roleLists.goalkeeperDF)
        else:
            print('loadDataFromFiles')

    def setContendersNames(self, contendersNames):
        self.contendersTeams.setContendersNames(contendersNames)
        print('TESTTTTTTT')
        print(self.fantasyFootball.contendersTeams.contendersTeams)

    def randomPick(self,roleName):
        print("randomPlayer")
        #  return a list of string
        singlePlayer = self.roleLists.randomPick(roleName)
        
        
        return singlePlayer


    def addPlayerToTeam(self,contenderName,playerDF):
        print("addPlayerToTeam")
        if contenderName is 'rejected':
            self.contendersTeams.rejectPlayer(playerDF)
        else:
            self.contendersTeams.addValueToTeam(contenderName,playerDF)
    
    def saveAuciton(self):
        print("saveAuction")
        folderPath = '??'
        self.contendersTeams.saveAll(folderPath)
        self.roleLists.saveAll(folderPath)
        

    def backOne():
        print("backOne")

    

    

    def loadFromFolder(self):
        print("loadFromFolder")

    # def saveContendersName():
    #     print("saveContendersName")

    def createFinalOutput():
        print("createFinalOutput")