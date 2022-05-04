
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

# print(multiply(10,20,5))


def sample_test(value,name='venky'):
    print(value)  # positional argument
    print(name)   # keyward argument

# sample_test(123)
# sample_test(123,'ravi')
# sample_test(123,name='mohan')


def fun_args(a,b,c,value=None):
    print(a)
    print(b)
    print(c)
    print(value)

# fun_args(1,2,3,value=100)


def args_kwargs(*args,**kwargs):
    print('args ----',args)
    print('kwargs ---',kwargs)

# args_kwargs(1,2,3,name='mohan',age=30)

def args_kwargs2(*abc,**xyz):
    print('abc ----',abc)
    print('xyz ---',xyz)

# args_kwargs2(1,2,3,name='mohan',age=30)
# args_kwargs2(1,2,3,age=30,name='mohan')


value = 100   # Global variable
def scope():
    value = 10  # Local variable
    print('inner scope - ',value)

print('outter scope',value)
scope()
















