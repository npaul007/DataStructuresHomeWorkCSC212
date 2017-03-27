# Implementation of an Unordered List ADT as a linked list.  The list
# is accessed through a reference to the first element, head.  
# Adopted from Section 3.9 of the textbook.

from Node import Node

class UnorderedList:
    '''
    List is empty upon creation and the head reference is None
    '''
    def __init__(self):
        self.head = None    
        
    '''
    Returns True if list is empty, False otherwise
    '''
    def is_empty(self):
        return self.head == None 
    
    '''
    Add an element to head of the list
    '''
    def add(self, item):
        # Create a node using item as its data
        temp = Node(item)
        # make the next reference of the new node refer to the head 
        # of the list
        temp.set_next(self.head)
        # modify the list head so that it references the new node
        self.head = temp
        
    '''
    Returns the size of the list
    '''
    def size(self):
        # start at the head of the list
        current = self.head
        count = 0
        # Traverse the list one element at a time.  We know
        # we reached the end when the next reference is None
        while current != None:
            count = count + 1
            current = current.get_next()
        return count

    '''
    Search for an item in the list.  Returns True if found, False otherise.  
    '''
    def search(self,item):
        current = self.head
        found = False
        # As long as the element is not found and we haven't 
        # reached the end of the list
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else:
                # go to the next element
                current = current.get_next()
        return found
    
    '''
    Remove the first occurrence of item from the list.  
    '''
    def remove(self, item):
        # keep track of current and previous elements
        current = self.head
        previous = None
        found = False
        # traverse the list 
        while current != None and not found:
            # if we have a match, stop
            if current.get_data() == item:
                found = True
            # otherwise advance current and next references
            else:
                previous = current
                current = current.get_next()
           
        # the element to be deleted is the head of the list     
        if found:
            if previous == None:
                self.head = current.get_next()
                # the element to be deleted is not the head
            else:
                previous.set_next(current.get_next())

    #print all list elements in a list format
    def print_list(self):
        current = self.head
        count = 0
        array = []

        while current != None and count < self.size():
            #add data to list
            array.append(current.get_data())

            #move to next list instance and repeat 
            current = current.get_next()
            count = count + 1

        #display unorderedlist
        print(array)
            
    # replace method parameters are position to change along with new value
    def replace_element(self,position,newValue):
        current = self.head
        count = 0

        while current != None and count < self.size():
            if count == position:
                current.data = newValue

            #move to next list instance and repeat 
            current = current.get_next()

            count = count + 1
          
          
def main():
    # create a list and add some elements to it
    aList = UnorderedList()
    
    print("Adding 3, 5, 8, and 11 to the list.")
    aList.add(3)
    aList.add(5)
    aList.add(8)
    # 11 is the head of the list
    aList.add(11)
    
    # print list method
    aList.print_list()

    # replace method
    aList.replace_element(2,100)

    # check that replace method works
    aList.print_list()
    
  
if __name__ == "__main__":
    main()


