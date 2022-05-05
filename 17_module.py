
"""
Module is a python file that can be imported inside another file.

"""

# Method - 1

'''
import calc

print(calc.value)
print(calc.add(20,10))
print(calc.mul(5,10))

'''


# Method - 2

'''
from calc import sub,div,value

print(sub(10,5))
print(div(20,2))

'''

# Method - 3

'''
from calc import *

print(add(20,30))
print(value)

'''


# Method - 4
# # filename - break_continue_pass as bcp
#
# bcp.add()
'''
import calc as cl

print(cl.value)
print(cl.div(100,10))

'''

from test import sample

print(sample.email('abc','xyz'))


from test2 import sample2

print(sample2.demo())

