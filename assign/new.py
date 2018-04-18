from prettytable import PrettyTable

x=PrettyTable()

Dict={}
DictOfToll={}
DictOfToll["T1"]=0
DictOfToll["T2"]=0
DictOfToll["T3"]=0

Card=5.0
Cash=3.0

print "enter no of customers: "
n=input()
#Arrival time , type of payment ,toll type,wt,et

def TollPlaza(n):
    
    for i in range(n):
        Dict[i]=[]
    print "Arrival time of vehicles"
    for i in range(n):
        Dict[i].append(input())

    print "Type of payment i.e Card,Cash"
    for i in range(n):
        Dict[i].append(input())

    for i in range(n):
        if DictOfToll["T1"]==0:
            Dict[i].append("T1")
            Dict[i].append(0)
            var = Dict[i][0]+Dict[i][1]+Dict[i][3]
            Dict[i].append(var)
            
            if var>=Dict[i+1][0]:
                DictOfToll["T1"]=1
            else:
                DictOfToll["T1"]=0


        elif DictOfToll["T2"]==0:
            Dict[i].append("T2")
            Dict[i].append(0)
            var=Dict[i][0]+Dict[i][3]+Dict[i][1]

            Dict[i].append(var)
            
            if var>=Dict[i+1][0]:
                DictOfToll["T2"]=1
            else:
                DictOfToll["T2"]=0


        elif DictOfToll["T3"]==0:
            Dict[i].append("T3")
            Dict[i].append(0)
            var=Dict[i][0]+Dict[i][3]+Dict[i][1]
            Dict[i].append(var)
            
            if var>=Dict[i+1][0]:
                DictOfToll["T3"]=1
            else:
                DictOfToll["T3"]=0
    

TollPlaza(n)

print Dict
#for i in range(n):
 #   x.add_row(Dict[i])
#print x


