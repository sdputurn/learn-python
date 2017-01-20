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

