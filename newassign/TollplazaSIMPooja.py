from matplotlib import pyplot
from multiprocessing import Process,Manager
import time

delayPeekTraffic1={} #for morning traffic
delayPeekTraffic2={} #for evening traffic
manager=Manager()
termsignal=manager.list()    #Used for terminating scheduler [terminate signal]
queue= manager.list()  #shared queue by all toolbooths for vehicles
InputData = manager.dict()

#Assumptions 
#[1] For morning session traffic rate is assumed as 20 cars/min
#[2] For evening session traffic rate is assumed as 35 cars/min
#[3] We have 3 tollbooths

#session=1 Indicates morning session
#session=2 Indicates evening session
#def calculateDelay(session):

def queueManager():



def scheduler():
    while len(termsignal)==0:
        print queue



def init():

    schedulerP=Process(target=scheduler,args=())
    queueManagerP=Process(target=queueManager,args=())
    queueManagerP.start()
    schedulerP.start()
    if raw_input()=="STOP":
        termsignal.append(True)
    schedulerP.join()

init()
