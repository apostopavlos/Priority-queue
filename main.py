from prettytable import PrettyTable
import random

# Class to represent a process
class process:
    def __init__(self,name,priority,arivalTime,serviceTime):
        self.name=name
        self.priority=priority
        self.arivalTime=arivalTime
        self.serviceTime=serviceTime
        self.endTime=0
        self.processTime=0
        self.flagProcess= False
        self.turnaround=0
        self.responeTime=0

    def __str__(self):
        return f"name:{self.name} arival time:{self.arivalTime} service time:{self.serviceTime} priority:{self.priority} process time:{self.processTime} end time: {self.endTime} "
        

# Class to represent a queue of processes
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
flag=1
while(flag==1):
    # Initialize process queues
    Timequeue = processQueue()
    Priotyqueue = processQueue()
    savequeue = processQueue()
    roundRobin = processQueue()
    time_table= PrettyTable()
    time_table.field_names =["task name","clock tick"]
    print("Priority Queue with Round robin ")
    i=int(input("1 for manual enterning 2 for random antering:"))
    # Validate user input for manual or random entry
    while(i!=1 and i!=2):
        i=int(input("1 for manual enterning 2 for random antering:"))
     # Process entry based on user choice
    if(i==1):
        numProcess=int(input("numeber of process:"))
        Q=int(input("Time Quantum:"))
        for i in range(numProcess):
            name=input("name of task:")
            arrivalTime=int(input("arrival time of task:"))
            serviceTime=int(input("brust time of task:"))
            priority=int(input("priority of task(between 1-7):"))
            while(priority<1 or priority>7):
                priority=int(input("priority of task(between 1-7):"))
            Timequeue.enQueue(process(name,priority,arrivalTime,serviceTime))
     # Process entry based on random choice
    else:
        numProcess=random.randint(1,11)
        Q=random.randint(1,6)
        for i in range(numProcess):
            name="T"+str(i)
            arrivalTime=random.randint(1,11)
            serviceTime=random.randint(1,11)
            priority=random.randint(1,8)
            Timequeue.enQueue(process(name,priority,arrivalTime,serviceTime))
    # Sort processes by arrival time and print
    Timequeue.sortByArivalTime()
    print("process befor:")
    Timequeue.printQueue()


    # Find total time required for execution
    time=0
    for i in Timequeue.Queue:
        if(i.arivalTime>time):
            time = i.arivalTime
        time+=i.serviceTime

    
    # Process execution based on priority and round robin
    for i in range(time):
        for j in range(len(Timequeue.Queue)):
        # Pass the processes from Timequeue to Priotyqueue when the arrival time of a process matches the current time (i)    
            if(int(Timequeue.Queue[0].arivalTime) == i): 
                x=Timequeue.deQueue()
                Priotyqueue.enQueue(x)
        Priotyqueue.sortByPrioty() # Sort processes by priority
        if(len(Priotyqueue.Queue)>0 or len(roundRobin.Queue)>0): # Check if there are processes available for execution
            if(len(Priotyqueue.Queue)>0):
                l=0
                # Check if there are processes whith some priority
                while (Priotyqueue.Queue[0].priority==Priotyqueue.Queue[l].priority) and (l+1<len(Priotyqueue.Queue)):
                    l+=1
                if(Priotyqueue.Queue[0].priority==Priotyqueue.Queue[len(Priotyqueue.Queue)-1].priority):
                    l+=1
            if(l>1 or len(roundRobin.Queue)>0):
                #start Round robin
                if(len(roundRobin.Queue)<1):
                    for k in range(l):
                        x=Priotyqueue.deQueue()
                        roundRobin.enQueue(x)
                        q=0
                if(q<Q):
                    q+=1
                    roundRobin.Queue[0].serviceTime-=1
                    time_table.add_row([roundRobin.Queue[0].name,i])
                    if(roundRobin.Queue[0].flagProcess==False):
                        roundRobin.Queue[0].processTime=i
                        roundRobin.Queue[0].flagProcess=True
                else:
                    x=roundRobin.deQueue()
                    roundRobin.enQueue(x)
                    roundRobin.Queue[0].serviceTime-=1
                    time_table.add_row([roundRobin.Queue[0].name,i])
                    if(roundRobin.Queue[0].flagProcess==False):
                        roundRobin.Queue[0].processTime=i
                        roundRobin.Queue[0].flagProcess=True
                    q=1
                if(roundRobin.Queue[0].serviceTime==0):
                    roundRobin.Queue[0].endTime= i
                    x=roundRobin.deQueue()
                    savequeue.enQueue(x)
                    q=0
                    #end Round Robin
                    #start Priority Queue
            else:
                time_table.add_row([Priotyqueue.Queue[0].name,i])
                Priotyqueue.Queue[0].serviceTime -=1
                if(Priotyqueue.Queue[0].flagProcess==False):
                    Priotyqueue.Queue[0].processTime=i
                    Priotyqueue.Queue[0].flagProcess=True

                if(Priotyqueue.Queue[0].serviceTime == 0):
                    Priotyqueue.Queue[0].endTime= i
                    x=Priotyqueue.deQueue()
                    savequeue.enQueue(x)

                    #end Priority Queue
                    
    print("*******************")  
    print(time_table)
    print("process after")
    savequeue.printQueue()
    avgRespone=0
    avgTurnaround=0
    my_table= PrettyTable()   
    my_table.field_names=["Name","Respone Time","Turnaround Time"]
   # Calculate and display response time and turnaround time for each process
    for i in savequeue.Queue:
        i.responeTime=i.processTime-i.arivalTime
        i.turnaround=i.endTime-i.arivalTime
        my_table.add_row([i.name,i.responeTime,i.turnaround])
        avgRespone+=i.responeTime
        avgTurnaround+=i.turnaround
    print(my_table)
    # Calculate and display average response time and turnaround time
    avgRespone=avgRespone/len(savequeue.Queue)
    avgTurnaround=avgTurnaround/len(savequeue.Queue)

    avg_table= PrettyTable()
    avg_table.field_names = ["Total","Avg Respone","Avg Turnaround"]
    avg_table.add_row([1,avgRespone,avgTurnaround])
    print(avg_table)
    # Prompt user to continue or end the program
    print("do you want to continue?")
    flag=int(input("press 1 to continue or 2 to end the program: "))
    while(flag!=1 and flag!=2):
        print("do you want to continue?")
        flag=int(input("press 1 to continue or 2 to end the program: "))