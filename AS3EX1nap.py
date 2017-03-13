#Hamburger class
class Hamburger:
    def __init__(self,weight,doneness,cheese,toppings):
          self.weight = weight
          self.doneness = doneness
          self.cheese = cheese
          self.toppings = toppings

    def setWeight(self,newWeight):
    	self.weight = newWeight

    def getWeight(self):
    	return self.weight

    def setCheese(self,newCheese):
    	self.cheese = newCheese

    def getCheese(self):
    	return self.cheese

    def setDoneness(self,newDoneness):
    	self.doneness = newDoneness

    def getDoneness(self):
    	return self.doneness

    def setToppings(self,newToppings):
    	self.toppings = newToppings

    def getToppings(self):
    	return self.toppings

    def bite(self):
    	if self.weight > 0:
    		self.weight = self.weight - 1

    def __str__(self):
    	return("This burger is cooked %s"
    		"\nIt weighs %s ounces"
    		"\nIt has the toppings: %s" 
    		"\nIt is %s that there is cheese"
    		% (self.getDoneness(),self.getWeight(),self.getToppings(),self.getCheese()))
	
#main method
def main():
	myBurger = Hamburger(16,"medium",True,['Mushrooms','Tomatoes'])

	# __str__ method
	print(myBurger)

	#burger now cooked well done
	myBurger.setDoneness("well done")

	#set burger weight to 10 ounces
	myBurger.setWeight(10)

	# reduce weight by 1 ounce from 10 ounces to 9 ounces
	myBurger.bite()

	#change toppings to Lettuce and Mayonnaise
	myBurger.setToppings(['Lettuce','Mayonnaise'])

	#no cheese on Burger
	myBurger.setCheese(False)

	# __str__ method
	print("\n%s" % myBurger)

if __name__ == "__main__":
    main()