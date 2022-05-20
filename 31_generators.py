''''

A generator is a function that returns generator object which we can iterate over.
Generator function contains yield keyword instead of return
'''


# def test():
#     return 1
#
# def demo():
#     yield 2

# a = test()
# b = demo()
#
# print(a)
# print(b)

def test():
    for i in [100,200,300,400]:
        return i*i

# print(test())

def demo():
    for i in [100,200,300,400]:
        yield i*i
    yield 'abc'
    yield 1234

gt = demo()

print(gt)

# import sys
# print(sys.getsizeof(list(range(1,1000))))
# print(sys.getsizeof(gt))

print(next(gt))
print(next(gt))
print('***************')
for i in gt:
    print(i)





