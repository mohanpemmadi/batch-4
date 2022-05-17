keys = ['name','age','salary']
values = ['sai',30,10000]

"""
for key,value in zip(keys,values):
    print(key)
    print(value)
    print('############')

"""

# dt = {key:value for key,value in zip(keys,values)}
dt = {a:b for a,b in zip(keys,values)}

# print(dt)

t1 = (1,2,3)
t2 = (100,200,300)

dt2 = {j:i for i,j in zip(t1,t2)}
# print(dt2)

lst1 = [1,2,3,4,5]
lst2 = [6,7,8,9,10]

dt3 = {lst1[i]:lst2[i] for i in range(len(lst1))}

print(dt3)