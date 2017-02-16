import paramiko
import os
import requests
import json
def print_pattern():
	i=0
	while (i<5):
		print "print", i
		i=i+1

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

#test some REST calls

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
















