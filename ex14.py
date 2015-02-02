from sys import argv

script, user_name = argv
prompt = '> '

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Are you hungry %s?" % user_name
hungry = raw_input (prompt)

print "Where do you live %s?" % user_name
lives = raw_input (prompt)

print "What kind of computer do you have?"
computer = raw_input (prompt)

print """
Alright, so you said %r about being hungry.
You live in %r.  No idea where that is.
And you have a %r computer. Acceptable.
""" % (hungry, lives, computer)