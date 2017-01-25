#!/bin/python
#this module contains code examples for any doubts or questions comes in mind

#checking scope of var
var="sandeep"
def scope_check():
	print "valuse in function before override - ", var
	global var
	var="test sandeep"	
	print "value in function - ", var
print "value outside function - ",var
scope_check()
print "value outside function - ",var