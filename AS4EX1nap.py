import time
import random

'''
def binarySearch (alist, item):
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last ) /2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

        return found  '''

def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found 

def bubbleSort(alist):
    startTime = time.time()

    for passnum in range(len(alist)-1,0,-1): 
        for i in range(passnum):
            if alist[i]>alist[i+1]: 
                temp = alist[i] 
                alist[i] = alist[i+1] 
                alist[i+1] = temp

    endTime = time.time()
    timeTaken = endTime-startTime

    print('It took %.5f seconds to bubble sort a list of size %s' % (timeTaken,len(alist)))

#main method
def main():
    # time taken of bubble sort sorting list of size n = 1000
    array = random.sample(range(0,1000),1000)
    bubbleSort(array)

     
if __name__ == "__main__":
    main()