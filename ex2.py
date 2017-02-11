def print_pattern(n):
	for i in range(1,n+1):
		for j in range(0,i):
			print "* ",
		for j in range(i,n):
			print "  ",
		for j in range(i,n):
			print "  ",
		for j in range(0,i):
			print "* ",
		print "\n"
n=int(raw_input("enter star pattern limit: "))
print_pattern(n)

def print_pattern_rev(n):
	for i in range(1,n+1):
		for j in range(i,n+1):
			print "* ",
		for j in range(1,i):
			print "  ",
		for j in range(1,i):
			print "  ",
		for j in range(i,n+1):
			print "* ",
		print "\n"


print_pattern_rev(n)

#String processing examples
#single quote and double quote are treated as same.

# print "my name is %s and weight is %d !!!" %('Zara', 21)
# print 'my name is %s and weight is %d !!!' %("Zara",21)



# e_string = '''this is a test string:\n
#  - to test the string count
#  - to check the length fo the string
#  - replace a string with gven string eg - all ee to i
#  - find some sting with in operator and by using program logic'''

e_string=raw_input("enter paragraph - ")
# print "string sount function syntax:\n",e_string.count.__doc__

# print e_string[0:20], "string" in e_string, e_string[0:20].capitalize(), "count - ", e_string.count("string",0, len(e_string))

pattern=raw_input("enter pattern to search - ").upper()
u_string=e_string.upper()
count=0
#below code is for fixed string length
# try:
# 	for i in range(0,len(e_string)):
# 		if u_string[i] ==pattern[0]:
# 			if u_string[i+1] == pattern[1]:
# 				if u_string[i+2] == pattern[2]:
# 					if u_string[i+3] == pattern[3]:
# 						if u_string[i+4] == pattern[4]:
# 							if u_string[i+5] == pattern[5]:
# 								count = count +1
# 							else:
# 								i = i +5
# 						else:
# 							i=i+4
# 					else:
# 						i = i+3
# 				else:
# 					i=i+2
# 			else:
# 				i=i+2
# except IndexError, e:
# 	print "looks like index error", e

# print "count of pattern - ", count
s_len = len(pattern)
# print u_string[10]
try:
	for i in range(0,len(e_string)):
		# print i
		# print u_string[i:i+s_len], pattern
		if u_string[i:i+s_len] == pattern:
			count=count+1
			i=i+s_len
			if i+s_len > len(e_string):
				break
		else:
			i=i+s_len
			if i+s_len > len(e_string):
				break
except IndexError,e:
	print "looks like index error"
print "count of pattern - ",count


