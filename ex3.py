import os
f_obj=open("accounts.csv","wb+")
new_account="101"+","+"sandeep"+','+"5000"
print "a file handling example module:", __name__
f_obj.write("""hello
""")
# f_obj.write("putting soma sample data")
# f_obj.write('''this is a test string:\n - to test the string count
#  - to check the length fo the string
#  - replace a string with gven string eg - all ee to i
#  - find some sting with in operator and by using program logic''')

#f_obj=open("accounts.csv","r+")
print f_obj.tell()
f_obj.seek(0)
print f_obj.tell()
print f_obj.read()
os.rename("accounts.csv","accounts_bkp.csv")
f_obj.close()
import os, sys

# using command mkdir
a = 'touch a'

b = os.popen(a)

print b