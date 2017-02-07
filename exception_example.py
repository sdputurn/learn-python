#this line is added to test git pull behabiour, when there file present as modefied and when the files are staged
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
except: 
	print "program has exception"
# finally:
# 	print "this is printed by finally blcok so there may be exceptions, if there is any exception exception will be handled after this block. to catch this exception place this block in another try block"
# except: 
# 	print "program has exception"
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

try:
	print a
except Exception, e:
	print "program has exception - ",e

#raising an exception

try:
	level=1
	if level < 2:
		raise Exception("level too low") #raise "Invalid Level","level too low" rasing exception with strings is not working, getting error  - TypeError: exceptions must be old-style classes or derived from BaseException, not str
except Exception,e:
	print "given level too low", e

def _decide(var):
	if var == "PASS":
		return 'PASS'
	else:
		raise MyRaiseExceptions(var)



class MyRaiseExceptions(Exception):
	pass

try:
	level=1
	if level < 2:
		raise MyRaiseExceptions("level too low")
except MyRaiseExceptions,e:
	print "given level too low  - ", e

print _decide('PASS')
try:
	print _decide('FAIL')
except Exception, e:
	print "there is error in program", e

class Employee:
	"this is test class for employee details"
	def __init__(self, name, empid):
		self.name=name
		self.empid=empid
	def display_employee(self):
		print "employee name - ",self.name
		print "empolyee id - ", self.empid

emp1=Employee("sandeep","sinsa45")
emp1.display_employee()
print "employee object", emp1

#User defined exceptions - Python also allows you to create your own exceptions by deriving classes from the standard built-in exceptions.
class MyException(NameError):
	"this class handles user defined exceptions"
	def __init__(self,args):
		self.args = args

try:
	level =1
	if level < 2:
		raise MyException(("level too low"))
except MyException,e:
	print "looks like some variable undefined - ",e






