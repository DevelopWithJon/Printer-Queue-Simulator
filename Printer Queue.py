import queue
import random
import time

class Printer():
    
    def __init__(self):
        self.printerStatus = "Available"
        self.q = queue.Queue(maxsize=20)
        self.currentTask = None
        self.totalTime = 0
        self.completedTasks = 0
        
    
    def addTaskToPrinter(self):
        if self.printerStatus == "Available" and self.q.qsize()>=1:
            self.currentTask = self.q.get()
            self.printerStatus = "Busy"
        elif self.q.full():
            self.totalTime+=1
        else:
            self.createTask(self.totalTime)
    
    def createTask(self, currentTime):
        currentSecond = random.randint(1,180)
        if currentSecond == 180:
            self.totalTime+=1
            self.q.put(self.task(currentTime))
        else:
            self.totalTime+=1
    
    def printing(self):
        while self.completedTasks<20:
            if self.printerStatus == "Busy":
                if  self.totalTime - self.currentTask["Timestamp"] >= self.currentTask["pages"]*(6*self.currentTask["quality"]):
                    self.currentTask = None
                    self.printerStatus = "Available"
                    self.completedTasks+=1
                else:
                    self.addTaskToPrinter()
            else:
                self.addTaskToPrinter()
                
    def task(self, currentTime):
        pages = random.randint(1,20)
        quality = random.randint(1,2)
        return {"pages": pages, "quality": quality, "Timestamp": currentTime}
time.
p = Printer()
p.printing()
print(p.completedTasks)
print(p.totalTime)


class Printer2:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
        
    def tick(self):
        if self.currentTask!=None:
            self.timeRemaining = self.timeRemaining-1
            if self.timeRemaining<=0:
                self.currentTask = None
                
    def busy(self):
        if self.currentTask!=None:
            return True
        else:
            return False
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate
        
class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
        
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self, currenttime):
        return currenttime - self.timestamp
    
start1 = time.time()
for i in range(100)
    p1 = Printer().printing()
end1 = time.time()