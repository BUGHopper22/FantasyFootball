import pandas as pd
from .contendersTeams import contendersTeams 
from .roleLists import roleList 


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
            self.contendersTeams = self.contendersTeams()
            self.roleLists = self.roleLists()
        else:
            print('loadDataFromFiles')

    def setContendersNames(self, contendersNames):
        self.contendersTeams.setContendersNames(contendersNames)

    def randomPlayer(self,roleName):
        print("randomPlayer")
        return self.roleLists.randomPlayer(roleName)

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