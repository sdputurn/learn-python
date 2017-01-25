import banking_library


list=[]
while True:
	print "1. add customer.."
	print "2. display customer.."
	choice=int(raw_input("Enter choice.."))
	if choice == 1:
		name=raw_input("enter customer name..")
		#acc=int(raw_input("enter acc no..."))
		salary=float(raw_input("enter salary.."))
		list.append(banking_library.Customer(salary,name))
		print ("Hi %s . your account created. your account number is.. %d" %(name, list[-1].customer_count))
	elif choice ==2:
		account=int(raw_input("enter acc numner..."))
		# list[acc-1].display()
		for i in list:
			if i.return_acc() == account:
				i.display()
				break
			if i == list[-1]:
				print "account not found"
		# print "account not found"
	else:
		print "invalid choice"


