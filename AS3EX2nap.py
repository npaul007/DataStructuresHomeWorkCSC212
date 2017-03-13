#SocialEvent class
class SocialEvent:
    def __init__(self,title,date,numAttend):
          self.title = title
          self.date = date
          self.numAttend = numAttend

    def setTitle(self,newTitle):
    	self.title = newTitle

    def getTitle(self):
    	return self.title

    def setDate(self,newDate):
    	self.date = newDate

    def getDate(self):
    	return self.date

    def setNumAttend(self,newNumAttend):
    	self.numAttend = newNumAttend

    def getNumAttend(self):
    	return self.numAttend

    def display(self):
    	print("\nThe title of this event is: %s "
        "\nThe event will take place on the date: %s "
        "\nThere will be %s in attendance" 
        % (self.getTitle() , self.getDate(), self.getNumAttend()))
	
#main method
def main():
    print("Please enter 5 events")

    #list to store eventsb
    events = []
    for i in range(0,5):
        print("\nEvent %s" % (i+1))

        eventName = input("Please enter the name of event %s:" % (i+1))
        eventDate = input("Please enter the date of event %s:" % (i+1))
        eventAttendance = input("Please enter the amount attending event %s:" % (i+1))

        newEvent = SocialEvent(eventName,eventDate,eventAttendance)

        # store events in events list
        events.append(newEvent)

    # sort events by number of attendees (least to greatest)
    for i in range(0,len(events)):
        for k in range(0,len(events)):
            if events[i].getNumAttend() < events[k].getNumAttend():
                t = events[i];
                events[i] = events[k];
                events[k] = t;

    print("\nList of Events\n***********************")
    # print events 
    for e in events:
        e.display()

if __name__ == "__main__":
    main()