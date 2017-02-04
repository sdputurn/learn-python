try:
	fo = open("test_file.txt","r")
	#print fo.read()
except IOError:
	print "file can not be opened"
else:
	print "file opened successfully"
	print fo.read()
	fo.close()

try:
	# a=1/0
	# print a
	print "hello",a

finally:
	print "this is printed by finally blcok so there may be exceptions, if there is any exception exception will be handled after this block. to catch this exception place this block in another try block"
except: 
	print "program has exception"
# else:
# 	print "no exception in this block"

try:
	try:
		a=1/0
		print a
	finally:
		print "print from finally block. there could be exceptions"
except (Exception,IOError), e:
	print "program has exception", e
else:
	print "program has no exceptions"