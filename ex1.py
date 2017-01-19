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
		sys.stdout.write("* ")
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
	print (globals())
	print(locals())

testGlobalsLocals()

#learning packaging with package name phone
import phone
phone.pot("iphone6")
phone.bob("iphone7")







