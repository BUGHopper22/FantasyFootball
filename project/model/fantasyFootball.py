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
        else:
            print('loadDataFromFiles')

    def setContendersNames(self, contendersNames):
        self.contendersTeams.setContendersNames(contendersNames)

    def randomPick(self,roleName):
        print("randomPlayer")
        #  return a list of string
        singlePlayer = self.roleLists.randomPick(roleName)
        
        
        return singlePlayer


    def addPlayerToTeam(self,contenderName,playerDF):
        print("addPlayerToTeam")
        # if contenderName is 'rejected':
        #     print('add player to rejected team')
        #     self.contendersTeams.rejectPlayer(playerDF)
        # else:
        self.contendersTeams.addValueToTeam(contenderName,playerDF)
    
    def saveAuciton(self):
        print("saveAuction called")
        folderPath = '??'
        self.contendersTeams.saveAll(folderPath)
        self.roleLists.saveAll(folderPath)
        

    def backOne(self):
        # remove last player insert in contender team
        self.lastPlayerInsert = self.contendersTeams.backOne()
        print(type(self.lastPlayerInsert))
        print(self.lastPlayerInsert)
        print(self.lastPlayerInsert.iloc[0,1])
        # check the rigth role
        if( self.lastPlayerInsert.iloc[0,1] == 'P'):
            role = 'goalkeeper'
        if( self.lastPlayerInsert.iloc[0,1] == 'D'):
            role = 'defender'
        if( self.lastPlayerInsert.iloc[0,1] == 'M'):
            role = 'midfielder'
        if( self.lastPlayerInsert.iloc[0,1] == 'F'):
            role = 'forward'
        
        # add lastPlayer to adeguate role list
        self.roleLists.addPlayer(self.lastPlayerInsert,role)

    def discardRejected(self):
        print('discard rejected called')

    def loadFromFolder(self):
        print("loadFromFolder")

    # def saveContendersName():
    #     print("saveContendersName")

    def createFinalOutput():
        print("createFinalOutput")