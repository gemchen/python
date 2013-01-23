#this one is like your scripts argv
def print_two(*argv):
	arg1, arg2 = argv
	print "arg1: %r, arg2: %r" % (arg1,arg2)

# OK, that *args is actually pointless, we can just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1,arg2)

# this take only one argument
def print_one(arg1):
	print "arg1: %r" %arg1

# this one takes no argument
def print_non():
	print "I have nothing."

print_two("gem","chen")
print_two_again("gem","chen")
print_one("First!")
print_non()