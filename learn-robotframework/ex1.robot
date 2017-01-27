*** Settings ***
| Library | my_library.py

*** Test Cases ***
| Example that calls a python keyword
| | ${result}= | join two strings | hello | world
| | Should be equal | ${result} | hello world