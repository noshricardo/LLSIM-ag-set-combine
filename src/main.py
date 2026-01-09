# by Noah Richards
# do not redistribute


import csv
import pandas


setDat = pandas.read_csv('../DataFiles/setDat.csv')
#print(setDat.loc[1:3])

agDat = pandas.read_csv('../DataFiles/agDat.csv')
#print(agDat.loc[1:3])

resDat = pandas.DataFrame(columns=setDat.columns)

#resDat = resDat._append(setDat.iloc[1])
#print(resDat)


for row, data in agDat.iterrows():
    print('processing year')
    print(data['year'])
    print('')
    #print("agregate data")
    #print(data)
    #print("")
    #if data['year'] == 2007:
        #break
    for index, set in setDat.iterrows():
        #print(sets['year'])
        #print(sets)
        if (set['year'] == data['year']) & (set['season'] == data['season']) & (set['program'] == data['program']):
            #print("set data")
            #print(set)
            #print("")
            resDat = resDat._append(set)
    sumHooks = 0
    sumSets = 0
    largetSet = 0
    for index, res in resDat.iterrows():
          if (res['year'] == data['year']) & (res['season'] == data['season']) & (res['program'] == data['program']):
            #print('true')
            sumHooks += res['hooks'].__int__()
            sumSets += 1
            if largetSet < res['set']:
                largetSet = res['set']
    neededHooks = 0
    neededSets = 0
    remainingNeededHooks = 0
    avgHooksPerNeededSet = 0
    #print(sumHooks)
    #print(data['hooks'])
    if sumHooks < data['hooks']:
        #print('hook and set calc')
        neededHooks = (data['hooks'].__int__() - sumHooks).__int__()
        neededSets = (data['sets'].__int__() - sumSets).__int__()
        #print(neededHooks)
        #print(neededSets)
        avgHooksPerNeededSet = (int)(neededHooks/neededSets)
        #print(avgHooksPerNeededSet)
        remainingNeededHooks = neededHooks%neededSets
        #print(remainingNeededHooks)
    #print('needed sets')
    #print(neededSets)
    #print("iter needed sets")
    for x in range(neededSets):
        #print(x)
        if x == neededSets -1:
            Hooks = avgHooksPerNeededSet + remainingNeededHooks
        else:
            Hooks = avgHooksPerNeededSet
        resDat = resDat._append({'year': data['year'] ,'season': data['season'],'Trip': data['trips'] + 1,'set': largetSet + x + 1,'hooks': Hooks,'species': 0.0,'Numb': 0.0,'program': data['program'],'EorW': 1.0,'CPUE(per 1k hooks)': 0.0}, ignore_index=True)

    
print(resDat)
resDat.to_csv("output.csv")
