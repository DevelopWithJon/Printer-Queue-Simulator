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



if __name__ == "__main__":
    P = Printer()
    P.printing()
    print(P.completedTasks)
    print(P.totalTime)
