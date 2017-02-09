def print_pattern():
	for i in range(1,5):
		for j in range(0,i):
			print "* ",
		for j in range(i,5):
			print "a ",
		for j in range(0,i):
			print "* ",
		print "\n"

print_pattern()