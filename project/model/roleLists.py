import pandas as pd
from model.contendersTeams import  contendersTeams

class roleLists():
    def __init__(   self,
                    isNewAuction = True,
                    folderPath = ''
                ):
        if isNewAuction:
            print('insert data in rolePlayer')
            self.playersRemainDF = pd.read_csv('./data/default/Quotazioni_Fantacalcio.csv')
            self.goalkeeperDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='P']
            self.defenderDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='D']
            self.midfielderDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='C']
            self.forwardDF = self.playersRemainDF.loc[self.playersRemainDF['R']=='A']
        else:
            # in questo caso devi caricarli da file csv, controlla dopo FORSE SI POSSONO EVITARE I SETTER
            self.goalkeeperDF = pd.read_csv(folderPath)
            self.defenderDF = pd.read_csv(folderPath)
            self.midfielderDF = pd.read_csv(folderPath)
            self.forwardDF = pd.read_csv(folderPath)

    def goalkeeperFromCsv(self,path):
        self.goalkeeper = pd.read_csv(path)
        
    def setDefenderFromCsv(self,path):
        self.defender = pd.read_csv(path)

    def setMidfielderFromCsv(self,path):
        self.midfielder = pd.read_csv(path)

    def setForwardFromCsv(self,path):
        self.forward = pd.read_csv(path)

    # return a randomPlayerDF and remove it from DFParameter
    def randomPick(self,roleName):
        if roleName is 'goalkeeper':
            # print(self)
            randomPlayer = self.goalkeeperDF.sample(n=1,replace=True)
            # get id
            idPlayer = randomPlayer.iloc[0,0]
            # remove id from DF
            self.goalkeeperDF = self.goalkeeperDF[self.goalkeeperDF.Id != idPlayer]

        if roleName is 'defender':
            randomPlayer = self.defenderDF.sample(n=1,replace=True)
            idPlayer = randomPlayer.iloc[0,0]
            self.defenderDF = self.defenderDF[self.defenderDF.Id != idPlayer]

        if roleName is 'midfielder':
            randomPlayer = self.midfielderDF.sample(n=1,replace=True)
            idPlayer = randomPlayer.iloc[0,0]
            self.midfielderDF = self.midfielderDF[self.midfielderDF.Id != idPlayer]
            
        if roleName is 'forward':
            randomPlayer = self.forwardDF.sample(n=1,replace=True)
            idPlayer = randomPlayer.iloc[0,0]
            self.forwardDF = self.forwardDF[self.forwardDF.Id != idPlayer]
        return randomPlayer

    def saveAll(self,folderPath):
        self.goalkeeper.to_csv(folderPath + '/goalkeeper.csv',index=False)
        self.defender.to_csv(folderPath + '/defender.csv',index=False)
        self.midfielder.to_csv(folderPath + '/midfielder.csv',index=False)
        self.forward.to_csv(folderPath + '/forward.csv',index=False)

    # to use in case of back button
    def addPlayer(self,playerDF,role):
        if role is 'goalkeeper':
            self.goalkeeper.append(playerDF)
        if role is 'defender':
            self.defender.append(playerDF)
        if role is 'midfielder':
            self.midfielder.append(playerDF)
        if role is 'forward':
            self.forward.append(playerDF)

# _____molto importante___get single random value____!!!!
# return random value of id column from dataframe
# randomId = self.goalkeeper['Id'].sample(n=1).iloc[0]
# print('randomId',randomId)


