
""" Exception Handling is a mechanism to handle runtime errors """

"""
try
except
else
finally
"""

# dt = {'name':'abc','age':12}
#
# dt['salary']
#
# dtt
# 100/0

''' ZeroDivisionError '''

# value = int(input('Enter a number: '))
#
# try:
#     result = 100/value
#     print('result', result)
#     print('try')
# except Exception as err:
#     print(err)
#     print('except')
#     print('Please enter a value grater than 0')

'''
try:
    result = 100/value
    print('result', result)
    print('try block')
except ZeroDivisionError:
    print('except block')
    print('Please enter a value grater than 0')
    
'''

# 100/value

dt = {'age':30}

# dt['salary']
'''
try:
    # result = 100/value
    dt['salary']
    print('try block')
except ZeroDivisionError:
    print('Zero division error except block')
except NameError:
    print('Name error except block')
except KeyError:
    print('Key error except block')
    
'''

'''
try:
    result = 100/0
    # dt['salary']
    # print(value)
    print('try block')
except (ZeroDivisionError, NameError,KeyError):
    print('except block')
    
'''

value = int(input('Enter a number: '))

try:
    result = 100/value
    print('result try - ', result)
    print('try block')
except ZeroDivisionError:
    result = 100/10
    print('result except - ',result)
    print('except block')
else:
    print('else block')
finally:
    print('finally block')

# try -> else -> finally
# except -> finally

