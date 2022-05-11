import json

# load -> to load the data from file
# dump -> push the data into file

""" load """

# f = open("sample.json",'r')
# data = json.load(f)
# print(f.closed)

# print(data)


# for row in data:
#     row['salary'] = 1000
    # print(row)
    # print('###########')

""" dump """

# g = open('sample2.json', 'w')
# json.dump(data, g)
# print(g.closed)


""" Context Manager - 	context manager take care of resource allocation and release """

# with open("sample.json") as f:
#     data = json.load(f)
#
# with open('sample3.json','w') as abc:
#     json.dump(data,abc)

# print(data)
# print(f.closed)


st = 'pythonpythonabababaap'

dt = dict.fromkeys(st,0)

for char in st:
    if char in dt:
        dt[char] = dt[char]+1

print(dt)








