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
#print (str(num))
#print (eval(num))

#operators
num1=9
num2=2
print ("num1+num2, num1-num2, num1*num2, num1/num2, num1%num2, num1//num2, num1>num2, num1==num2", num1+num2, num1-num2, num1*num2, float(float(num1)/num2), num1%num2, num1//num2, num1>num2, num1==num2)




