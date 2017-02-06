import subprocess
try:
	subprocess.call(["xyz"])
	subprocess.check_call("xyz")

except subprocess.CalledProcessError:
	print "command failed"
