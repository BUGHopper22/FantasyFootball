import pandas as pd
import csv
import os

class contendersTeams():

    historyInsertion = []
    trashPlayers = pd.DataFrame()
    contendersNames = []
    # lista contenente i teams dei contenders {'contender1':{team1},'contender2':{team2}}
    contendersTeams = {}

    def __init__(self,isNewAuction = True, contendersNames = [], folderPath = ''):
        print('isNewAuction',isNewAuction)
        # case : new auction
        if isNewAuction:
            # contenderName
            self.contendersNames = list(contendersNames)
            #contender Team
            for name in self.contendersNames:
                self.contendersTeams[name] = pd.DataFrame()
            # historyInsertion
            self.historyInsertion = []
        # case : load from files
        else:
            # contenderName
            print('costruisce contenderTeams da files')
            contendersNamesDF = pd.read_csv(folderPath + '/contendersNames.csv')
            
            for i in range(0,contendersNamesDF.size):
                name = contendersNamesDF.iloc[i,0]
                teamName = pd.read_csv(folderPath + '/contendersTeams/' + name + '.csv')
                self.contendersNames.append(name)
                self.contendersTeams.update({name : teamName})
            # historyInsertion
            self.historyInsertion = []
    
    def setContendersNames(self, contendersNames):
        self.contendersNames = list(contendersNames)
        self.contendersNames.append('rejected')
        for name in self.contendersNames:
            self.contendersTeams[name] = pd.DataFrame()
        # self.contendersTeams['rejected'] = pd.DataFrame()
    
    def checkRole(self,roleTocheck):
        isRightRole = False
        print(len(self.historyInsertion))
        print(len(self.historyInsertion))
        print(len(self.historyInsertion))
        print(len(self.historyInsertion))
        if len(self.historyInsertion) is not 0:
            print('la size è maggiore di zero')
            lastContender = self.historyInsertion[len(self.historyInsertion)-1]
            lastInsertRole = self.contendersTeams[lastContender].iloc[0,1]
            
            if( lastInsertRole == 'P'):
                role = 'goalkeeper'
            if( lastInsertRole == 'D'):
                role = 'defender'
            if( lastInsertRole == 'C'):
                role = 'midfielder'
            if( lastInsertRole == 'A'):
                role = 'forward'
            
            
            
            
            print(roleTocheck,'==',role)
            if roleTocheck is role:
                isRightRole = True
        return isRightRole


    # the andom player was already remove from main dataframe
    def addValueToTeam(self,contenderName,playerDF):
        # update history
        print('BEFOREHIS',len(self.historyInsertion))
        self.historyInsertion.append(contenderName)
        print('AFTERHIS',len(self.historyInsertion))
        self.contendersTeams[contenderName] = self.contendersTeams[contenderName].append(playerDF)



    # rifatto ma nella lista dei contenderTeams nell'ultimo tema c è rejected team!!!!!
    # def rejectPlayer(self,playerDF):

    #     self.historyInsertion.append('rejected')
    #     self.trashPlayers = self.trashPlayers.append(playerDF)

    # return last player insert in team and drop its
    def backOne(self):

        lastContender = self.historyInsertion[len(self.historyInsertion)-1]
        del self.historyInsertion[len(self.historyInsertion)-1]
        
        if lastContender is 'rejected':

            lastInsertDF = self.trashPlayers.tail(1)
            # remove last row
            self.trashPlayers.drop(self.trashPlayers.tail(1).index,inplace=True)
        else:
            # prendo il player dal team in cui lo avevo inserito
            lastInsertDF = self.contendersTeams[lastContender].tail(1)
            # remove last row
            self.contendersTeams[lastContender].drop(self.contendersTeams[lastContender].index,inplace=True)

        
        return lastInsertDF

    def saveAll(self,folderPath):
        # Alberto.csv, Giovanni.csv, Giacomo.csv, contenderName.csv

        # convert list in DF 
        contendersNamesDict = {'name':self.contendersNames}
        contendersNamesDF = pd.DataFrame(data=contendersNamesDict)
        contendersNamesDF.to_csv(folderPath + '/contendersNames.csv',index=False)
        

        contenderTeamsFolder = folderPath + '/contendersTeams/'
        # create a folder if not exhist
        if not os.path.exists(contenderTeamsFolder):
            print('non esiste ', contenderTeamsFolder)
            os.makedirs(contenderTeamsFolder)

        for name in self.contendersNames:
            self.contendersTeams[name].to_csv(contenderTeamsFolder + name + '.csv',index=False)


        

        # POTREBBE ESSERCI UN PROBLEMA CON IL '.' PRIMO ELEMENTO DELLA RIGAA
        # if os.path.exists(folderPath + '/contendersNames.csv'):  
        #     os.remove(folderPath + '/contendersNames.csv')
    

        


    




if __name__ == "__main__":
    print('T1_________CONSTRUCTOR__________!')

    # new auction
    l = ['Alberto','Giacomo','Giovanni']
    d = contendersTeams(True,l,'../data/testData')
    print(d.contendersTeams)

    # load auction
    c = contendersTeams(False,[],'../data/testData')
    print(c.contendersNames)
    print(c.contendersTeams["Alberto"])
    print('__T1_PASSED')
    print(' ')
    print(' ')


    print('T2_________addValueToTeam__________!')
    playerDF = c.contendersTeams['Giovanni'].tail(1)
    print('Toadd')
    print(playerDF)
    print('PRE')
    print(d.contendersTeams['Alberto'])
    d.addValueToTeam('Alberto',playerDF)
    print('POST')
    print(d.contendersTeams['Alberto'])
    print('history',d.historyInsertion)
    print('__T2_PASSED')
    print(' ')
    print(' ')


    print('T3_________RejectPlayer__________!')
    print('d.trashPlayers_BEFORE',d.trashPlayers)
    d.rejectPlayer(playerDF)
    print('d.trashPlayers_AFTER',d.trashPlayers)
    print('history',d.historyInsertion)
    print('__T3_PASSED')
    print(' ')
    print(' ')


    print('T4_________HistoryInsertion__________!')
    print('BEFORE')
    print(d.historyInsertion)
    print(d.trashPlayers)
    d.backOne()
    print('AFTER')
    print(d.historyInsertion)
    print(d.trashPlayers)
    print(d.contendersTeams['Alberto'])
    print(' ')
    print(' ')
    

    print('T5_________SaveAll__________!')
    d.saveAll('../data/testData')

    

    