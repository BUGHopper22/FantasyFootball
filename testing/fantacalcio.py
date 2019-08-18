import pandas as pd
import numpy as np
import numpy.random as random


def divideForRole(playersData):
    AttaccantiDF =playersData.loc[playersData['R']=='A']
    CentrocampistiDF =playersData.loc[playersData['R']=='C']
    PortieriDF =playersData.loc[playersData['R']=='P']
    DifensoriDF = playersData.loc[playersData['R']=='D']
    
    return AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF

# per ogni elemento
    # scegli un numero random tra gli Id del dataframe
    # estrarre singleRoleDF.axes della row random
    # stampare la row
    # eliminare la row
def randomPick(singleRoleDF):

    print('RANDOM PICK START ____________________________________________')
    contenderTeamList = {
        "Giulio": pd.DataFrame(),
        "Federico": pd.DataFrame(),
    }
    # mantain a history of insertion to come back in case of errors
    # example ['Giulio','Giulio','Federico','Giulio','Pippo']
    historyOfContenderInsertion = []
    # serie with all Id Values
    idsSeries = singleRoleDF['Id']
    for col, player in singleRoleDF.iterrows():
        input("Press Enter to continue...")
        # serie with random Id as value
        randomIdFromSerie = idsSeries.sample(n=1)

        # random id as integer
        randomID = randomIdFromSerie.iloc[0]

        # single line dataframe with picked player
        playerPicked = singleRoleDF.loc[singleRoleDF['Id'] == randomID]
    
        print(playerPicked)
        # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        # drop 
        idsSeries = idsSeries[idsSeries.iloc[:] != randomID]

        # TEST____________________________
        giulio = 'Giulio'
        federico = 'Federico'
        if((randomID % 2) == 0):
            insertPlayerPickedInContenderTeam(playerPicked,
                                                giulio,
                                                contenderTeamList,historyOfContenderInsertion)
        else:
            insertPlayerPickedInContenderTeam(playerPicked,federico,contenderTeamList,historyOfContenderInsertion)
        # TEST____________________________
        

        # drop line of singleRoleDF where Id == randomID
        SingoloRuoloIdColDF = singleRoleDF.set_index("Id")
        SingoloRuoloIdColDF = SingoloRuoloIdColDF.drop(randomID, axis=0)
        # fa la stessa cosa di drop (decidere quale versisone tenere)
        # singleRoleDF = singleRoleDF[singleRoleDF.Id != randomID]

    # print('_________________________________________')
    # printContendersTeam(contenderTeamList)

    goBackLastInsertion(historyOfContenderInsertion,contenderTeamList,singleRoleDF)

    # print('_________________________________________AFTER GO BACK')
    # printContendersTeam(contenderTeamList)
    print("FINISH")

# (contenderTeamList is a dictionary with contenderName and dataframe of players picked)
# insert playerPicked in contenderTeamList where contenders == contender
def insertPlayerPickedInContenderTeam(playerPicked,contender,contenderTeamList,historyOfContenderInsertion):
    for contenders in contenderTeamList:
        if(contenders == contender):
            contenderTeamList[contender] = contenderTeamList[contender].append(playerPicked)
            historyOfContenderInsertion.append(contender)
    

def printContendersTeam(contenderTeamList):
    print(contenderTeamList)

def goBackLastInsertion(historyOfContenderInsertion,contenderTeamList,singleRoleDF):
    print('************Sei IN GOBACK*************************')
    lastContender = historyOfContenderInsertion[-1]
    del historyOfContenderInsertion[-1]

    # save last player from dataframe of lastContendor
    lastPlayerInsertedInTeam = contenderTeamList[lastContender].tail(1)
    # remove last player from dataframe of lastContendor
    contenderTeamList[lastContender] = contenderTeamList[lastContender][:-1]

    # reinsert lastPlayerInsertedInTeam in singleRoleDF
    singleRoleDF.append(lastPlayerInsertedInTeam)
    print('************fine GOBACK*************************')




if __name__ == "__main__":

    playersData = pd.read_csv('Quotazioni_Fantacalcio.csv')
    AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF = divideForRole(playersData)

    listaRuoli = [AttaccantiDF, CentrocampistiDF, PortieriDF, DifensoriDF]
    for singleRoleDF in listaRuoli:
        randomPick(singleRoleDF)

    # insertPlayerPickedInContenderTeam()
    