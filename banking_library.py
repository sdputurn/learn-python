#!/bin/python

class Customer:
	"""docstring for Customer"""
	acc=0
	customer_count=0
	def __init__(self, salary,name):
		#super(Customer, self).__init__()
		self.acc = Customer.customer_count + 1
		self.name=name
		self.salary=float(salary)
		Customer.customer_count=Customer.customer_count+1
	def display(self):
		print "############### Customer informations ##############"
		print "name - ", self.name
		print "acc - ", self.acc
		print "salary - ", self.salary
		# var=Customer.customer_count + 1
		# print "total customer..." , var
		print "####################################################"
	def return_acc(self):
		return self.acc
