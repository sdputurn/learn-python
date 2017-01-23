import sys
def fibonacci(n):
	a=0;b=1;fib=0
	sys.stdout.write("%d" % a)
	sys.stdout.write(" ")
	sys.stdout.write("%d" % b)
	while (fib<n):
		fib=a+b
		a=b
		b=fib
		print " ",fib, 
	return;

if __name__ == "__main__":
	fibonacci(100)

def sorting(list):
	limit = list.length()
	i=0
	while (i<limit):
		while (j<i):
			if limit[i] > limit[j]:
				tmp=lmit[i]

def find_max(list):
	tmp=list[0]

	for i in list[1:]:
		if tmp < i:
			tmp=i
	return tmp


def find_min_while_loop(list):
	i=1
	tmp=list[0]
	while i < len(list) :
		if tmp > list[i]:
			tmp=list[i]
		i=i+1
	return tmp

def sorting(list):
	i=0
	tmp=list[0]
	while i< len(list):
		j=i+1
		while j< len(list):
			if list[i] > list[j]:
				tmp=list[j]
				list[j]=list[i]
				list[i]=tmp
			j=j+1
		i=i+1
	return list

