*** Settings ***
Library  my_functions.py

*** Keywords ***
test sum function
  [arguments]  ${var1}  ${var2}
  ${return} =  my sum  ${var1}  ${var2}
  ${int_output} =  Evaluate  ${var1}+${var2}
  log to console  ${int_output}
  Should be equal  ${return}  ${int_output}

test sub function
  [arguments]  ${var1}  ${var2}
  ${return} =  my sub  ${var1}  ${var2}
  ${int_output} =  Evaluate  ${var1}-${var2}
  log to console  ${int_output}
  Should be equal  ${return}  ${int_output}
run my testcase
  [arguments]  ${var1}  ${var2}
  ${return} =  run testcase  ${var1}  ${var2}
  log to console  ${return}
  Should be equal  ${return}  Pass

*** Test Cases ***
Sum function Test
  test sum function  ${var1}  ${var2}
  Should be equal  3  3
Subtract function test
  test sub function  ${var1}  ${var2}
  # ${result} =  my sub  ${var2}  ${var1}
  # Should be equal  ${result}  1


test_case_suite_test_001
  run my testcase  ${test_suite_var}  testcase001

test_case_suite_test_002
  run my testcase  ${test_suite_var}  testcase002

*** Variables ***
${var1}  4
${var2}  5
${test_suite_var}  test_suite_test
    # ${result}=  my sum  1  2
    # Should be equal  ${result}  3