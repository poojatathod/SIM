import math
import random

dict1={}

def  table1(start,end,timeInterval):
    CurrTime=start
    i=0
    c=30
    while(CurrTime!=end):
        CurrTime=CalculateTime(CurrTime,timeInterval,i)
        CalculateArrivalRate(i,c)
        i+=1
        c+=5

def CalculateTime(CurrTime,timeInterval,i):
    l1=[]
    time=""
    time=str(CurrTime+timeInterval)
    l1=time.split(".")

    l1[0]=int(l1[0])
    l1[1]=int(l1[1])

    if(l1[1]>=6):
        l1[0]+=1
        l1[1]-=6
    dict1[i]=[]
    dict1[i].append(str(CurrTime)+"-"+str(l1[0])+"."+str(l1[1]))
    CurrTime=str(l1[0])+"."+str(l1[1])
    CurrTime=float(CurrTime)
    return CurrTime


def CalculateArrivalRate(i,x):
    e=2.71
    lamb=CalLamb()
    X=(lamb**x * e**(-lamb))/math.factorial(x)
    dict1[i].append(round(X,2))
    
def CalLamb():
    return random.randint(0,10)
    


table1(6.30,10.30,0.30)
print dict1
