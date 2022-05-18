'''

The map function takes function as a first argument and applies a given function to each item in the sequence


'''
def cube(num):
    return num*num*num

# print(cube(4))

lst = [1,2,3,4,5]

for i in lst:
    print(cube(i))

"""
Syntax:

map(fun, sequence)

fun - function name
sequence - list,tuple,dict,set

"""

res = map(cube, (1,2,3))
# print(res)
#
# for i in res:
#     print(i)

map(lambda num:num*num*num,[3,4,5])

# print(list(map(lambda num:num*num*num,[3,4,5])))

map_obj = list(map(lambda name:name.upper(),['a','b','c']))

# for name in map_obj:
#     print(name)

print(map_obj)




