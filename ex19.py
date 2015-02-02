# Creates a function to be called later.  The print gets called as well.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
# Calls the function after the first sentence, giving numbers for cheese_count and boxes_of_crackers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Sets the values for the function
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50
#Calls the function
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Sets values (using math!) and calls the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#Uses the last values and adds more to them.  Then it calls the function.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

