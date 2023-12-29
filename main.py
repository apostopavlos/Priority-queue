
class process:
    def __init__(self,name,priority,arivalTime,serviceTime):
        self.name=name
        self.priority=priority
        self.arivalTime=arivalTime
        self.serviceTime=serviceTime
        self.endTime=0
        self.processTime=0
        self.flagProcess= False

    def __str__(self):
        return f"name:{self.name} arival time:{self.arivalTime} service time:{self.serviceTime} priority:{self.priority} process time:{self.processTime} end time: {self.endTime} "
        

class processQueue:
    def __init__(self) :
        self.Queue = []

    def enQueue(self,a:process):
        self.Queue.append(a)

    def deQueue(self)->process or None:
        return self.Queue.pop(0)
    
    def sortByArivalTime(self):
        self.Queue.sort(key=lambda x: x.arivalTime)

    def sortByPrioty(self):
        self.Queue.sort(key=lambda x: x.priority)

    def printQueue(self):
        for i in self.Queue:
            print(i)
        


#main 

x1=process("t1",2,0,3)
x2=process("t2",1,2,2)
x3=process("t3",7,5,2)
x4=process("t4",5,3,3)
x5=process("t5",5,2,2)
Timequeue = processQueue()
Priotyqueue = processQueue()
savequeue = processQueue()


Timequeue.enQueue(x1)
Timequeue.enQueue(x2)
Timequeue.enQueue(x3)
Timequeue.enQueue(x4)
Timequeue.enQueue(x5)
Timequeue.sortByArivalTime()
Timequeue.printQueue()


#find time
time=0
for i in Timequeue.Queue:
    if(i.arivalTime>time):
        time = i.arivalTime
    time+=i.serviceTime

print(time)

for i in range(time):
    for j in range(len(Timequeue.Queue)):
        
        if(int(Timequeue.Queue[0].arivalTime) == i):
            x=Timequeue.deQueue()
            Priotyqueue.enQueue(x)
    Priotyqueue.sortByPrioty()
    if(len(Priotyqueue.Queue)>0):
        print(Priotyqueue.Queue[0].name, i)
        Priotyqueue.Queue[0].serviceTime -=1
        if(Priotyqueue.Queue[0].flagProcess==False):
            Priotyqueue.Queue[0].processTime=i
            Priotyqueue.Queue[0].flagProcess=True

        if(Priotyqueue.Queue[0].serviceTime == 0):
            Priotyqueue.Queue[0].endTime= i
            x=Priotyqueue.deQueue()
            savequeue.enQueue(x)


print("*******************")  
savequeue.printQueue()
            
