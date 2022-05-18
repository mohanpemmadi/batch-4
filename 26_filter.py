
"""
The filter function takes other function as a first argument and applies the given condition to each item in the sequence

"""
"""
Syntax:

filter(fun,sequence)

"""

def even(num):
    if num%2==0:
        return True
    else:
        return False

# print(even(5))


res = filter(even,[1,2,3,4,5,6])

# for i in res:
#     print(i)

print(list(filter(lambda num: num%2==0, [1,2,3,4,5,10,122,121])))






