
'''

	Iterables are objects, which one can iterate over, like list,tuple,dictionary etc

'''

lst = [1,2,3,4]
st = 'python'
num = 123

# print(dir(lst))

''' 	

An iterator is an object that can be iterated upon, we can use iter method to create a iterator from iterables.

'''

l = [100,2,300,4,500,6,700,8,900,10]
# l = list(range(1,1000000))

it = iter(l)

# print(type(it))

import sys

# print(sys.getsizeof(l))
#
# print(sys.getsizeof(it))

# print(next(it))
# print(next(it))
# print(next(it))

# for i in it:
#     print(i)







