from sys import argv
from os.path import exists
script, from_file, to_file = argv

# print "Coping from %s to %s." % (from_file, to_file)

# input = open(from_file)
# indata = input.read()

# print "The input file is %d bytes long." % len(indata)

# print "Dose the output file exists? %r" %exists(to_file)
# print "Press RETURN to continue, type CTRL-C to abort."
# raw_input()

# output = open(to_file, 'w')
# output.write(indata)

# print "All DONE"
# output.close()
# input.close()

open(to_file, 'w').write(open(from_file).read())