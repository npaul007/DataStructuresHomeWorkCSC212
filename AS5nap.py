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
    def __init__(self,time,minSize,maxSize):
        self.timestamp = time
        self.pages = random.randrange(minSize,maxSize)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):
        return currenttime - self.timestamp

def simulation(numberOfIterations, numSeconds, pagesPerMinute, minSize, maxSize,fout):
    overall = 0
    printContent = []

    for i in range(numberOfIterations):
        labprinter = Printer(pagesPerMinute)    
        printQueue = Queue()
        waitingtimes = []

        for currentSecond in range(numSeconds):
            if newPrintTask():
                task = Task(currentSecond,minSize,maxSize)
                printQueue.enqueue(task)

            if not labprinter.busy() and not printQueue.is_empty():
                nexttask = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter.startNext(nexttask)

            labprinter.tick()

        averageWait = sum(waitingtimes)/len(waitingtimes)
        overall = overall + averageWait
        fout.write("Average Wait %6.2f secs %3d tasks remaining.\n" % (averageWait,printQueue.size()))

    averageOverall = overall/numberOfIterations
    fout.write('Overall average wait time: %.2f secs\n' % averageOverall)

def simulationTwoPrinters(numberOfIterations, numSeconds, pagesPerMinute,pagesPerMinute2, minSize, maxSize,fout):
    overall = 0
    printContent =[]
 
    for i in range(numberOfIterations):
        labprinter = Printer(pagesPerMinute)
        labprinter2 = Printer(pagesPerMinute2) 
        
        printQueue = Queue()
        waitingtimes = []

        for currentSecond in range(numSeconds):
            if newPrintTask():
                task = Task(currentSecond,minSize,maxSize)
                printQueue.enqueue(task)

            if not labprinter.busy() and not printQueue.is_empty():
                nexttask = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter.startNext(nexttask)

            if not labprinter2.busy() and not printQueue.is_empty():
                nexttask = printQueue.dequeue()
                waitingtimes.append(nexttask.waitTime(currentSecond))
                labprinter2.startNext(nexttask)

            if not labprinter.busy() and not labprinter2.busy() and not printQueue.is_empty():
                if pagesPerMinute > pagesPerMinute2:       
                    nexttask = printQueue.dequeue()
                    waitingtimes.append(nexttask.waitTime(currentSecond))
                    labprinter.startNext(nexttask)
                elif pagesPerMinute2 > pagesPerMinute:
                    nexttask = printQueue.dequeue()
                    waitingtimes.append(nexttask.waitTime(currentSecond))
                    labprinter2.startNext(nexttask) 

            labprinter.tick()
            labprinter2.tick()

        averageWait = sum(waitingtimes)/len(waitingtimes)
        overall = overall + averageWait
        fout.write("Average Wait %6.2f secs %3d tasks remaining.\n" % (averageWait,printQueue.size()))

    averageOverall = overall/numberOfIterations
    fout.write('Overall average wait time: %.2f secs\n' % averageOverall)

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
            #push configurations to list
            allConfigs.append(config)
            
            #reset configuration key setter
            counter = 0
            config = dict()
        else:
            # add data to config dictionary
            config[keys[counter]] = content.replace('\n','')
            counter = counter + 1

    return allConfigs

def runProject(config,fout):
    configs = getConfigurations()
    numOfPrinters = int(config['numOfPrinters'])
    
    try:
        if numOfPrinters <= 2:
            if numOfPrinters == 1:
                simulation(int(config['simExperiments']),
                           int(config['simTime']),
                           int(config['ppmPrintOne']),
                           int(config['minTask']),
                           int(config['maxTask']),fout)
                fout.write('\n')
            if numOfPrinters == 2:
                simulationTwoPrinters(int(config['simExperiments']),
                                      int(config['simTime']),
                                      int(config['ppmPrintOne']),
                                      int(config['ppmPrintTwo']),
                                      int(config['minTask']),
                                      int(config['maxTask']),fout)
                fout.write('\n')
               
        else:
            fout.write('Invalid number of printers. Exiting\n')
        
        
    except ValueError:
        fout.write('Format error minimum task size. Exiting\n')

def main():
    configs = getConfigurations()
    fout= open("sim_out.txt",'w')
    
    print('Processing simulations. Please wait.')
    for config in configs:
        runProject(config,fout)
    fout.close()
    print('Process Complete. Data written to sim_out.txt file')
        
# main method   
if __name__ == "__main__":
    main()
