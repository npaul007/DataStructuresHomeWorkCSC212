import random

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask != None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self,newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60/self.pagerate

class Task:
    def __init__(self,time):
        self.timestamp = time
        self.pages = random.randrange(1,21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numSeconds, pagesPerMinute):
    #printers
    labprinter = Printer(pagesPerMinute)
    labprinter2 = Printer(pagesPerMinute)
    
    printQueue = Queue()
    printQueue2 = Queue()
    
    waitingtimes = []

    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)
            printQueue.enqueue(task)

        if not labprinter.busy() and not printQueue.is_empty():
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)

        labprinter.tick()

    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Average Wait %6.2f secs %3d tasks remaining." % (averageWait,printQueue.size()))

def newPrintTask():
    num = random.randrange(1,181)
    if num == 180:
        return True
    else:
        return False

#returns configurations from sim_config.txt file
def getConfigurations():
    allConfigs = []
    config = dict()
    
    keys = ['simTime','simExperiments','minTask','maxTask','numOfPrinters','ppmPrintOne','ppmPrintTwo']

    # loading file data
    file = open('sim_config.txt','r')
    fileContents = file.readlines()
    
    counter = 0
    for content in fileContents:
        #new configuration set detected in text file
        if content == '\n':
            #reset configuration key setter
            counter = 0
            #push configurations to list
            allConfigs.append(config)
        else:
            # add data to config dictionary
            config[keys[counter]] = content.replace('\n','')
            counter = counter + 1

    return allConfigs

def main():
    '''
    # run simulation 10 times
    for i in range(10):
        simulation(3600, 10) '''
    
    print(getConfigurations())

# main method   
if __name__ == "__main__":
    main()
