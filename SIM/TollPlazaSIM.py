from matplotlib import pyplot
from multiprocessing import Process,Manager
import time,copy

delayPeekTraffic1=dict() #for morning traffic
delayPeekTraffic2=dict() #for evening traffic
termsignal=False    #Used for terminating scheduler [terminate signal]
queue= list()  #shared queue by all toolbooths for vehicles
InputData = dict()

carLog = dict()

#tollBooths
tollBooth1 = list()
tollBooth2 = list()
tollBooth3 = list()


#service times
serviceCosts={"MS":20,"TS":7,"MPTS":10,"EZP":4}

#Assumptions
#[1] For morning session traffic rate is assumed as 20 cars/min
#[2] For evening session traffic rate is assumed as 35 cars/min
#[3] We have 3 tollbooths

#session=1 Indicates morning session
#session=2 Indicates evening session
#def calculateDelay(session):

def readInput(inputFile):
    for line in inputFile:
        key,carid,serviceType=line.split()
        serviceType=serviceType.split("\n")[0]
        if key not in InputData:
            InputData[key]=[]
        InputData[key].append([carid,serviceType])

def getFreeTime(ctime,delay):
    h=ctime[0]
    m=ctime[1]
    s=ctime[2]

    i=1
    while i<=delay:
        s+=1
        if s==60:
            if m==59:
                m=0
                s=0
                h+=1
                if h==24:
                    h=0
                    m=0
                    s=0
            else:
                m+=1
        i+=1
    return str(h)+":"+str(m)+":"+str(s)

def scheduler():
    hours=6
    minutes=0
    sec=0
    tollBooth1FreeTime=tollBooth2FreeTime=tollBooth3FreeTime=""
    while termsignal==False:
        currentTime=str(hours)+":"+str(minutes)+":"+str(sec)
        if currentTime in InputData:
            for rec in InputData[currentTime]:
                newRec=[currentTime]+rec
                queue.append(newRec)
        print currentTime,"\t",queue[0][0]
        if len(tollBooth1)==0 and len(queue)!=0:
            carLog[queue[0][1]]=[queue[0][0],queue[0][2]]
            tollBooth1.append(queue[0])
            tollBooth1FreeTime=getFreeTime([hours,minutes,sec],serviceCosts[tollBooth1[0][2]])
            queue.pop(0)

        if len(tollBooth2)==0 and len(queue)!=0:
            carLog[queue[0][1]]=[queue[0][0],queue[0][2]]
            print "in2"
            tollBooth2.append(queue[0])
            tollBooth2FreeTime=getFreeTime([hours,minutes,sec],serviceCosts[tollBooth1[0][2]])
            queue.pop(0)

        if len(tollBooth3)==0 and len(queue)!=0:
            carLog[queue[0][1]]=[queue[0][0],queue[0][2]]
            print "in3"
            tollBooth3.append(queue[0])
            tollBooth3FreeTime=getFreeTime([hours,minutes,sec],serviceCosts[tollBooth1[0][2]])
            queue.pop(0)

        if currentTime==tollBooth1FreeTime:
            carLog[tollBooth1[0][1]].append(copy.deepcopy(currentTime))
            tollBooth1.pop(0)
        if currentTime==tollBooth2FreeTime:
            carLog[tollBooth2[0][1]].append(copy.deepcopy(currentTime))
            tollBooth2.pop(0)
        if currentTime==tollBooth3FreeTime:
            carLog[tollBooth3[0][1]].append(copy.deepcopy(currentTime))
            tollBooth3.pop(0)


        sec+=1
        if sec==60:
            if minutes==59:
                minutes=0
                sec=0
                hours+=1
                if hours==24:
                    hours=0
                    minutes=0
                    sec=0
            else:
                minutes+=1
                sec=0

def originalTimer(startHours):
    hours=startHours
    minutes=0
    sec=0
    flag=0
    while termsignal==False:
        now = time.localtime(time.time())
        sec=now[5]
        if sec==59:
            if flag==1:
                minutes=0
                hours+=1
                flag=0
            else:
                minutes+=1
        if minutes==59:
            flag=1
        systemTime[0]=str(hours)+":"+str(minutes)




def init():
    readInput(open("InputFile","r"))
    scheduler()
    for key in carLog.keys():
                        print key,carLog[key]


    #schedulerP=Process(target=scheduler,args=())
    #schedulerP.start()
    #if raw_input()=="STOP":
    #    termsignal.append(True)
    #schedulerP.join()

init()
