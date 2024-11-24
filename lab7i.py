#!/usr/bin/env python3
# Student ID: rrpatel51

def function1():
    global schoolName  # Use the global variable
    schoolName = 'SICT'
    print('print() in function1 on schoolName:', schoolName)

def function2():
    global schoolName  # Modify the global variable
    schoolName = 'SSDO'
    print('print() in function2 on schoolName:', schoolName)

schoolName = 'Seneca'  # Global variable
print('print() in main on schoolName:', schoolName)
function1()  # This modifies the global 'schoolName'
print('print() in main on schoolName:', schoolName)
function2()  # This modifies the global 'schoolName'
print('print() in main on schoolName:', schoolName)
