from sys import argv # Import brings in outside information
# and helps compress the code (modules)
script, first, second, third = argv
# Line 3 "unpacks" argv.  It assigns it variables to use
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third