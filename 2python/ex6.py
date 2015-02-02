x = "there are %d people" % 10
binary = 'binary'
do_not = 'don\'t'
y = 'those who know %s and those who %s' % (binary, do_not)

print x
print y

print '%r' % x
print '%s' % y

funny = False
joke = 'funny? %r'

print joke % funny

w = 'this is the left'
e = 'this is the right'

print w + e
