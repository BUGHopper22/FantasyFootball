import pandas as pd
from model.contendersTeams import contendersTeams 
from model.roleLists import roleLists
import os


class fantasyFootball():
    
    # roleLists = roleLists()
    contendersTeams = contendersTeams()
    roleLists = roleLists() 


    def __init__(self, isNewAuction = True, folderPath = ''):
        print("start")
        # build fields by default
        if isNewAuction:
            print('newAuction in fantasyFootball')
            # crea contendersName vuoti
            self.contendersTeams = contendersTeams()
            self.roleLists = roleLists()
        else:

            print('loadDataFromFiles')
            self.loadFromFolder(folderPath)

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
    
    def saveAuction(self):
        print("saveAuction called")
        folderPath = './data/save'
        

        # check file in  directory
        # for (dirpath, dirnames, filenames) in os.walk(folderPath):
        #     print(filenames)

        self.contendersTeams.saveAll(folderPath)
        self.roleLists.saveAll(folderPath)
        
    def checkRole(self,roleTocheck):
        toP = self.contendersTeams.checkRole(roleTocheck)
        print('final',toP)
        print('final',toP)
        print('final',toP)
        print('final',toP)
        return toP


    def backOne(self):
        
        

        # remove last player insert in contender team
        self.lastPlayerInsert = self.contendersTeams.backOne()

        # check the rigth role
        if( self.lastPlayerInsert.iloc[0,1] == 'P'):
            role = 'goalkeeper'
        if( self.lastPlayerInsert.iloc[0,1] == 'D'):
            role = 'defender'
        if( self.lastPlayerInsert.iloc[0,1] == 'M'):
            role = 'midfielder'
        if( self.lastPlayerInsert.iloc[0,1] == 'F'):
            role = 'forward'

        print(type(self.lastPlayerInsert))
        print(self.lastPlayerInsert)
        print(self.lastPlayerInsert.iloc[0,1])
        
        # add lastPlayer to adeguate role list
        self.roleLists.addPlayer(self.lastPlayerInsert,role)

    def discardRejected(self):
        print('discard rejected called')

    def loadFromFolder(self, folderPath):
        print("loadFromFolder")
        self.contendersTeams = contendersTeams(isNewAuction = False, contendersNames = None,folderPath = folderPath)
        print('DA FARE ROLE LIST LOAD NON FATTA!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
        # self.roleLists. = roleLists(isNewAuction = False,folderPath)

    # def saveContendersName():
    #     print("saveContendersName")

    def createFinalOutput():
        print("createFinalOutput")