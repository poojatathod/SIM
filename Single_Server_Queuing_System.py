globaldict={}

def CalcTable(noOfCust,IAT,ST):
    for i in range(noOfCust):
        globaldict['cust'].append(i)
        globaldict['IAT'].append(IAT[i])
        globaldict['ST'].append(ST[i])
        if i==0:
            globaldict['AT'].append(0)
            if globaldict['AT'][0]==0:
                globaldict['TSB'].append(0)

        else:
            globaldict['AT'].append(globaldict['IAT'][i]+globaldict['AT'][i-1])
            if globaldict['AT'][i]>=globaldict['TSE'][i-1]:
                globaldict['TSB'].append(globaldict['AT'][i])
            else:
                globaldict['TSB'].append(globaldict['TSE'][i-1])


        globaldict['TCWQ'].append(globaldict['TSB'][i]-globaldict['AT'][i])
        globaldict['TSE'].append(globaldict['TSB'][i]+globaldict['ST'][i])
        globaldict['TCSS'].append(globaldict['TSE'][i]-globaldict['AT'][i])
        if i==0:
            globaldict['ITS'].append(0)
        else:
            if globaldict['AT'][i]>globaldict['TSE'][i-1]:
                globaldict['ITS'].append(globaldict['AT'][i]-globaldict['TSE'][i-1])
            else:
                globaldict['ITS'].append(0)
    print globaldict
    return 0





print("Enter no of customer")
noofCust=input()

IAT=[]
ST=[]
print "Enter IAT of",noofCust,"customer:"
for i in range(0,noofCust):
    IAT.append(input())

print "Enter ST of",noofCust,"customer:"
for i in range(0,noofCust):
    ST.append(input())

globaldict['cust']=[]
globaldict['IAT']=[]
globaldict['AT']=[]
globaldict['ST']=[]
globaldict['TSB']=[]
globaldict['TCWQ']=[]
globaldict['TSE']=[]
globaldict['TCSS']=[]
globaldict['ITS']=[]

CalcTable(noofCust,IAT,ST)
