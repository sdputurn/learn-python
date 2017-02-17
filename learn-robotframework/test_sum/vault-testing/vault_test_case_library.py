#!/usr/bin/python
import requests
import sys
import getopt
import json
import os
import paramiko



def store_secrets(url, app_id, access_token):
	print "running store secrets test case..."
	headers={'content-type': 'application/json', 'X-Vault-Token': access_token}
	print headers
	data={'test':'test message'}
	print json.dumps(data)
	r=requests.post(url +'/'+ app_id, data='{"test":"message"}', headers=headers )
	print 'r.url - ', r.url
	print r.status_code
	print 'r.content - ',r.content
	if r.status_code == 201:
		print 'Pass'
	else:
		print 'Fail'


def read_secrets(url, app_id, access_token):
	print "running read secrets test case..."
	headers={'content-type': 'application/json', 'X-Vault-Token': access_token}
	r=requests.get(url +'/'+ app_id +'/1', headers=headers)
	print r.status_code
	# print 'r.headers', r.headers
	print 'r.content',r.content
	if r.status_code == 200:
		print 'Pass'
	else:
		print 'Fail'

#def get_container_id_from_container_ip(contianer_ip):


def check_secrets_passed_to_app_container(app_id):
	# choice=''
	# print "checking if the app is already running"
	# headers={'content-type': 'application/json'}
	# r=requests.get("http://jsonplaceholder.typicode.com" + '/'+ app_id, headers=headers)
	# print r.status_code, "r.content - ", r.content
	# if r.status_code != 404:
	# 	print "seems like app is already running.. please remove app and then test again"
	# 	choice = raw_input("would you like to destoy running app (y/n).. ")
	# if choice in ('y', 'Y'):
	# 	r=requests.delete("http://jsonplaceholder.typicode.com" + '/'+ app_id)
	# 	if r.status_code ==200:
	# 		print "application deleted, proceesing with the test.."
	# 	else:
	# 		print "currently unable to delete app. please delte app and run this test"
	# 		return "Fail"
	# else:
	# 	return "Fail"
	# print "launching app with app_id - ", app_id
	# f_obj=open(os.getcwd() + os.sep + 'vault-testing' + os.sep + 'app.json', "r+")
	# buffer=json.load(f_obj)
	# f_obj.close()
	# print buffer
	# buffer['test']= app_id
	# jbuffer=json.dumps(buffer)
	# print jbuffer
	# r=requests.post("http://jsonplaceholder.typicode.com" + '/' + 'posts', data=jbuffer, headers=headers)
	# print r.status_code, "r.content - ",r.content
	# if r.status_code == 201:
	# 	print "application launched successfully"
	# 	print "r.content - ", r.content
	# else:
	# 	return "Fail"
	print "proceesing futher to read secrets from containers"
	print "querying marathon json or the app.. currently using localfile"
	f_obj=open(os.getcwd()+'/vault-testing/container_info.json', "r+")
	buffer=json.load(f_obj)
	f_obj.close()
	jbuffer=json.dumps(buffer)
	print jbuffer, type(jbuffer), buffer, type(buffer)
	print buffer['host_ip']#, jbuffer['container_ip']
	ssh_client = ssh_connect(buffer['host_ip'])
	stdin, stdout, stderr = ssh_client.exec_command( "docker network inspect --format '{{json .Containers }}'  bridge")
	print "got list of continer from the host - ", buffer['host_ip']
	x=stdout.readlines()
	print "printinggggggggggggggg", x[0], type(x[0])
	j=json.loads(x[0])
	z=stderr.readlines()
	print stdout.readlines(),x, "errorrrrrr" , z,"input......", stdin , type(x), "\n printing jjjjjjjjj", j, type(j)
	container_id = ''
	count=0
	for key in j:
		count = count + 1
		if j[key]['IPv4Address'] == buffer['container_ip']:
			container_id = key
			break
		if len(j.keys()) == count:
			print "container not found.. looks like some error.. exiting.."
			sys.exit(2)
	print " got continer id - ", container_id
	cmd = "docker exec -it "+ container_id + " sh -c env"
	print "running command...............", cmd
	stdin, stdout, stderr = ssh_client.exec_command(cmd, get_pty=True)
	x=stdout.readlines()
	#y=stdin.readlines()
	z=stderr.readlines()
	print "out", x, "stdinnnnnnnn", "stderr - ---- ", z
	if "TERM=xterm\r\n" in x:
		print "keys present "





def check_mounted_volumes(json_dict):
	ssh_client=ssh_connect('192.168.56.101')
	stdin, stdout, stderr = ssh_client.exec_command("mount")
	x=stdout.readlines()
	ssh_client.close()
	extflag=1
	#print x
	for i in x:
		#print i
		if "/dev/mapper/VolGroup00-LogVol00 on /" in i:
			#print i
			extflag=0
			break
	if extflag == 0:
		return 'Pass'
	else:
		return 'Fail'




def ssh_connect(conn_details):
	ssh_client=paramiko.SSHClient()
	ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	path_to_key=os.path.join(os.environ['HOME'], '.ssh', 'id_rsa')
	ssh_client.connect(conn_details, username='vagrant', key_filename=path_to_key)
	return ssh_client

# fd=open(Pth+'mon-nginx.json','r')
#        buffer=json.load(fd)
#        print buffer
#        fd.close()
#        print '\n\n======================================'
#        print '          Editing joson file                        '
#        print '======================================'
#        for ele in SetDetails.json_parameters.keys():
#            #print 'ele',ele,SetDetails.json_parameters[ele]       
#            if ele == 'mon-nginx':
#               print '**',SetDetails.json_parameters['mon-nginx'].has_key('MON_EXTSVCIPv4')
#               if SetDetails.json_parameters['mon-nginx'].has_key('MON_EXTSVCIPv4'):
#                  buffer["ExtNetEnv"]["MON_EXTSVCIPv4"]=SetDetails.json_parameters['mon-nginx']['MON_EXTSVCIPv4']
#        #updating json with webserver image
#        if SetDetails.Final_App_Images.has_key('qawebserver'):
#           pass
#           buffer['container']['docker']['image']=SetDetails.Final_App_Images['qawebserver']









def test_HTTP_REST(url,num):
	headers={'content-type': 'application/json', 'X-Vault-Token': 'sdfdfd'}
	r=requests.get(url +'/'+ num, headers=headers)
	print r.status_code
	print 'r.headers', r.headers
	print 'r.content',r.content
	if r.status_code == 200:
		print 'Pass'
	else:
		return 'Fail'
	data={'test':'test message'}
	print json.dumps(data)
	print data.keys()
	print data.values()
	print data['test']
	r=requests.post(url, data='{"test":"message"}', headers=headers )
	print 'r.url', r.url
	print r.status_code
	print 'r.headers', r.headers
	print 'r.content',r.content
	if r.status_code == 201:
		print 'Pass'
	else:
		return 'Fail'

def main(argv):
	default_url = "http://jsonplaceholder.typicode.com"
	url=''
	app_id=''
	access_token=''
	# print "number of arguments - ", len(argv)
	# print "aguments - ", argv
	if len(argv) == 0:
		print "script needs arguments"
	try:
		opts, args = getopt.getopt(argv,"hu:i:t:",["url=","app_id=","access_token="])
	except getopt.GetoptError, e:
		print "got exception", e
		print "usage: script -u url -i app_id -t access_token"
		sys.exit(2)
	# print "args - ", args, "opts - ", opts
	for opt,arg in opts:
		if opt == '-h':
			print "usage: script -u url -i app_id -t access_token"
		if opt in ("-u","--url"):
			url = arg
		elif opt in ("-i","--app_id"):
			app_id = arg
		elif opt in ("-t", "--access_token"):
			access_token = arg
	print "url - ", url, "app_id - ", app_id,"access_token - ", access_token
	# store_secrets(url, app_id, access_token)
	# read_secrets(url, app_id, access_token)
	print check_secrets_passed_to_app_container(app_id)

main(sys.argv[1:])