import os
import sys
from termcolor import colored

for pth in os.environ['PATH'].split(':'):
    sys.path.append(pth)
sys.path.append(os.environ['PATH'])
sys.path.append(os.getcwd())
my_library_path= os.getcwd() + os.sep +'my_library'
#sys.path.append(my_library_path)

from my_library.test_functions import *
#import my_library.test_functions
from my_library import test_functions
#import test_functions
#print dir(my_library) #, "my_functions", dir(test_functions)
print dir(test_functions)
test_functions.print_pattern()
print_pattern()

# from my_library.test_case_library import *
# print_pattern()
# import test_case_library
# print dir(test_case_library)
# from test_case_library import *
import my_library.test_case_library
print my_library.test_case_library.name
my_library.test_case_library.print_pattern()
print dir(my_library.test_case_library)


# from my_library_test_function import *
# my_print()

result=check_mounted_volumes({"hostname":"192.168.56.101"})
if result == "Pass":
	print "check mounted volumes", colored("Pass", "green")
else:
	sys.exit(1)

result = test_HTTP_REST("http://jsonplaceholder.typicode.com/posts","1")
if result == "Pass":
	print "check HTTP REST", colored("Pass", "green")
else:
	sys.exit(1)
