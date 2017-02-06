
import os
import sys
import subprocess
import cPickle

def my_sum(var1,var2):
	sum=int(var1)+int(var2)
	return sum
def my_sub(var1,var2):
	sub=int(var1)-int(var2)
	return sub

def run_testcase(tsid,tcid):
    test_case_pwd = _getTCPath(tsid,tcid)
    run_cmd = 'python ' + test_case_pwd +os.sep+tcid+'.py'
    fd_log=open(tcid+".html",'w')
    p = subprocess.Popen(run_cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE,shell=True)
    out, err = p.communicate()
    fd_log.write(out)
    fd_log.write(err)
    fd_log.close()
    print(out)
    if len(err) != 0:
    	  print len(err)
          _result=_decide('Fail') 
    if p.returncode != 0:
    	  print p.returncode
          _result=_decide('Fail') 
    _result=_decide('Pass')
    return _result

def _getTCPath(tsid,tcid):
        tc_path=os.getcwd()+ os.sep+ tsid + os.sep + tcid 
        return tc_path


def _decide(result):
        if result == 'Pass':
           return 'Pass'
        else:
           raise ExecuteError('Failed TestCase')



#run_testcase('test_suite_test', 'testcase001')

class ExecuteError(Exception):
    pass


	