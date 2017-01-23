import schoolMathExamples

num=int(raw_input("enter the limit:"))

# list=[]
# i=1
# while (i<=num):
# 	list[i]=int(raw_input("enter numner:"))
# 	i+=1

# print "your list", list
list=[]
i=0
while i<num:
	list.append(int(raw_input("enter numer:")))
	i=i+1

print "max num in list - ", schoolMathExamples.find_max(list)
print "min num in list - ", schoolMathExamples.find_min_while_loop(list)
print "sorted list - ", schoolMathExamples.sorting(list)