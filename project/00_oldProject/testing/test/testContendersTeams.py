from model.contendersTeams import contendersTeams
import pandas as pd
if __name__=="__main__":

    folderPath = '../../data/testData'
    
    print('_________CONSTRUCTOR__________TEST1')

    # new auction
    l = ['Alberto','Giacomo','Giovanni']
    d = contendersTeams(True,l,folderPath)
    print(d.contendersTeams)

    # load auction
    c = contendersTeams(False,[],folderPath)
    print(c.contendersNames)
    print(c.contendersTeams["Alberto"].head(3))
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


    # print('T3_________RejectPlayer__________!')
    # print('d.trashPlayers_BEFORE',d.trashPlayers)
    # d.rejectPlayer(playerDF)
    # print('d.trashPlayers_AFTER',d.trashPlayers)
    # print('history',d.historyInsertion)
    # print('__T3_PASSED')
    # print(' ')
    # print(' ')


    # print('T4_________HistoryInsertion__________!')
    # print('BEFORE')
    # print(d.historyInsertion)
    # print(d.trashPlayers)
    # d.backOne()
    # print('AFTER')
    # print(d.historyInsertion)
    # print(d.trashPlayers)
    # print(d.contendersTeams['Alberto'])
    # print(' ')
    # print(' ')
    

    # print('T5_________SaveAll__________!')
    # d.saveAll(folderPath)