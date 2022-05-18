"""
Reduce takes function as a first argument and applies the given condition to return a consolidated result

"""

"""
syntax:

reduce(fun, sequence)

"""

from functools import reduce

print(reduce(lambda x,y:x+y,[1,2,3,4,5,6]))

# print(reduce(lambda x,y:x+y,range(1,101)))


