cars = 100
space_in_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_car
average_passengers = passengers / cars_driven
# everything above this is "variables", names given for numbers
# everything below this is a mix of words and using the variables.  Remember to use commas before and after the variable.
print "there are", cars, "cars"
print "there are only", drivers, "drivers"
print "there will be", cars_not_driven, "empty cars"
print "we can transpot", carpool_capacity, "people"
print "we have", passengers, "to carpool"
print "we need to put", average_passengers, "in each car" 
