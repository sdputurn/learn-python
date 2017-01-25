print ("hello world!")
print ('hello world!')
if False:
	print True
else:
	print "false"
#multiline
item1=10; item2=10
total = item1 + \
item2
#or 
total = {item1 +
item2}
total = [item1 +
item2]
total = (item1 +
				item2)
print total
total = """item1 +
      				item2"""
print total

#input
#input ("\n\n press any key to exit")

#no difference in single and double quote
var1 = 'hello world'
var2 = "hello world"
print ('%s var2 %s ' % (var1, var2))
print ("%s var2 - %s"% (var1, var2)) #both stames are same
#delete variable
del var1, var2
#print ("%s var2 - %s"% (var1, var2)) #this gives error variable undefined

#Strings
str = "hello world"
print (str)
print (str[0])
print (str[1:2])
print (str[1:])
print (str * 2)
print(str + "added string"+ "\n")


#list
list = [123,"hello", -123,12.12,'!@#$%^&*()']
print (list)
print (list[1:2])
list[1]= "hello!"
print (list[1:])

#tuples
tuples = (111, "hello", -111, 11.11, '!@#$%^&*()')
print (tuples)

#dictionary
dict = {}
dict["one"] = "hello world!"
dict[2] = 111
dict[3] = 11.11
print (dict)
print (dict["one"], dict[2],dict[3])
print (dict.keys())
print (dict.values() , "\n")

#data type conversion
num = 111
print (float(num) , "\n" ) #seems like print convets do a ttpe conversions on the item it prints. seems like this is converted into a tuple
print ("%d and a new line %s"%(float(num) , "\n")) # where this line is treated a string
#print ("sting" + 10) #this is not allowed as we concatinating 2 different data types
#print ("string", 10, list, tupple ) # this is valid, where i guess the output is a tupple of all values
#print (str(num))
#print (eval(num))

#operators
num1=9
num2=2
print ("num1+num2, num1-num2, num1*num2, num1/num2, num1%num2, num1//num2, num1>num2, num1==num2 - ", num1+num2, num1-num2, num1*num2, float(float(num1)/num2), num1%num2, num1//num2, num1>num2, num1==num2)

#logical operators
var1 = "hello world!"
var2 = "hello"
print ("\nvar2 in var1, var2 not in var1, var2 is var1, var2 is not var1 - ", var2 in var1, var2 not in var1, var2 is var1, var2 is not var1)

#decision making
num1 = 2
num2 = 5
num3 = 9
#find max
if (num1 > num2):
	if num1 > num3 :
		print "num1 is greater numner - %d" % num1
	else :
		print ("num3 is grater numner - %d" %num3)
elif (num2 > num3) :
	print ("num2 is the greater numner - %d " % (num2))
else :
	print ("num3 is grater numner - %d" % (num3))
#loops
#print patter like below
#*
#* *
#* * *  #till 5 lines
import sys

for i in range (1,6):
	for j in range (0,i):
		#print ("* ")
		sys.stdout.write("* ")
	print ("\n")
#same thing with while
i=0
while (i<5): 
	j=0
	while (j <= i):
		# sys.stdout.write("* ")
		print "* ",
		j=j+1
		#or j += 1
	i += 1
	print ("\n")

#date and time
import time
ticks = time.time()
print ("numner of ticks since 12:00 am 1-jan-1970", ticks)

#localltime
localtime = time.localtime(time.time())
print ("localtime", localtime)

print ("asctime", time.asctime())

#calendar
import calendar
print("here is the cal %s" %("\n"))
print (calendar.month(2017,1))

def printme(str):
	"this function print the given string parameter"
	print (str)
	return;

printme("fun_call1")
printme("fun_call2")

def changeme(mylist):
	"changes the passed parameter in function"
	mylist=[1,2,3]
	print ("mylist - ", mylist)
	return;
mylist=[10,20,30]
changeme(mylist)
printme(mylist)

import support
#from support import printme, changeme # not sure why this is not working
support.printme("fun_call")
support.changeme([1,2,3])

from schoolMathExamples import fibonacci
fibonacci(100)

#global variable
def addMoney (txn):
	"this function add txn amount to money"
	global money
	money = money + txn
	print ("%s" %("\n"), "\n","%d" %(money)) # not sure what is the issue with print
	print "\n", money
	print ("%s" %("\n"),1000)
	print ("%s" %("\n"))
	print (1000)
	#print "this is test print" 1000
	return;

money=1000
addMoney(10)
print (money)

#dir() is a buil-in function

print(dir(support))

#globals and locals functions
#print (globals())
#print locals()
def testGlobalsLocals():
	par=""
	#print (globals()) #gives a big output
	print(locals())

testGlobalsLocals()

#learning packaging with package name phone
import phone
phone.pot("iphone6")
phone.bob("iphone7")

print (dir(phone))
#naming conventions
# module_name, package_name, ClassName, method_name, ExceptionName
# function_name, GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name, function_parameter_name, local_var_name

#class examples
class Employee: #(object):
	"""docstring for Employee"""
	emp_count=0
	def __init__(self, name, salary):
		#super(Employee, self).__init__()
		self.name = name
		self.salary = salary
		Employee.emp_count=Employee.emp_count+1

	def display_count(self):
		print ("total count = %d" %self.emp_count)

	def display_employee(self):
		print ("employee name %s, employee salary - %d"%(self.name, self.salary))

emp1=Employee("sandeep",1000)
emp1.display_count()
emp1.display_employee()
emp2=Employee("Jagat",1000)
emp2.display_employee()
emp2.display_count()

print (emp1.emp_count, "emp2", emp2.emp_count, "employee", Employee.emp_count)
print emp1.emp_count, "emp2", emp2.emp_count, "employee", Employee.emp_count #what is the difference from above print statement. above print tuple, whereas this prints variables values only
emp1.salary = 2000
#class fundtions
print  ( getattr(emp1,'name'), hasattr(emp1,'salary'), setattr(emp1,'empid',1), delattr(emp1,'empid') )

#Built in class attributes
print ("Employee.__doc__:", Employee.__doc__)
print ("Employee.__name__:", Employee.__name__)
print ("Employee.__module__:", Employee.__module__)
print ("Employee.__bases__:", Employee.__bases__)
print ("Employee.__dict__:", Employee.__dict__ )

class Library(Employee):
	"this class stroe library related txn information"
	def __init__(self,books):
		self.books = books
	def display_books(self):
		print "employee - ", Employee.emp_count ,"has books", self.books

emp3=Library(2)
emp3.display_books()
#emp3.display_employee()
emp3.display_count()

print (issubclass(Library,Employee), issubclass(Employee,Library), isinstance(emp3,Employee), isinstance(emp3,Library))
print __name__

#regular expressions
import re
line="this is a test text message #<testing re module> "
match_obj = re.match('.*test text(.*) #<(.*) $',line,re.I)
if match_obj:
	print ("match_obj.groups()", match_obj.group(), match_obj.group(1),match_obj.group(2))
else:
	print("no match")

#match vs search # match checks at the beginning of the string whereas search checks the entore string. 
#del match_obj
match_obj=re.match(r'text',line,re.I)
if match_obj:
	print ("match_obj.groups()", match_obj.group(), match_obj.group(1),match_obj.group(2))
else:
	print("no match")

search_obj=re.search(r'text',line,re.I)
if search_obj:
	print(search_obj.group())
else:
	print "pattern not found"

#can we create object of a module?
obj1=support.par #just testing this is not a object
print obj1
obj1="objtest"
print obj1, support.par

#obj=support()
#print obj.par
obj=support
print obj.par
print dir(obj)

# print "enter the limit of the list"
# limit=int(raw_input())
# print "entered value",  limit

#File I/O
# raw_input=int(raw_input("enter number"))
# input=input("enter number..")
# print raw_input, "input - " , input

fo =open("foo.txt","wb+")
print "file name", fo.name
print "file closed", fo.closed
print " file opening mode", fo.mode
print "Softspace flag", fo.softspace
fo.write("Python is a great language.\nYeah its great!!\n")	
fo.close()


fo = open("foo.txt", "ab+")
var=fo.read(10)
print "reading file foo.txt - ", var
new_var = raw_input("enter content to put in file foo.txt...")
fo.write( new_var)










