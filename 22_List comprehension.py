
""" List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list """
lst = [10,20,30]
# [1,4,9]

# result = []
# for i in lst:
#     result.append(i*i)
#
# print(result)

names = ['ravi','siva','sai']

res = [i*i for i in lst]

# print(res)

result = [name.upper() for name in names]
# print(result)

evens = [i for i in range(1,20) if i%2 == 0]
# print(evens)

['true result' if 'condition' else 'else result']

even_odd = [('even',i) if i%2 == 0 else ('odd',i) for i in range(1,10)]
print(even_odd)

