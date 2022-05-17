"""

Lambda is an anonymous function in Python,we use lambda functions when we require a nameless function for a short period of time

"""

# def test():
#     pass

"""
Syntax:

lambda arguments:expression(logic)

"""

def test(n):
    return n*n

def test2(lst):
    res = []
    for i in lst:
        res.append(i*i)
    return res
print(test2([10,20,30]))

# print(test(10))
# print(test(8))

res = lambda n:n*n
# print(res(11))

result = lambda a,b,c:a+b+c
# print(result(10,20,30))

# print(lambda n:n*n)

n = lambda name:name.upper()
print(n('ravi'))

