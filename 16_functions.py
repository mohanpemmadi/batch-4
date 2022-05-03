
"""

Function - Function is a block of reusable code

"""
'''

syntax : 

def function_name(argument):
    pass

'''

def sample():
    # print('called')
    pass

# sample()
# sample()
# print(sample())


def test():
    return 'hello world'

# print(test())


def demo(name):  # name - positional argument
    print('---------------',name)
    res = name.upper()
    print('###################',res)
    return res


# print(demo('venky'))
# print(demo('mohan'))
# print(demo('sai'))
# print(demo())

def sum(a,b):
    c = a+b
    return c

# print(sum(10,20))
# print(sum(5,-5))
# print(sum(5.23,5.23))


def multiply(value1,value2,value3):
    final_res = sum(value1,value2) * value3
    return final_res

print(multiply(10,20,5))




