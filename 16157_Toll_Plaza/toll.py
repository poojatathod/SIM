import time
import timeInSec

#class 3 taking single process not list of processes
class server3():
    def __init__(self):
        self.AT3 = []
        self.ST3 = []
        self.IAT3 = []
        self.TSB3 = []
        self.TCWQ3 = []
        self.TSE3 = []
        self.TCSS3 = []
        self.ITS3 = []
        self.pID3 = []

        self.pCount = 0
        self.custWait = 0
        self.serverIdle = 0

    #inter arrival time function
    def InterArrivalTime(self,cnt):
        if(len(self.IAT3)==0):
            self.IAT3.append(self.AT3[0])
        else:
            self.IAT3.append(self.AT3[cnt]-self.AT3[cnt-1])


    #service begin time function
    def ServiceBeginTime(self,cnt):
        if(cnt==0):
            self.TSB3.append(self.AT3[0])
        else:
            self.TSB3.append(max(self.TSE3[cnt-1],self.AT3[cnt]))


    #customer waits in queue time function definition
    def CustomerWaitsInQueueTime(self,cnt):
        self.TCWQ3.append(self.TSB3[cnt]-self.AT3[cnt])


    #service end time function definition
    def ServiceEndTime(self,cnt):
        self.TSE3.append(self.TSB3[cnt]+self.ST3[cnt])


    #time customer spends in system function definition
    def TimeCustomerSpendInSystem(self,cnt):
        self.TCSS3.append(self.TSE3[cnt]-self.AT3[cnt])


    #server idle time calculating function
    def ServerIdleTime(self, cnt):
        if(cnt==0):
            self.ITS3.append(self.AT3[0]-self.codeno)
        else:
            if((self.AT3[cnt]-self.TSE3[cnt-1])>0):
                self.ITS3.append(self.AT3[cnt]-self.TSE3[cnt-1])
            else:
                self.ITS3.append(0)



    def init1(self, custNo, AT1, ST1, fp, no, codeno):
        self.AT1 = AT1
        self.ST1 = ST1
        self.cust = custNo
        self.fp = fp
        self.no = no
        self.codeno = codeno

        self.AT3.append(AT1)
        self.ST3.append(ST1)
 
        self.InterArrivalTime(self.pCount)
        self.ServiceBeginTime(self.pCount)
        self.CustomerWaitsInQueueTime(self.pCount)
        self.ServiceEndTime(self.pCount)
        self.TimeCustomerSpendInSystem(self.pCount)
        self.ServerIdleTime(self.pCount)

        self.pCount += 1
        self.pID3.append(self.cust)
 
    #AT:Arrival Time, ST: Service time, IAT: Inter-Arrival Time
    #TSB: Service Begin Time, TCWQ: Customer waits in queue, TSE: Service End
    #TCSS: Time Customer Spend In System, ITS: Server Idle Time

    def printing(self):
        print("\t\tTHIS IS TOLL NUMBER "+str(self.no)+"\n")
        print("PID\tAT\tST\tTSB\tCWQT\tTSE\tTCSS\tITS\n")

        for i in range(len(self.AT3)):
            print(str(self.pID3[i])+"\t"+str(self.AT3[i])+"\t"+str(self.ST3[i])+"\t"+str(self.TSB3[i])+"\t"+str(self.TCWQ3[i])+"\t"+str(self.TSE3[i])+"\t"+str(self.TCSS3[i])+"\t"+str(self.ITS3[i]))

        print("\n")

        return self.waitTime(), self.servIdle()

    #customer waiting time
    def waitTime(self):
        self.custWait = reduce(lambda x,y: x+y, self.TCWQ3) 
        print "Total time customer waits in queue: ",self.custWait      

        return self.custWait

    #server idle time
    def servIdle(self):
        self.serverIdle = reduce(lambda x,y: x+y, self.ITS3)
        print "Total time Toll idle is: ",self.serverIdle,"\n\n"

        return self.serverIdle




def Toll(fileName):
    fp = open(fileName,'r')
    
    sc = {'MS':20, 'TS':7, 'MPTS':10, 'EZP':4}
    
    AT = []
    ST = []
    CID = []

    for line in fp:
        line = line.split()

        AT.append(timeInSec.timeInSec(line[0]))
        
        if line[2] in sc.keys():
            ST.append(sc[line[2]])

        CID.append(line[1])


    if fileName == 'InputFile1':
        cn = 21600
    else:
        cn = 14400

    obj3 = server3()
    obj4 = server3()
    obj5 = server3()

    obj3.init1(CID[0],AT[0],ST[0],fp,1,cn) 
    obj4.init1(CID[1],AT[1],ST[1],fp,2,cn)
    obj5.init1(CID[2],AT[2],ST[2],fp,3,cn)

    for x in range(len(AT)-2):
        i = x+3

        if i == len(AT):
            break        

        if obj3.TSE3[obj3.pCount-1] < obj4.TSE3[obj4.pCount-1]:
            if obj3.TSE3[obj3.pCount-1] < obj5.TSE3[obj5.pCount-1]:
                obj3.init1(CID[i],AT[i],ST[i],fp,1,cn)
            else:
                obj5.init1(CID[i],AT[i],ST[i],fp,3,cn)
        
        elif obj4.TSE3[obj4.pCount-1] < obj5.TSE3[obj5.pCount-1]:
            obj4.init1(CID[i],AT[i],ST[i],fp,2,cn)

        else:
            obj5.init1(CID[i],AT[i],ST[i],fp,3,cn)



    a,d = obj3.printing()
    b,e = obj4.printing()
    c,f = obj5.printing()

    fp.close()


    print "average server idle time is per server is : ",(d+e+f)
    print "average waiting time per process is : ",(a+b+c)/500


#main function
if __name__ == "__main__":

    print"DELAY VS PEAK TRAFFIC TIME FROM 6.30 to 10.30 AM"
    Toll('InputFile1')
    print"\n\n###########################################################\n\n\nDELAY VS PEAK TRAFFIC TIME FROM 4.00 to 8.00 PM"
    Toll('InputFile2')