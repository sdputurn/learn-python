import os
import json
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

#print b
f_obj=open("test1.json",'r+')
x=json.load(f_obj)

print "json load function", x, type(x)
f_obj.seek(0)
x=f_obj.readlines(0)
f_obj.close()

print "x reading lines from file", x , type(x)

json_string='''[{"dict_item1":"milk",
"dict_item2":"bread"}]'''
buffer = json_string
print json_string, type(json_string)

x=json.loads(buffer)

print "json_load", x , type(x)
print x[0], type(x[0])

#with above examples, we understand load works on file objects and loads works on Strings

#learning json dump and dumps (dump string) functions
json_string=[{'json_item1':"milk"}]

x=json.dumps(json_string,indent=4)

print x, type(x)

f_obj=open("test1.json", 'r+')
x=f_obj.readlines()
result_f_obj=open("result.json","w+")
json.dump(x, result_f_obj, indent=4)

result_f_obj.seek(0)

print "encoding a python object into valid json ", x, "json dump", result_f_obj.read(), type(result_f_obj)







