# this one is like argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# new way to do it
def print_two_again(arg1, arg2): 
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# this just takes one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#this one takes no arguments
def print_none():
	print "I got nothin."


print_two ("Seen", "Shawn")
print_two_again ("Seen", "Shawn")
print_one ("First!")
print_none ()